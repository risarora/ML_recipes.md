### First Classification Model in keras

<img src="./fig_neural_network.png" style="width:400px;height:300px;">




##### import the packages

```python
import keras
from keras.models import Sequential # import Sequential library
from keras.models import Dense      # import Dense library to
from keras.models import to_categorical      # import Dense library to

```

##### define the input values

```python

model = Sequential()
n_cols = car_data.shape[1]
target=to_categorical(target)

```

##### Create the layers


```python

model.add(Dense(5,activation='relu',input_shape=(n_cols,)))
model.add(Dense(5,activation='relu'))
model.add(Dense(4),activation='softmax'))

```

#### Compiling the model


```python

model.compile(optimizer='adam',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(predictors,target,epochs=10)

```

```python


```
```python
predictions = model.predict(test_data)
```
