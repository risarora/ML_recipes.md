### Comparison of activation functions

Some desirable properties in an activation function include:

  * **Nonlinear** – When the activation function is non-linear, then a two-layer neural network can be proven to be a universal function approximator.[5] The identity activation function does not satisfy this property. When multiple layers use the identity activation function, the entire network is equivalent to a single-layer model.
  * **Continuously differentiable **– This property is desirable (RELU is not continuously differentiable and has some issues with gradient-based optimization, but it is still possible) for enabling gradient-based optimization methods. The binary step activation function is not differentiable at 0, and it differentiates to 0 for all other values, so gradient-based methods can make no progress with it.[6]
  * **Range **– When the range of the activation function is finite, gradient-based training methods tend to be more stable, because pattern presentations significantly affect only limited weights. When the range is infinite, training is generally more efficient because pattern presentations significantly affect most of the weights. In the latter case, smaller learning rates are typically necessary.[citation needed]
  * **Monotonic** – When the activation function is monotonic, the error surface associated with a single-layer model is guaranteed to be convex.[7]
  * **Smooth Functions with a Monotonic derivative** – These have been shown to generalize better in some cases.
  * **Approximates identity near the origin** – When activation functions have this property, the neural network will learn efficiently when its weights are initialized with small random values. When the activation function does not approximate identity near the origin, special care must be used when initializing the weights.[8] In the table below, activation functions where {\displaystyle f(0)=0} f(0)=0 and {\displaystyle f'(0)=1} f'(0)=1 and {\displaystyle f'} f' is continuous at 0 are indicated as having this property.


Is the cube root function suitable as a n activation function?

There are a few traits that you want the activation function to have, and cube roots rate as OK-ish:

Nonlinear – check.
Continuously differentiable – no. There is a problem at x=0. Unlike other discontinuous functions like ReLU, although the gradient can be calculated near zero, it can be arbitrarily high as you approach x=0, because d(x^1/3)/dx=1/(3*x^2/3)
Range considerations – limited range functions are more stable, large/infinite range functions are more efficient. You may need to reduce learning rates compared to e.g. tanh.
Monotonic – check.
Monotonic derivative - no.
Approximates identity near the origin – no, the approximation is bad near the origin.

If you look through the list of current, successful activation functions, you will see a few that also fail to provide one or more desirable traits, yet are still used routinely.

I would worry about the high gradients near x=0, but other than that I think the function could work ok. It may sometimes be unstable during learning, as small changes near zero will result in large changes to output. You might be able to work around the high gradients simply in practice, by clipping them. If the raw calculation returns value greater than 1 (or less than −1) then treat the gradient as if it were 1 (or −1) for the rest of backpropagation.

The only way of finding out if the function is competitive with other more standard activation functions is to try it on some standard data sets and make comparisons.

https://en.wikipedia.org/wiki/Activation_function#Comparison_of_activation_functions
https://ai.stackexchange.com/questions/8181/is-the-cube-root-function-suitable-as-a-n-activation-function


#### How to Escape Saddle Points Efficiently
https://bair.berkeley.edu/blog/2017/08/31/saddle-efficiency/
https://stats.stackexchange.com/questions/278104/how-can-it-be-trapped-in-a-saddle-point


#### Coding Neural Network - Forward Propagation and Backpropagtion
https://imaddabbura.github.io/post/coding_neural_network_fwd_bckwd_prop/

#### Coding Neural Network — Forward Propagation and Backpropagtion
https://towardsdatascience.com/coding-neural-network-forward-propagation-and-backpropagtion-ccf8cf369f76


#### A Beginner's Guide to Neural Networks and Deep Learning
https://skymind.ai/wiki/neural-network

#### Hacker's guide to Neural Networks
http://karpathy.github.io/neuralnets/

### 45 Questions to test a data scientist on basics of Deep Learning (along with solution)
https://www.analyticsvidhya.com/blog/2017/01/must-know-questions-deep-learning/
