
<a href="https://cognitiveclass.ai"><img src = "https://ibm.box.com/shared/static/9gegpsmnsoo25ikkbl4qzlvlyjbgxs5x.png" width = 400> </a>

<h1 align=center><font size = 5>Regression Models with Keras</font></h1>

## Introduction

As we discussed in the videos, despite the popularity of more powerful libraries such as PyToch and TensorFlow, they are not easy to use and have a steep learning curve. So, for people who are just starting to learn deep learning, there is no better library to use other than the keras library. 

Keras is a high-level API for building deep learning models. It has gained favor for its ease of use and syntactic simplicity facilitating fast development. As you will see in this lab and the other labs in this course, building a very complex deep learning network can be achieved with Keras with only few lines of code. You will appreciate Keras even more, once you learn how to build deep models using PyTorch and TensorFlow in the other courses.

So, in this lab, you will learn how to use the Keras library to build a regression model.

## Table of Contents

<div class="alert alert-block alert-info" style="margin-top: 20px">

<font size = 3> 
1. <a href="#item1">Download and Clean Dataset</a>  
2. <a href="#item2">Import Keras</a>  
3. <a href="#item3">Build a Neural Network</a>  
4. <a href="#item4">Train and Test the Network</a>  
</font>
</div>

<a id="item1"></a>

## Download and Clean Dataset

Let's start by importing the <em>pandas</em> and the Numpy libraries.


```python
import pandas as pd
import numpy as np
```

We will be playing around with the same dataset that we used in the videos.

<strong>The dataset is about the compressive strength of different samples of concrete based on the volumes of the different materials that were used to make them. Ingredients include:</strong>

<strong>1. Cement</strong>

<strong>2. Blast Furnace Slag</strong>

<strong>3. Fly Ash</strong>

<strong>4. Water</strong>

<strong>5. Superplasticizer</strong>

<strong>6. Coarse Aggregate</strong>

<strong>7. Fine Aggregate</strong>

Let's download the data and read it into a <em>pandas</em> dataframe.


```python
concrete_data = pd.read_csv('https://ibm.box.com/shared/static/svl8tu7cmod6tizo6rk0ke4sbuhtpdfx.csv')
concrete_data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cement</th>
      <th>Blast Furnace Slag</th>
      <th>Fly Ash</th>
      <th>Water</th>
      <th>Superplasticizer</th>
      <th>Coarse Aggregate</th>
      <th>Fine Aggregate</th>
      <th>Age</th>
      <th>Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>540.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>162.0</td>
      <td>2.5</td>
      <td>1040.0</td>
      <td>676.0</td>
      <td>28</td>
      <td>79.99</td>
    </tr>
    <tr>
      <th>1</th>
      <td>540.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>162.0</td>
      <td>2.5</td>
      <td>1055.0</td>
      <td>676.0</td>
      <td>28</td>
      <td>61.89</td>
    </tr>
    <tr>
      <th>2</th>
      <td>332.5</td>
      <td>142.5</td>
      <td>0.0</td>
      <td>228.0</td>
      <td>0.0</td>
      <td>932.0</td>
      <td>594.0</td>
      <td>270</td>
      <td>40.27</td>
    </tr>
    <tr>
      <th>3</th>
      <td>332.5</td>
      <td>142.5</td>
      <td>0.0</td>
      <td>228.0</td>
      <td>0.0</td>
      <td>932.0</td>
      <td>594.0</td>
      <td>365</td>
      <td>41.05</td>
    </tr>
    <tr>
      <th>4</th>
      <td>198.6</td>
      <td>132.4</td>
      <td>0.0</td>
      <td>192.0</td>
      <td>0.0</td>
      <td>978.4</td>
      <td>825.5</td>
      <td>360</td>
      <td>44.30</td>
    </tr>
  </tbody>
</table>
</div>



So the first concrete sample has 540 cubic meter of cement, 0 cubic meter of blast furnace slag, 0 cubic meter of fly ash, 162 cubic meter of water, 2.5 cubic meter of superplaticizer, 1040 cubic meter of coarse aggregate, 676 cubic meter of fine aggregate. Such a concrete mix which is 28 days old, has a compressive strength of 79.99 MPa. 

#### Let's check how many data points we have.


```python
concrete_data.shape
```




    (1030, 9)



So, there are approximately 1000 samples to train our model on. Because of the few samples, we have to be careful not to overfit the training data.

Let's check the dataset for any missing values.


```python
concrete_data.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cement</th>
      <th>Blast Furnace Slag</th>
      <th>Fly Ash</th>
      <th>Water</th>
      <th>Superplasticizer</th>
      <th>Coarse Aggregate</th>
      <th>Fine Aggregate</th>
      <th>Age</th>
      <th>Strength</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>1030.000000</td>
      <td>1030.000000</td>
      <td>1030.000000</td>
      <td>1030.000000</td>
      <td>1030.000000</td>
      <td>1030.000000</td>
      <td>1030.000000</td>
      <td>1030.000000</td>
      <td>1030.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>281.167864</td>
      <td>73.895825</td>
      <td>54.188350</td>
      <td>181.567282</td>
      <td>6.204660</td>
      <td>972.918932</td>
      <td>773.580485</td>
      <td>45.662136</td>
      <td>35.817961</td>
    </tr>
    <tr>
      <th>std</th>
      <td>104.506364</td>
      <td>86.279342</td>
      <td>63.997004</td>
      <td>21.354219</td>
      <td>5.973841</td>
      <td>77.753954</td>
      <td>80.175980</td>
      <td>63.169912</td>
      <td>16.705742</td>
    </tr>
    <tr>
      <th>min</th>
      <td>102.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>121.800000</td>
      <td>0.000000</td>
      <td>801.000000</td>
      <td>594.000000</td>
      <td>1.000000</td>
      <td>2.330000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>192.375000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>164.900000</td>
      <td>0.000000</td>
      <td>932.000000</td>
      <td>730.950000</td>
      <td>7.000000</td>
      <td>23.710000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>272.900000</td>
      <td>22.000000</td>
      <td>0.000000</td>
      <td>185.000000</td>
      <td>6.400000</td>
      <td>968.000000</td>
      <td>779.500000</td>
      <td>28.000000</td>
      <td>34.445000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>350.000000</td>
      <td>142.950000</td>
      <td>118.300000</td>
      <td>192.000000</td>
      <td>10.200000</td>
      <td>1029.400000</td>
      <td>824.000000</td>
      <td>56.000000</td>
      <td>46.135000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>540.000000</td>
      <td>359.400000</td>
      <td>200.100000</td>
      <td>247.000000</td>
      <td>32.200000</td>
      <td>1145.000000</td>
      <td>992.600000</td>
      <td>365.000000</td>
      <td>82.600000</td>
    </tr>
  </tbody>
