import numpy as np
from numpy.linalg import inv

def sigmoid_fn(alpha, beta, inputs):
    val = np.exp(alpha + beta * inputs)
    p = val / (1 + val)
    return p

def make_jacob(logits, inputs, labels):
    partial_alpha = np.sum(labels - logits)
    partial_beta = np.sum(inputs * (labels - logits))
    Jacobian_matrix = np.reshape([partial_alpha, partial_beta], [2,1])
    return Jacobian_matrix

def make_information(logits, inputs, labels):
    partial_sq_alpha = -1*np.sum(logits*(1 - logits))
    partial_alpha_beta = -1*np.sum(inputs*logits*(1-logits))
    partial_sq_beta = -1*np.sum(np.square(Days)*logits*(1-logits))
    Hessian_matrix = [[partial_sq_alpha, partial_alpha_beta],[partial_alpha_beta, partial_sq_beta]]
    Information_matrix = -1*inv(Hessian_matrix)
    return Information_matrix

Days = np.asarray([21.,24.,25.,26.,28.,31.,33.,34.,35.,37.,43.,49.,51.,55.,25.,29.,43.,44.,46.,46.,51.,55.,56.,58.])
Response = np.asarray([1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,1.,0.,0.,0.,0.,0.,0.,0.,0.,0.,0.])
iteration = 100
theta = [0.01,0.01]

for i in range(iteration):
    p = sigmoid_fn(theta[0], theta[1], Days)
    J = make_jacob(p, Days, Response)
    I = make_information(p, Days, Response)
    theta = theta + np.reshape(np.matmul(I,J), [2])
    print("iteration:", i, "    theta:", theta)
print("-"*80)
print("P(Days): ", p)

