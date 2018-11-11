### First Regression Model in keras

<img src="./fig_neural_network.png" style="width:400px;height:300px;">




##### import the packages

```python
import keras
from keras.models import Sequential # import Sequential library
from keras.models import Dense      # import Dense library to
```

##### define the input values

```python

model = Sequential()
n_cols = concrete_data.shape[1]

```

##### Create the layers


```python

model.add(Dense(5,activation='relu',input_shape=(n_cols,)))
model.add(Dense(5,activation='relu'))
model.add(Dense(1))

```

#### Compiling the model


```python

model.compile(optimizer='adam',loss='mean_squared_error')
model.fit(predictors,target)

```

```python


```
```python
predictions = model.predict(test_data)
```