</table>
</div>




```python
concrete_data.isnull().sum()
```




    Cement                0
    Blast Furnace Slag    0
    Fly Ash               0
    Water                 0
    Superplasticizer      0
    Coarse Aggregate      0
    Fine Aggregate        0
    Age                   0
    Strength              0
    dtype: int64



The data looks very clean and is ready to be used to build our model.

#### Split data into predictors and target


```python
concrete_data_columns = concrete_data.columns

predictors = concrete_data[concrete_data_columns[concrete_data_columns != 'Strength']] # all columns except Strength
target = concrete_data['Strength'] # Strength column
```

<a id="item2"></a>

Let's do a quick sanity check of the predictors and the target dataframes.


```python
predictors.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cement</th>
      <th>Blast Furnace Slag</th>
      <th>Fly Ash</th>
      <th>Water</th>
      <th>Superplasticizer</th>
      <th>Coarse Aggregate</th>
      <th>Fine Aggregate</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>540.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>162.0</td>
      <td>2.5</td>
      <td>1040.0</td>
      <td>676.0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>1</th>
      <td>540.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>162.0</td>
      <td>2.5</td>
      <td>1055.0</td>
      <td>676.0</td>
      <td>28</td>
    </tr>
    <tr>
      <th>2</th>
      <td>332.5</td>
      <td>142.5</td>
      <td>0.0</td>
      <td>228.0</td>
      <td>0.0</td>
      <td>932.0</td>
      <td>594.0</td>
      <td>270</td>
    </tr>
    <tr>
      <th>3</th>
      <td>332.5</td>
      <td>142.5</td>
      <td>0.0</td>
      <td>228.0</td>
      <td>0.0</td>
      <td>932.0</td>
      <td>594.0</td>
      <td>365</td>
    </tr>
    <tr>
      <th>4</th>
      <td>198.6</td>
      <td>132.4</td>
      <td>0.0</td>
      <td>192.0</td>
      <td>0.0</td>
      <td>978.4</td>
      <td>825.5</td>
      <td>360</td>
    </tr>
  </tbody>
</table>
</div>




```python
target.head()
```

Finally, the last step is to normalize the data by substracting the mean and dividing by the standard deviation.


```python
predictors_norm = (predictors - predictors.mean()) / predictors.std()
predictors_norm.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Cement</th>
      <th>Blast Furnace Slag</th>
      <th>Fly Ash</th>
      <th>Water</th>
      <th>Superplasticizer</th>
      <th>Coarse Aggregate</th>
      <th>Fine Aggregate</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2.476712</td>
      <td>-0.856472</td>
      <td>-0.846733</td>
      <td>-0.916319</td>
      <td>-0.620147</td>
      <td>0.862735</td>
      <td>-1.217079</td>
      <td>-0.279597</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2.476712</td>
      <td>-0.856472</td>
      <td>-0.846733</td>
      <td>-0.916319</td>
      <td>-0.620147</td>
      <td>1.055651</td>
      <td>-1.217079</td>
      <td>-0.279597</td>
    </tr>
    <tr>
      <th>2</th>
      <td>0.491187</td>
      <td>0.795140</td>
      <td>-0.846733</td>
      <td>2.174405</td>
      <td>-1.038638</td>
      <td>-0.526262</td>
      <td>-2.239829</td>
      <td>3.551340</td>
    </tr>
    <tr>
      <th>3</th>
      <td>0.491187</td>
      <td>0.795140</td>
      <td>-0.846733</td>
      <td>2.174405</td>
      <td>-1.038638</td>
      <td>-0.526262</td>
      <td>-2.239829</td>
      <td>5.055221</td>
    </tr>
    <tr>
      <th>4</th>
      <td>-0.790075</td>
      <td>0.678079</td>
      <td>-0.846733</td>
      <td>0.488555</td>
      <td>-1.038638</td>
      <td>0.070492</td>
      <td>0.647569</td>
      <td>4.976069</td>
    </tr>
  </tbody>
