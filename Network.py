import numpy as np
import random


def sigmoid(x):
    sigma = 1 / (1 + np.exp(-x))
    return sigma

def sigmoid_prime(x):

    return sigmoid(x)*(1-sigmoid(x))

def softplus(x):
    zeta = np.log(1 + np.exp(x))
    return zeta

def reLU(x):
    y = np.maximum(0,x)
    return y

class Network(object):
    def __init__(self, sizes, *args, **kargs) -> None:
        self.num_layers = len(sizes)
        self.sizes = sizes

        self.biases = [np.random.randn(y, 1) for y in sizes[1:]]
        self.weights = [np.random.randn(y, x) 
                        for x, y in zip(sizes[:-1], sizes[1:]) ]

    def feedforward(self, a):

        for b, w in zip(self.biases, self.weights):
            a = sigmoid(np.dot(w, a) + b)
        
        return a
    

    def SGD(self, training_data, epochs, mini_batch_size, eta, test_data=None):

        if test_data: n_test = len(test_data)

        n = len(training_data)
        for j in range(epochs):
            random.random.shuffle(training_data)
            random.shuffle(training_data)

            mini_batchs = [
                training_data[k:k+mini_batch_size]
                for k in range(0, n, mini_batch_size)
            ]

            for mini_batch in mini_batchs:
                self.update_mini_batch(mini_batch, eta)

            if test_data:
                print ("Epoch {0}: {1} / {2}".format(
                    j, self.evaluate(test_data), n_test
                ))
            else:
                print ("Epoch {0} complete".format(j))
    
    def update_mini_batch(self, mini_batch, eta):

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]

        for x, y in mini_batch:
            delta_nabla_b, delta_nabla_w = self.backprop(x, y)
            nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
            nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]

        self.weights = [w-(eta/len(mini_batch))*nw 
                        for w, nw in zip(self.weights, nabla_w)]
        self.biases = 0


    def backprop(self, x, y):

        nabla_b = [np.zeros(b.shape) for b in self.biases]
        nabla_w = [np.zeros(w.shape) for w in self.weights]
        activation = x
        activations = [x]
        zs = []

        for b, w in zip(self.biases, self.weights):

            z = np.dot(w, activation) + b
            zs.append(z)
            activation =self.non_linearity(z)
            activations.append(activation)

        delta = self.cost_derivative(activations[-1], y) *\
            self.d_non_linearity(zs[-1])
        
        nabla_b[-1] = delta
        nabla_w[-1] = np.dot(delta, activations[-2].transpose())


        for l in range(2, self.num_layers):
            z = zs[-l]
            sp = self.d_non_linearity(z)
            delta = np.dot(self.weights[-l+1].transpose(), delta) * sp
            nabla_b[-l] = delta
            nabla_w[-l] = np.dot(delta, activations[-l-1].transpose())
        
        return (nabla_b, nabla_w)



    def non_linearity(x):
        pass


    def cost_derivative(self, output_activations, y):

        return output_activations-y
        

    def d_non_linearity(x):
        pass

    def evaluate(self, test_data):

        test_results = [(np.argmax(self.feedforward(x)), y)
                        for (x, y) in test_data]
        
        return sum(int(x==y) for (x, y) in test_results)
