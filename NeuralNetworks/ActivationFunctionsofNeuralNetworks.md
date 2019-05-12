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


# Why derivative/differentiation is used ?
When updating the curve, to know in which direction and how much to change or update the curve
depending upon the slope.That is why we use differentiation in almost every part of Machine Learning
and Deep Learning.

![All Activation Functions and their
Derivatives](./images/AllActivationFunctionsandtheirDerivatives.png)


References :
https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6
