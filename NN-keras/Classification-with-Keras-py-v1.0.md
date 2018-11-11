
<a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/9gegpsmnsoo25ikkbl4qzlvlyjbgxs5x.png" width = 400> </a>

<h1 align=center><font size = 5>Classification Models with Keras</font></h1>

## Introduction

In this lab, we will learn how to use the Keras library to build models for classificaiton problems. We will use the popular MNIST dataset, a dataset of images, for a change. 

The <strong>MNIST database</strong>, short for Modified National Institute of Standards and Technology database, is a large database of handwritten digits that is commonly used for training various image processing systems.he database is also widely used for training and testing in the field of machine learning.
    
The MNIST database contains 60,000 training images and 10,000 testing images of digits written by high school students and employees of the United States Census Bureau.

Also, this way, will get to compare how conventional neural networks compare to convolutional neural networks, that we will build in the next module.

## Table of Contents

<div class="alert alert-block alert-info" style="margin-top: 20px">

<font size = 3>

1. <a href="#item2">Import Keras and Packages</a>      
2. <a href="#item3">Build a Neural Network</a>     
3. <a href="#item4">Train and Test the Network</a>     
</font>
</div>

## Import Keras and Packages


```python
import keras

from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
```

    Using TensorFlow backend.


Since we are dealing we images, let's also import the Matplotlib scripting layer in order to view the images.


```python
import matplotlib.pyplot as plt
```

The Keras library conveniently includes the MNIST dataset as part of its API. You can check other datasets within the Keras library [here](https://keras.io/datasets/). 

So, let's load the MNIST dataset from the Keras library. The dataset is readily divided into a training set and a test set.


```python
# import the data
from keras.datasets import mnist

# read the data
(X_train, y_train), (X_test, y_test) = mnist.load_data()
```

    Downloading data from https://s3.amazonaws.com/img-datasets/mnist.npz
    11493376/11490434 [==============================] - 0s 0us/step


Let's confirm the number of images in each set. According to the dataset's documentation, we should have 60000 images in X_train and 10000 images in the X_test.


```python
X_train.shape
```




    (60000, 28, 28)



The first number in the output tuple is the number of images, and the other two numbers are the size of the images in datset. So, each image is 28 pixels by 28 pixels.

Let's visualize the first image in the training set using Matplotlib's scripting layer.


```python
plt.imshow(X_train[0])
```




    <matplotlib.image.AxesImage at 0x7f3f0c0799b0>




![png](output_14_1.png)


With conventional neural networks, we cannot feed in the image as input as is. So we need to flatten the images into one-dimensional vectors, each of size 1 x (28 x 28) = 1 x 784.


```python
# flatten images into one-dimensional vector

num_pixels = X_train.shape[1] * X_train.shape[2] # find size of one-dimensional vector

X_train = X_train.reshape(X_train.shape[0], num_pixels).astype('float32') # flatten training images
X_test = X_test.reshape(X_test.shape[0], num_pixels).astype('float32') # flatten test images
```

Since pixel values can range from 0 to 255, let's normalize the vectors to be between 0 and 1.


```python
# normalize inputs from 0-255 to 0-1
X_train = X_train / 255
X_test = X_test / 255
```

Finally, before we start building our model, remember that for classification we need to divide our target variable into categories. We use the to_categorical function from the Keras Utilities package.


```python
# one hot encode outputs
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

num_classes = y_test.shape[1]
print(num_classes)
```

    10


## Build a Neural Network


```python
# define classification model
def classification_model():
    # create model
    model = Sequential()
    model.add(Dense(num_pixels, activation='relu', input_shape=(num_pixels,)))
    model.add(Dense(100, activation='relu'))
    model.add(Dense(num_classes, activation='softmax'))
    
    
    # compile model
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
    return model
```

## Train and Test the Network


```python
# build the model
model = classification_model()

# fit the model
model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=10, verbose=2)

# evaluate the model
scores = model.evaluate(X_test, y_test, verbose=0)
```

    Train on 60000 samples, validate on 10000 samples
    Epoch 1/10
     - 31s - loss: 0.1864 - acc: 0.9433 - val_loss: 0.0997 - val_acc: 0.9680
    Epoch 2/10
     - 30s - loss: 0.0774 - acc: 0.9756 - val_loss: 0.0756 - val_acc: 0.9776
    Epoch 3/10
     - 30s - loss: 0.0543 - acc: 0.9831 - val_loss: 0.0600 - val_acc: 0.9810
    Epoch 4/10
     - 31s - loss: 0.0390 - acc: 0.9876 - val_loss: 0.0733 - val_acc: 0.9777
    Epoch 5/10
     - 30s - loss: 0.0318 - acc: 0.9897 - val_loss: 0.0724 - val_acc: 0.9801
    Epoch 6/10
     - 30s - loss: 0.0273 - acc: 0.9915 - val_loss: 0.0820 - val_acc: 0.9796
    Epoch 7/10
     - 30s - loss: 0.0211 - acc: 0.9932 - val_loss: 0.0814 - val_acc: 0.9796
    Epoch 8/10
     - 31s - loss: 0.0217 - acc: 0.9930 - val_loss: 0.0751 - val_acc: 0.9818
    Epoch 9/10
     - 30s - loss: 0.0166 - acc: 0.9944 - val_loss: 0.1005 - val_acc: 0.9777
    Epoch 10/10
     - 30s - loss: 0.0144 - acc: 0.9953 - val_loss: 0.0849 - val_acc: 0.9820


Let's print the accuracy and the corresponding error.


```python
print('Accuracy: {}% \n Error: {}'.format(scores[1], 1 - scores[1]))        
```

    Accuracy: 0.982% 
     Error: 0.018000000000000016


Just running 10 epochs could actually take over 2 minutes. But enjoy the results as they are getting generated.

Sometimes, you cannot afford to retrain your model everytime you want to use it, especially if you are limited on computational resources and training your model can take a long time. Therefore, with the Keras library, you can save your model after training. To do that, we use the save method.


```python
model.save('classification_model.h5')
```

Since our model contains multidimensional arrays of data, then models are usually saved as .h5 files.

When you are ready to use your model again, you use the load_model function from <strong>keras.models</strong>.


```python
from keras.models import load_model
```


```python
pretrained_model = load_model('classification_model.h5')
```

### Thank you for completing this lab!

This notebook was created by [Alex Aklson](https://www.linkedin.com/in/aklson/). I hope you found this lab interesting and educational. Feel free to contact me if you have any questions!

This notebook is part of a course on **edX** called *Deep Learning Fundamentals with Keras*. If you accessed this notebook outside the course, you can take this course online by clicking [here](http://cocl.us/DL0101EN_edX_Week3_LAB2).

<hr>

Copyright &copy; 2018 [IBM Developer Skills Network](https://cognitiveclass.ai/?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
