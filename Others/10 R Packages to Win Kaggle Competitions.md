# 10 R Packages to Win Kaggle Competitions

Humans can help the Machine too!  But don’t oversimplify and discard any data. 
SVM and feature selection matter too!

Allow the Machine to Capture Complexity
## 1. gbm
 Use gbm.more to write your own early-stopping procedure 
Don’t be impatient. My best GBM had 24,500 trees with learning rate = 0.01!
The Machine seems much smarter than I am at capturing complexity in the data even for simple datasets!


## 2. randomForest

 Importance=True for permutation importance
Tune the sampsize parameter for faster computation and handling unbalanced classes

## 3. e1071

SVM  Use kernlab (Karatzoglou, Smola and Hornik) to get heuristic
Write own pattern search
Take Advantage of High-Cardinality Categorical or Text Data

## 4.   glmnet
L1 / Elasticnet / L2
- Try interactions of 2 or more categorical variables
- Test your code on the Kaggle: “Amazon Employ Access Challenge”

## 5.   tau
Used for automating text-mining
Key Trick:
Word n-grams and character n-grams can make a big difference
Try character n-grams. They work surprisingly well!

Make Your Code More Efficient 
## 6 Matrix
Use sparse.model.matrix for one-hot encoding

## 7. SOAR
Used to store large R objects in the cache and release memory

## 8. forEach
## 9. doMC
Use for parallel-processing to speed up computation

## 10.  data.table
Essential for doing fast data aggregation operations at scale



Always compute differences / ratios of features
This can help the Machine a lot!

Always consider discarding features that are “too good”
They can make the Machine lazy!
An example: GE Flight Quest
