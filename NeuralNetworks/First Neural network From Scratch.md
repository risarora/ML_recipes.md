import numpy as np # import Numpy library to generate

x_1 = 0.5 # input 1
x_2 = -0.35 # input 2
print('x1 is {} and x2 is {}'.format(x_1, x_2))

weights = np.array([0.55,0.45])  # initialize the biases
biases = np.array([0.15])        # initialize the biases

print(weights)
print(biases)

z = x_1 * weights[0] + x_2 * weights[1] + biases[0]
print('z is {} '.format(z))

a = 1.0 / (1.0 + np.exp(-z))

print('a is {} '.format(a))
