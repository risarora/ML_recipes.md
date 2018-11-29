## Class Imbalance
#### Binary-class Classification

* Typical methods for imbalance data in 2-class classification:
* Oversampling: re-sampling of data from positive class
* Under-sampling: randomly eliminate tuples from
negative class
* Penalize: penalize the algorithm more when it makes a
mistake on the minority class
* Still difficult for class imbalance problem on multiclass tasks

###### SMOTE: Synthetic Minority
* Oversampling Technique
* Key idea: Oversample minority class by generating synthetic data points
  * Step 1: Find k nearest neighbors of training examples of minority class
  * Step 2: Generate synthetic data points along the lines that connect those neighbors (with some random noise)
* Chawla et al. “SMOTE: Synthetic Minority Oversampling Technique”, JAIRC 2002


#### Multi-class Classification
* Popular methods use binary classifiers as basis

* Method 1. One-vs.-all (OVA): Learn a classifier one at a time
  * Given m classes, train m classifiers: one for each class
  * Classifier j: treat tuples in class j as positive & all others as negative
  * To classify a tuple X, the set of classifiers vote as an ensemble

* Method 2. All-vs.-all (AVA): Learn a classifier for each pair of classes
  * Given m classes, construct m(m-1)/2 binary classifiers
  * A classifier is trained using tuples of the two classes
  * To classify a tuple X, each classifier votes. X is assigned to the class with maximal vote

* Comparison
* All-vs.-all tends to be more robust than one-vs.-all


[source](http://www.cs.ucr.edu/~epapalex/teaching/171_S18/slides/05d-classification-advanced.pdf.html)

## Active Learning
1. Unlabeled points
2. Supervised learning
3. Semisupervised and active learning

### Class labels are expensive to obtain
* Solution: query human (oracle) for labels
* Pool-based approach: Uses a pool of unlabeled data
* L: a small subset of D is labeled, U: a pool of unlabeled data in D
* Use a query function to carefully select one or more tuples from U and request
labels from an oracle (a human annotator)
* The newly labeled samples are added to L, and learn a model
* Goal: Achieve high accuracy using as few labeled data as possible
* Evaluated using learning curves: Accuracy as a function of the number of
instances queried (# of tuples to be queried should be small)

* Active Learning
  * Typical heuristic algorithm:
  * Start with pool of unlabeled data
  * Pick few points at random and label them
  * Fit a classifier to the labeled data
  * Query the data point closest to the boundary

[source](http://hunch.net/~active_learning/)