</table>
</div>




```python
n_cols = predictors_norm.shape[1] # number of predictors
```

<a id="item1"></a>

## Import Keras

Recall from the videos that Keras normally runs on top of a low-level library such as TensorFlow. This means that to be able to use the Keras library, you will have to install TensorFlow first and when you import the Keras library, it will be explicitly displayed what backend was used to install the Keras library. In CC Labs, we used TensorFlow as the backend to install Keras, so it should clearly print that when we import Keras.

#### Let's go ahead and import the Keras library


```python
import keras
```

    Using TensorFlow backend.


As you can see, the TensorFlow backend was used to install the Keras library.

Let's import the rest of the packages from the Keras library that we will need to build our regressoin model.


```python
from keras.models import Sequential
from keras.layers import Dense
```

## Build a Neural Network

Let's define a function that defines our regression model for us so that we can conveniently call it to create our model.


```python
# define regression model
def regression_model():
    # create model
    model = Sequential()
    model.add(Dense(50, activation='relu', input_shape=(n_cols,)))
    model.add(Dense(50, activation='relu'))
    model.add(Dense(1))
    
    # compile model
    model.compile(optimizer='adam', loss='mean_squared_error')
    return model
```

<a id="item4"></a>

## Train and Test the Network


```python
# build the model
model = regression_model()

# fit the model
model.fit(predictors_norm, target, validation_split=0.3, epochs=100, verbose=2)
```

    Train on 721 samples, validate on 309 samples
    Epoch 1/100
     - 0s - loss: 1668.0867 - val_loss: 1159.0696
    Epoch 2/100
     - 0s - loss: 1555.1509 - val_loss: 1048.1265
    Epoch 3/100
     - 0s - loss: 1371.6259 - val_loss: 878.7858
    Epoch 4/100
     - 0s - loss: 1092.3431 - val_loss: 647.2639
    Epoch 5/100
     - 0s - loss: 734.2938 - val_loss: 396.3186
    Epoch 6/100
     - 0s - loss: 424.3245 - val_loss: 218.8226
    Epoch 7/100
     - 0s - loss: 278.6959 - val_loss: 166.2804
    Epoch 8/100
     - 0s - loss: 242.9704 - val_loss: 162.4391
    Epoch 9/100
     - 0s - loss: 228.1289 - val_loss: 158.7672
    Epoch 10/100
     - 0s - loss: 214.9327 - val_loss: 161.4950
    Epoch 11/100
     - 0s - loss: 206.4547 - val_loss: 156.7180
    Epoch 12/100
     - 0s - loss: 197.9466 - val_loss: 152.8896
    Epoch 13/100
     - 0s - loss: 191.2017 - val_loss: 149.3376
    Epoch 14/100
     - 0s - loss: 185.6181 - val_loss: 147.7438
    Epoch 15/100
     - 0s - loss: 181.1299 - val_loss: 145.9771
    Epoch 16/100
     - 0s - loss: 176.7143 - val_loss: 142.8426
    Epoch 17/100
     - 0s - loss: 173.5258 - val_loss: 141.4312
    Epoch 18/100
     - 0s - loss: 169.8020 - val_loss: 140.8451
    Epoch 19/100
     - 0s - loss: 166.8531 - val_loss: 139.3640
    Epoch 20/100
     - 0s - loss: 164.0962 - val_loss: 138.8215
    Epoch 21/100
     - 0s - loss: 161.9370 - val_loss: 137.1125
    Epoch 22/100
     - 0s - loss: 159.2270 - val_loss: 135.9488
    Epoch 23/100
     - 0s - loss: 158.0600 - val_loss: 138.2760
    Epoch 24/100
     - 0s - loss: 155.6476 - val_loss: 136.2907
    Epoch 25/100
     - 0s - loss: 153.7434 - val_loss: 136.9958
    Epoch 26/100
     - 0s - loss: 151.5600 - val_loss: 136.5463
    Epoch 27/100
     - 0s - loss: 150.2445 - val_loss: 136.2792
    Epoch 28/100
     - 0s - loss: 148.2961 - val_loss: 137.6153
    Epoch 29/100
     - 0s - loss: 147.7016 - val_loss: 136.6190
    Epoch 30/100
     - 0s - loss: 145.7121 - val_loss: 134.9710
    Epoch 31/100
     - 0s - loss: 144.1296 - val_loss: 137.3133
    Epoch 32/100
     - 0s - loss: 143.0230 - val_loss: 139.4884
    Epoch 33/100
     - 0s - loss: 141.4476 - val_loss: 137.4651
    Epoch 34/100
     - 0s - loss: 140.8038 - val_loss: 138.7442
    Epoch 35/100
     - 0s - loss: 139.1329 - val_loss: 138.5511
    Epoch 36/100
     - 0s - loss: 138.9991 - val_loss: 139.1242
    Epoch 37/100
     - 0s - loss: 137.3805 - val_loss: 139.2027
    Epoch 38/100
     - 0s - loss: 135.8545 - val_loss: 138.5945
    Epoch 39/100
     - 0s - loss: 134.6725 - val_loss: 140.7328
    Epoch 40/100
     - 0s - loss: 133.6757 - val_loss: 140.9090
    Epoch 41/100
     - 0s - loss: 132.7791 - val_loss: 138.6245
    Epoch 42/100
     - 0s - loss: 131.6085 - val_loss: 139.9095
    Epoch 43/100
     - 0s - loss: 130.4505 - val_loss: 139.9367
    Epoch 44/100
     - 0s - loss: 130.1310 - val_loss: 141.8153
    Epoch 45/100
     - 0s - loss: 128.4616 - val_loss: 139.9030
    Epoch 46/100
     - 0s - loss: 127.5130 - val_loss: 141.8059
    Epoch 47/100
     - 0s - loss: 126.8767 - val_loss: 139.0099
    Epoch 48/100
     - 0s - loss: 125.4185 - val_loss: 140.2470
    Epoch 49/100
     - 0s - loss: 124.6095 - val_loss: 141.4137
    Epoch 50/100
     - 0s - loss: 123.6110 - val_loss: 140.3835
    Epoch 51/100
     - 0s - loss: 122.3340 - val_loss: 139.3326
    Epoch 52/100
     - 0s - loss: 121.4310 - val_loss: 141.2979
    Epoch 53/100
     - 0s - loss: 120.7683 - val_loss: 138.6142
    Epoch 54/100
     - 0s - loss: 120.2955 - val_loss: 139.2421
    Epoch 55/100
     - 0s - loss: 118.7538 - val_loss: 138.7694
    Epoch 56/100
     - 0s - loss: 116.7642 - val_loss: 139.3208
    Epoch 57/100
     - 0s - loss: 116.1116 - val_loss: 135.7481
    Epoch 58/100
     - 0s - loss: 114.1143 - val_loss: 137.8700
    Epoch 59/100
     - 0s - loss: 113.1653 - val_loss: 137.9940
    Epoch 60/100
     - 0s - loss: 111.7290 - val_loss: 134.9991
    Epoch 61/100
     - 0s - loss: 110.1913 - val_loss: 135.1240
    Epoch 62/100
     - 0s - loss: 108.4302 - val_loss: 133.2318
    Epoch 63/100
     - 0s - loss: 106.8922 - val_loss: 135.8674
    Epoch 64/100
     - 0s - loss: 105.1045 - val_loss: 135.2025
    Epoch 65/100
     - 0s - loss: 103.1828 - val_loss: 132.2417
    Epoch 66/100
     - 0s - loss: 102.5104 - val_loss: 131.5124
    Epoch 67/100
     - 0s - loss: 99.4331 - val_loss: 129.9964
    Epoch 68/100
     - 0s - loss: 97.6290 - val_loss: 129.8510
    Epoch 69/100
     - 0s - loss: 94.9035 - val_loss: 126.8755
    Epoch 70/100
     - 0s - loss: 92.6281 - val_loss: 126.0648
    Epoch 71/100
     - 0s - loss: 89.6003 - val_loss: 122.8450
    Epoch 72/100
     - 0s - loss: 87.7818 - val_loss: 125.9121
    Epoch 73/100
     - 0s - loss: 85.2236 - val_loss: 120.9672
    Epoch 74/100
     - 0s - loss: 81.4547 - val_loss: 119.8860
    Epoch 75/100
     - 0s - loss: 79.1539 - val_loss: 117.2428
    Epoch 76/100
     - 0s - loss: 76.5552 - val_loss: 118.0591
    Epoch 77/100
     - 0s - loss: 74.4755 - val_loss: 116.5348
    Epoch 78/100
     - 0s - loss: 73.4357 - val_loss: 121.4253
    Epoch 79/100
     - 0s - loss: 70.8813 - val_loss: 112.2689
    Epoch 80/100
     - 0s - loss: 69.2171 - val_loss: 114.9091
    Epoch 81/100
     - 0s - loss: 66.5939 - val_loss: 114.5285
    Epoch 82/100
     - 0s - loss: 65.4645 - val_loss: 108.7609
    Epoch 83/100
     - 0s - loss: 63.2388 - val_loss: 110.0646
    Epoch 84/100
     - 0s - loss: 61.6493 - val_loss: 117.0202
    Epoch 85/100
     - 0s - loss: 60.4708 - val_loss: 101.3180
    Epoch 86/100
     - 0s - loss: 60.2505 - val_loss: 110.0509
    Epoch 87/100
     - 0s - loss: 58.3921 - val_loss: 103.8122
    Epoch 88/100
     - 0s - loss: 57.4460 - val_loss: 102.8007
    Epoch 89/100
     - 0s - loss: 56.4559 - val_loss: 106.9205
    Epoch 90/100
     - 0s - loss: 54.7322 - val_loss: 106.2429
    Epoch 91/100
     - 0s - loss: 53.6166 - val_loss: 103.6098
    Epoch 92/100
     - 0s - loss: 52.5585 - val_loss: 108.5131
    Epoch 93/100
     - 0s - loss: 51.7297 - val_loss: 105.5168
    Epoch 94/100
     - 0s - loss: 51.3630 - val_loss: 101.9567
    Epoch 95/100
     - 0s - loss: 49.5500 - val_loss: 111.5102
    Epoch 96/100
     - 0s - loss: 49.1530 - val_loss: 102.8371
    Epoch 97/100
     - 0s - loss: 48.2750 - val_loss: 103.8946
    Epoch 98/100
     - 0s - loss: 47.8825 - val_loss: 112.9797
    Epoch 99/100
     - 0s - loss: 47.8847 - val_loss: 101.5104
    Epoch 100/100
     - 0s - loss: 45.7881 - val_loss: 110.7909





    <keras.callbacks.History at 0x7f88e7a7dda0>



<strong>You can refer to this [link](https://keras.io/models/sequential/) to learn about other functions that you can use for prediction or evaluation.</strong>

Feel free to vary the following and note what impact each change has on the model's performance:

1. Increase or decreate number of neurons in hidden layers
2. Add more hidden layers
3. Increase number of epochs

### Thank you for completing this lab!

This notebook was created by [Alex Aklson](https://www.linkedin.com/in/aklson/). I hope you found this lab interesting and educational. Feel free to contact me if you have any questions!

This notebook is part of a course on **edX** called *Deep Learning Fundamentals with Keras*. If you accessed this notebook outside the course, you can take this course online by clicking [here](http://cocl.us/DL0101EN_edX_Week3_LAB1).

<hr>

Copyright &copy; 2018 [IBM Developer Skills Network](https://cognitiveclass.ai/?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
