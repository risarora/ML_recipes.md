
### Recap

From the videos, let's recap how a neural network makes predictions through the forward propagation process. Here is a neural network that takes two inputs, has one hidden layer with two nodes, and an output layer with one node.

   

<img src="http://cocl.us/neural_network_example" alt="Neural Network Example" width=600px>

  

Let's start by randomly initializing the weights and the biases in the network. We have 6 weights and 3 biases, one for each node in the hidden layer as well as for each node in the output layer.


```python
import numpy as np # import Numpy library to generate 

weights = np.around(np.random.uniform(size=8), decimals=2) # initialize the weights
biases = np.around(np.random.uniform(size=2), decimals=2) # initialize the biases
```

Let's print the weights and biases for sanity check.


```python
weights[0]=0.15
weights[1]=0.45
weights[2]=0.25
weights[3]=0.55
weights[4]=0.50
weights[5]=0.60
weights[6]=0.40
weights[7]=0.35

biases[0]=0.45
biases[1]=0.25

```


```python
print(weights)
print(biases)
```

    [0.15 0.45 0.25 0.55 0.5  0.6  0.4  0.35]
    [0.45 0.25]


Now that we have the weights and the biases defined for the network, let's compute the output for a given input, $x_1$ and $x_2$.


```python
x_1 = 0.25 # input 1
x_2 = 0.05 # input 2

print('x1 is {} and x2 is {}'.format(x_1, x_2))
```

    x1 is 0.25 and x2 is 0.05


Let's start by computing the wighted sum of the inputs, $z_{1, 1}$, at the first node of the hidden layer.


```python
z_11 = x_1 * weights[0] + x_2 * weights[1] + biases[0]

print('The weighted sum of the inputs at the first node in the hidden layer is {}'.format(z_11))
```

    The weighted sum of the inputs at the first node in the hidden layer is 0.51


Next, let's compute the weighted sum of the inputs, $z_{1, 2}$, at the second node of the hidden layer. Assign the value to **z_12**.


```python
z_12 = x_1 * weights[2] + x_2 * weights[3] + biases[0]
```

Double-click __here__ for the solution.
<!-- The correct answer is:
z_12 = x_1 * weights[2] + x_2 * weights[3] + biases[1]
-->

Print the weighted sum.


```python
print('The weighted sum of the inputs at the second node in the hidden layer is {}'.format(np.around(z_12, decimals=4)))
```

    The weighted sum of the inputs at the second node in the hidden layer is 0.54


Next, assuming a sigmoid activation function, let's compute the activation of the first node, $a_{1, 1}$, in the hidden layer.


```python
a_11 = 1.0 / (1.0 + np.exp(-z_11))

print('The activation of the first node in the hidden layer is {}'.format(np.around(a_11, decimals=4)))
```

    The activation of the first node in the hidden layer is 0.6248


Let's also compute the activation of the second node, $a_{1, 2}$, in the hidden layer. Assign the value to **a_12**.


```python
a_12 = 1.0 / (1.0 + np.exp(-z_12))
```

Double-click __here__ for the solution.
<!-- The correct answer is:
a_12 = 1.0 / (1.0 + np.exp(-z_12))
-->

Print the activation of the second node.


```python
print('The activation of the second node in the hidden layer is {}'.format(np.around(a_12, decimals=4)))
```

    The activation of the second node in the hidden layer is 0.6318


Now these activations will serve as the inputs to the output layer. So, let's compute the weighted sum of these inputs to the node in the output layer. Assign the value to **z_2**.


```python
z_21 = a_11 * weights[4] + a_12 * weights[5] + biases[1]

z_22 = a_11 * weights[7] + a_12 * weights[6] + biases[1]


a_21 = 1.0 / (1.0 + np.exp(-z_21))

a_22 = 1.0 / (1.0 + np.exp(-z_22))

```


```python
print('The activation of the second node in the hidden layer is {}'.format(np.around(a_21, decimals=4)))
```

    The activation of the second node in the hidden layer is 0.7194



```python
Err = (((0.15-0.7194)**2)+((0.85-0.6729)**2))/2
Err/weights[4]
```




    0.35558077


