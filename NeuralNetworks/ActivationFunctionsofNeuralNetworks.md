# Activation Functions in Neural Networks

### Sigmoid Activation Function

![SigmoidFunction](./images/SigmoidFunction.png)
```
def sigmoid(x):
    return 1/(1*np.exp(-x))

```

### Derivative of Sigmoid Activation Function
```
def derivative_sigmoid(x):
    return x*(1-x))
```



References :
https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6
