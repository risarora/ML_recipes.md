## Comparison among Hyper-parameter Optimizers

parameter :-
All the values that we set constant for our neural network are called paramers for example, we train a network and then using back propagation we drive the weight matrix and bias matrix. These final-trained values are set to constant and then the model is ready for testing.

hyper-parameter :-
They both sound similar, but hyper-parameters are chosen prior to the assignment of parameter values. That means we first train our network to find out how many layers we need, how many neurons per each layer, drop out ratio, etc. Then using these optimized hyper-parameter values we train our model with back propagation for parameter setting. Now this hyper-parameter optimized model is best among its family of ensemble models.

EG.

learning rate
regularizers
strength of those regularizers
dimensionality of any hidden representations
number of decision trees (for random forest )
optimization algorithm (even could be)
Hyper-parameters selection has significant impact on model performance.
Open-source hyper-parameter optimization packages,
1) Hyperopt -

explores hyper-parameter space strategically using “tree of Parzen estimators” (bayesian approach)
2) scikit-optimize -

new package
has 3 algorithms :-
1. forest_minimize(decision tree regression search)
2. gbrt_minimize (gradient-boosted-tree regression search)
3. gp_minimize (Gaussian Process Regression Search)
Above 2 are most prominent methods.

3) Spearmint -

under active development (license does not permit for commercial usage)

4) MOE -

growing as start-up

These packages, (benefit)

1. can set up very large space of hyper-parameters to explore
2. can reduce the number of choices (heuristically made)
We compare the packages based on balance accuracy && speed. (test scores)
The above both packages are based on Sequential model-based optimization.( at start samples small number of points from full hyper-parameter space, then run evaluations based on them)
Baseline Method :-
These are the conventional optimization methods, on which we couldn’t find any improvements on qualities. Here we take 2 baseline methods to compare with our 2 packages.

Grid Search -
exhaustive search (will try every combination of each settings of hyper-parameters)
is guaranteed to find the best set of values(discrete version) in search space.
not tractable for large parameter space
2. Randomized Search -

samples from full grid search
doesn’t offer the same guarantee as grid search
extremely effective in practice

Packages -
Basis for search is “dictionary mapping parameter names to values”
we give a set of values for each key word. So this has one-to-many dictionary format.
EG . for baseline methods

param_grid = {
‘max_depth’ : [4, 8, 12],
‘learning_rate’ : [0.01, 0.3, 0.5],
‘n_estimators’ : [20, 50, 200],
‘objective’ : [‘multi:softprob’],
‘gamma’ : [0, 0.25, 0.5],
‘min_child_weight’ : [1, 3, 5],
‘subsample’ : [0.1, 0.5, 1],
‘colsample_bytree’ : [0.1, 0.5, 1]}
We provide full list of values for dict. The algorithm only search among them.
Mostly, the model expands for large dataset or architecture. So dict expands to very large list. So the algorithms have to search for each combinations including cross-combinations. So grid search is not tractable.
In Hyperopt, values are hyper-opt functions specifying distributions over parameter values.

Search is then samples the distributions over the each values.

hyperopt_grid = {
‘max_depth’ : hp.choice(‘max_depth’, range(4, 13, 1)),
‘learning_rate’ : hp.quniform(‘learning_rate’, 0.01, 0.5, 0.01),
‘n_estimators’ : hp.choice(‘n_estimators’, range(20, 205, 5)),
‘objective’ : ‘multi:softprob’,
‘gamma’ : hp.quniform(‘gamma’, 0, 0.50, 0.01),
‘min_child_weight’ : hp.quniform(‘min_child_weight’, 1, 5, 1),
‘subsample’ : hp.quniform(‘subsample’, 0.1, 1, 0.01),
‘colsample_bytree’ : hp.quniform(‘colsample_bytree’, 0.1, 1.0, 0.01)}
scikit-optimize only requires to specify the upper && lower bound for the search space.

scikit-opt wants lists of lists of values, rather than just dict.

So hard to keep track of which parameters are being specified.

The packge code handles internal conversions for dict — -> list && list — -> dict.

skopt_grid = {
‘max_depth’: (4, 12),
‘learning_rate’: (0.01, 0.5),
‘n_estimators’: (20, 200),
‘objective’ : Categorical((‘multi:softprob’,)),
‘gamma’: (0, 0.5),
‘min_child_weight’: (1, 5),
‘subsample’: (0.1, 1),
‘colsample_bytree’: (0.1, 1)}
Experimental Set-up :-
This will make max use of available data (whether its small or large)

1 ) Outer five-fold cross-validation

the full dataset is divided into five sections (folds). This creates five experimental settings, in which we train on four of the folds (merged together) and test on the fifth.

2 ) Inner five-fold cross-validation

For each experimental setting, the training set is used to find the optimal hyperparameters — for each setting of the hyperparameters, a full round of five-fold cross-validation is performed using only the training data.

3 ) hybrid

The hyperparameter setting that does best at step 2 is the basis for the model that is used for testing in the outer cross-validation.

For each (train_folds, test_fold) in the outer cross-validation:
For each setting S of the hyperparameters:
Cross-validate S on train_folds
Let S* be the setting that did best in the inner loop.
Use S* to assess on test_fold.
Here if we considered the parallelization, then the performance for each packages and baseline will be different.
We can segment and provide data sets to each algorithms for better performance.

full_experimental_run = [
(grid_search, param_grid, {}),
(random_search, param_grid, {‘sampsize’: None}),
(hyperopt_search, hyperopt_grid, {‘max_evals’: 100}),
(skopt_gp_search, skopt_grid, {‘n_calls’: 100}),
(skopt_forest_search, skopt_grid, {‘n_calls’: 100}),
(skopt_gbrt_search, skopt_grid, {‘n_calls’: 100})]
Usually, from experiments the the time taken is,(in fast measurement)
2 packages > > grid search
2 packages > random_search
Random search strongly shows the brute-force approach.
Experiment should be conducted on cases of,

Small datasets
Small features, but large observations
large features, but small observations
Large datasets
Summary :-
— No big difference between Hyperopt && scikit-opt. They consistently perform better && deliver more effective models faster && easy to use.

— But clearly better than baseline approaches.

— These baseline approaches needlessly expensive.

References :-
https://roamanalytics.com/2016/09/15/optimizing-the-hyperparameter-of-which-hyperparameter-optimizer-to-use/
http://www.cs.ubc.ca/~hutter/papers/11-LION5-SMAC.pdf
MOE — https://github.com/Yelp/MOE
https://medium.com/@ramrajchandradevan/comparison-among-hyper-parameter-optimizers-cd37483cd47