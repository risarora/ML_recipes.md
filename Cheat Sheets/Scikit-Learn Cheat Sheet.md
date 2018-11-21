## Scikit-Learn Cheat Sheet

Scikit-learn is an open source Python library that implements a range of machine learning, preprocessing, cross-validation and visualization algorithms using a unified interface.

```python
# import the libraries
from sklearn import neighbors, datasets, preprocessing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the data set
iris = datasets.load_iris()
X, y = iris.data[:, :2], iris.target

# perform the train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=33)
# pre-prcess the data
# scalar transformation
scaler = preprocessing.StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)

# Create the model object
knn = neighbors.KNeighborsClassifier(n_neighbors=5)

#fit the model
knn.fit(X_train, y_train)

#predict the value
y_pred = knn.predict(X_test)

#Evaluation matix
accuracy_score(y_test, y_pred)

```
## 1. Load the data

```
import numpy as np
X = np.random.random((10,5))
y = np.array(['M','M','F','F','M','F','M','M','F','F','F'])
X[X < 0.7] = 0
```


## 2. Preprocessing The Data
#### 2.1 Standardization
```
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler().fit(X_train)
standardized_X = scaler.transform(X_train)
standardized_X_test = scaler.transform(X_test)
```

#### 2.2 Normalization
```
from sklearn.preprocessing import Normalizer
scaler = Normalizer().fit(X_train)
normalized_X = scaler.transform(X_train)
normalized_X_test = scaler.transform(X_test)
```
#### 2.3 Binarization
```
from sklearn.preprocessing import Binarizer
binarizer = Binarizer(threshold=0.0).fit(X)
binary_X = binarizer.transform(X)
```
#### 2.4 Encoding Categorical Features
```
from sklearn.preprocessing import LabelEncoder
enc = LabelEncoder()
y = enc.fit_transform(y)
```
#### 2.5 Imputing Missing Values
```
from sklearn.preprocessing import Imputer
imp = Imputer(missing_values=0, strategy='mean', axis=0)
imp.fit_transform(X_train)
```
#### 2.6 Generating Polynomial Features
```
from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(5)
poly.fit_transform(X)
```

## 3. Training And Test Data split
```
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, random_state=0)
```

## 4. Create Model
### 4.1 Supervised Learning Estimators
##### Linear Regression
```
from sklearn.linear_model import LinearRegression
lr = LinearRegression(normalize=True)
```
##### Support Vector Machines (SVM)
```
from sklearn.svm import SVC
svc = SVC(kernel='linear')
```
##### Naive Bayes
```
from sklearn.naive_bayes import GaussianNB
gnb = GaussianNB()
```
##### KNN
```
from sklearn import neighbors
knn = neighbors.KNeighborsClassifier(n_neighbors=5)
```

### 4.2 Unsupervised Learning Estimators
##### Principal Component Analysis (PCA)
```
from sklearn.decomposition import PCA
pca = PCA(n_components=0.95)
```

##### K Means
```
from sklearn.cluster import KMeans
k_means = KMeans(n_clusters=3, random_state=0)
```

## 5. Model Fitting
#### 5.1 Supervised learning
```
lr.fit(X, y)
knn.fit(X_train, y_train)
svc.fit(X_train, y_train)
```
#### 5.2 Unsupervised Learning
```
k_means.fit(X_train)
pca_model = pca.fit_transform(X_train)      # Fit to data, then transform it
```

## 6.Prediction
#### 6.1 Supervised Estimators

```
y_pred = svc.predict(np.random.random((2,5))) # Predict labels
y_pred = lr.predict(X_test)                   # Predict labels
y_pred = knn.predict_proba(X_test)            # Estimate probability of a label #Estimate probability of a label
```
#### 6.2 Unsupervised Estimators
```
y_pred = k_means.predict(X_test)              # Predict labels in clustering algorithms
```

## 7. Model Evaluation Matrices
#### 7.1 Classification Metrics
##### Accuracy Score
```
knn.score(X_test, y_test)
from sklearn.metrics import accuracy_score    # Estimator score method metric scoring functions
accuracy_score(y_test, y_pred)
```
##### Classification Report
```
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))  # Precision, recall, f1-score and support
```
##### Confusion Matrix
```
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))
```

#### 7.2 Regression Metrics
##### Mean Absolute Error
```
from sklearn.metrics import mean_absolute_error
y_true = [3, -0.5, 2]
mean_absolute_error(y_true, y_pred)
```
##### Mean Squared Error
```
from sklearn.metrics import mean_squared_error
mean_squared_error(y_test, y_pred)
```
##### R² Score
```
from sklearn.metrics import r2_score
r2_score(y_true, y_pred)
```
#### 7.3 Clustering Metrics
##### Adjusted Rand Index
```
from sklearn.metrics import adjusted_rand_score
adjusted_rand_score(y_true, y_pred)
```
##### Homogeneity
```
from sklearn.metrics import homogeneity_score
homogeneity_score(y_true, y_pred)
```
##### V-measure
```
from sklearn.metrics import v_measure_score
metrics.v_measure_score(y_true, y_pred)
```

#### 7.4 Cross-Validation
```
from sklearn.cross_validation import cross_val_score
print(cross_val_score(knn, X_train, y_train, cv=4))
print(cross_val_score(lr, X, y, cv=2))
```

### 8. Fine Tuning the Model

##### Grid Search
```
from sklearn.grid_search import GridSearchCV
params = {"n_neighbors": np.arange(1,3),
          "metric": ["euclidean", "cityblock"]}
grid = GridSearchCV(estimator=knn,param_grid=params)
grid.fit(X_train, y_train)
print(grid.best_score_)
print(grid.best_estimator_.n_neighbors)
```

##### Randomized Parameter Optimization
```
from sklearn.grid_search import RandomizedSearchCV
params = {"n_neighbors": range(1,5),
          "weights": ["uniform", "distance"]}
rsearch = RandomizedSearchCV(estimator=knn,
                              param_distributions=params,
                              cv=4,
                              n_iter=8,
                              random_state=5)
rsearch.fit(X_train, y_train)
print(rsearch.best_score_)
```

Source : [DataCamp](DataCamp.com)
