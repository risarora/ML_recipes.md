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


#############################################################

The (Not so) Secrete Sauce

* Luck
* Discipline
* Proper validation framework
* Effort
* Domain knowledge + Feature engineering
* The “right” model structure
* Familiarity with many machine learning tools/packages
* Coding/data manipulation efficiency

The ToolBox
Data Manipulation
* Python
Modeling tools
* Gradient Boosting Machine (xgboost recommended)
* Neural Networks (esp. for multiclass classification problems)
* CNN a must for image recognition
* Regularized regression / SGD
* Factorization machine
* SVM
* Random Forest, ExtraTrees, etc.
* Ensemble / Stacking


## Amazon User Access
### Intro

* One of the most popular competitions on Kaggle to date with 1687 teams
* Use anonymized features to predict if employee access request would be granted or denied
* All categorical features ○ Resource ID / Mgr ID / User ID / Dept ID … ○ Many features have high cardinality
* A recurring feature engineering challenge – how to convert categorical features into numerical, so that they can be fed into GBM

### Summary

* Encode categorical features using observation counts
  * This is even available for test data!
* Encode categorical features using average response

* Build different kind of trees + ENET
  * GBM + ERT + ENET + RF + GBM2 + ERT2
  * I didn't know VW (or similar), otherwise might have got better results.
* Code available https://github.com/owenzhang/Kaggle-AmazonChallenge2013

### Response Encoding

* Every level of a categorical feature is represented by the average value of the response variable in that level in the training data
* However this leads to severe overfitting when the # of rows in each level is low
  * Double dipping the response
* Take the following steps to control overfitting:
  * For training data
    * Use the average response of all the other rows in each level, except for the current row
    * Shrink the row avg(response) toward global mean, based on # of rows in that average
    * Apply a small random multiplying factor in (.95, 1/.95) to avoid concentration of frequent values
  * For test data
  * Still apply shrinkage, but not leave-self-out or randomization



## Allstate User Purchase Option Prediction
### Intro
* Predict final purchased product (insurance policy) options based on earlier transactions.
* 7 correlated targets, each has 2-4 levels
* This turns out to be very difficult because:
  * The evaluation criteria is all-or-nothing: all 7 predictions need to be correct
  * The baseline “last quoted” is very hard to beat.
    * Last quoted 53.269%
    * #3 (me) :  53.713% (+0.44%)
    * #1 solution 53.743% (+0.47%)
* Key challenges -- capture correlation, and not to lose to baseline

### Summary

* Dependency -- Chained models ○ First build stand-alone model for F ○ Then model for G, given F
  * ○ F => G => B => A => C => E => D
  * “Free models” first, “dependent” model later
  * In training time, use actual data
  * In prediction time, use most likely predicted value

* Not to lose to baseline -- 2 stage models
  * Build one more model to predict which one to use: chained prediction, or baseline

## Liberty Mutual Fire Loss Prediction
20
3. Liberty Mutual Fire Loss -- Feature Engineering
21
3. Liberty Mutual Fire Loss – Model Structure
22
4. Avito Context Ads Click Through Rate Prediction
23

* Big Data?
* 112159462 rows
* 392346948 rows

* It is all relative

* All data processing done in R on a single 16core/256GB machine
4. Avito Summary

* This comp has fairly large data and nontrivial structure. I spent about ⅔ of time doing feature engineering and ⅓ training models.
* It is interesting that pure xgboost models performed so well that I never had the need to build other models to add to the ensemble.
* The structure of the data provide interesting feature engineering opportunities.
* The data are large enough that there is virtually no risk of overfitting public LB.
* Code available https://github.com/owenzhang/kaggle-avito
24
4. Avito Features

* raw features, such as Position, HistCTR,
* simple time based features, such as time of day and day of the week
* sequence based features, such as # of ads seen up to a given impression
* average prior response, such as # of ads clicked up to a given impression
* text based features, using ngram/tfidf/svd, such as SearchQuery
* text similarity, for example, similarity between SearchQuery and Title
* simple text stats, such as # of characters in Title
* price based features, such as average price for given category views of a given user
* entropy based features how diverse/concentrated a user’s history is
* categorical features that are encoded with click rate, adjusted for credibility
25
Bane of DS Competitions – Data Leakage

* It is extremely difficult to set up a “smart data scientist proof” DS competition
* Many kind of leaks can ruin a dataset:
* Sequential ID/rows that are highly correlated with target
* Name, timestamp, or other attributes of data files
* Data elements that are dependent on the target variable
* In actual practice, we must be vigilant against data leaks
* Watch out for models that are “too good to be true”
* Some leaks can be quite subtle
* A good rule – never use data elements that don’t exist at prediction time
26
DS Competitions vs the Real World

* Implementation is a curial component in reality
* Time to market and run-time performance are important
* A fast to implement 80% solution may outperform a hard-to-implement 95% solution, especially in a fast moving environment
* Complex models carry higher cost in both maintenance and interpretation
* Generally speaking, complex models are less robust against “unknown unknown”
27
Practical Lessons Learned from Kaggle

* A group of highly competitive experts can quickly create models that out perform existing baseline (very often created by competent internal team), even with little domain knowledge and anonymized data
* Winning models, however, are usually NOT good candidates for direct production use, because
* They are far too complex, often hard or impossible to implement and interpret
* Very often a significant gain of prediction accuracy comes from data leakage, not real signal – there is no LB to game in the real world
28
Then What Good can Come from DS Comps?
Plenty:
* Identify potential data issues / leakage
* Provide benchmark of “upper end” of predictability
* Provide ideas for feature engineering for the production model
* Screen all possible modeling approaches and find the most promising ones
* Recruit talent
* Good test of practical technical capability
* Also shows that the sponsor is cool



Source : OwenZhang0210-Cutting Edge Data Science
