
##### import the numpy package

```python
import numpy as np # import Numpy library to generate   
```

##### define the input values

```python

x_1 = 0.5 # input 1
x_2 = -0.35 # input 2
print('x1 is {} and x2 is {}'.format(x_1, x_2))

```

##### add the weights and bias 


```python

weights = np.array([0.55,0.45])  # initialize the biases
biases = np.array([0.15])        # initialize the biases

print(weights)
print(biases)
```
```python

z = x_1 * weights[0] + x_2 * weights[1] + biases[0]

print('z is {} '.format(z))
```
```python

a = 1.0 / (1.0 + np.exp(-z))

print('a is {} '.format(a))

```
```python


Output :
```
```python
x1 is 0.5 and x2 is -0.35
[0.55 0.45]
[0.15]
z is 0.2675
a is 0.5664790559676278

```
