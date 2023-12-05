import numpy as np

class Ripples():
    def __init__(self, bias = 3, sigma = 1, omega = 2*2**0.5, k = 0.1):
        self.bias = bias
        self.sigma = sigma
        self.omega = omega
        self.k = k
    
    def calculate(self, x):
        f = 0
        dim = len(x)
        M = np.eye(dim,dim) * self.bias
        for i in range(dim):
            singleModality = np.exp(-(0.5*(self.sigma**-2))*np.dot(x + np.array(M[i]), x+np.array(M[i]))) \
                             + self.k * np.cos(self.omega * np.pi * np.linalg.norm(x+np.array(M[i]))) - self.k
            f += singleModality
        return f  
    

if __name__ == '__main__':

    func = Ripples()

    x = [0,0,0,-3]

    print(func.calculate(x))