#include "FPS_GT511C3.h"
#include "SoftwareSerial.h"

int sol = 4;
int piezo = 10;
int val;

FPS_GT511C3 fps(51, 50);

void setup()
{
  Serial3.begin(9600);
  Serial.begin(9600);
  pinMode(sol,OUTPUT);
  pinMode(piezo,OUTPUT);
  delay(100);
  fps.Open();
  fps.SetLED(true);
  Serial.println("Insira a digital");
}

void loop(){
  if(Serial3.available()){
    val = int(Serial3.read());
    if(val == 49){
      tone(piezo,261);
      delay(500);
      tone(piezo,294);
      delay(500);
      tone(piezo,330);
      delay(500);
      noTone(piezo);
      digitalWrite(sol,HIGH);
      delay(1500);
      digitalWrite(sol,LOW);
      delay(1500);
      }}

  if (fps.IsPressFinger())
  {
    fps.CaptureFinger(false);
    int id = fps.Identify1_N();
    if (id <200)
    {
      Serial.print("Verified ID:");
      Serial.println(id);
      tone(piezo,261);
      delay(500);
      tone(piezo,310);
      delay(500);
      tone(piezo,350);
      delay(500);
      noTone(piezo);
      digitalWrite(sol,HIGH);
      delay(1500);
      digitalWrite(sol,LOW);
      delay(1500);
    }
    else
    {
      Serial.println("Finger not found");
      tone(piezo,349);
      delay(500);
      tone(piezo,349);
      delay(500);
      noTone(piezo);
    }
  }
  else
  {
    Serial.println("Please press finger");
  }
  delay(200);
}
