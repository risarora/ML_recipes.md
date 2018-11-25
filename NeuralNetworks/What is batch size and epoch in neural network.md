What is batch size and epoch in neural network?
## NEURAL NETWORK
Batch size defines number of samples that going to be propagated through the network.For instance, let’s say you have 1050 training samples and you want to set up batch_size equal to 100. Algorithm takes first 100 samples (from 1st to 100th) from the training dataset and trains network. Next it takes second 100 samples (from 101st to 200th) and train network again. We can keep doing this procedure until we will propagate through the networks all samples. The problem usually happens with the last set of samples. In our example we’ve used 1050 which is not divisible by 100 without remainder. The simplest solution is just to get final 50 samples and train the network.

* Advantages:

It requires less memory. Since you train network using less number of samples the overall training procedure requires less memory. It’s especially important in case if you are not able to fit dataset in memory.

Typically networks trains faster with mini-batches. That’s because we update weights after each propagation. In our example we’ve propagated 11 batches (10 of them had 100 samples and 1 had 50 samples) and after each of them we’ve updated network’s parameters. If we used all samples during propagation we would make only 1 update for the network’s parameter.

* Disadvantages:

The smaller the batch the less accurate estimate of the gradient. In the figure below you can see that mini-batch (green color) gradient’s direction fluctuates compare to the full batch (blue color).

enter image description here

Stochastic is just a mini-batch with batch_size equal to 1. Gradient changes its direction even more often than a mini-batch.

 

In the neural network terminology:

one epoch = one forward pass and one backward pass of all the training examples
batch size = the number of training examples in one forward/backward pass. The higher the batch size, the more memory space you’ll need.
number of iterations = number of passes, each pass using [batch size] number of examples. To be clear, one pass = one forward pass + one backward pass (we do not count the forward pass and backward pass as two different passes).
Example: if you have 1000 training examples, and your batch size is 500, then it will take 2 iterations to complete 1 epoch.

FYI: Tradeoff batch size vs. number of iterations to train a neural network

 

 

Epoch and Iteration describe slightly different things.

As others have already mentioned, an “epoch” describes the number of times the algorithm sees the ENTIRE data set. So each time the algorithm has seen all samples in the dataset, an epoch has completed.

An “iteration” describes the number of times a “batch” of data passed through the algorithm. In the case of neural networks, that means the “forwarwd pass” and “backward pass”. So every time you pass a batch of data through the NN, you completed an “iteration”

An example might make it clearer:

Say you have a dataset of 10 examples/samples. You have batch size of 2, and you’ve specified you want the algorithm to run for 3 epochs.

Therefore, in each epoch, you have 5 batches (10/2 = 5). Each batch gets passed through the algorithm, therefore you have 5 iterations per epoch. Since you’ve specified 3 epochs, you have a total of 15 iterations (5*3 = 15) for training.

 

Source – https://stats.stackexchange.com/questions/153531/what-is-batch-size-in-neural-network

https://stackoverflow.com/questions/4752626/epoch-vs-iteration-when-training-neural-networks

