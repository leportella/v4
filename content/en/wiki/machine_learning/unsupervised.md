---
layout: post
title: "Unsupervised"
slug: unsupervised
date: 2018-05-20T14:25:52-05:00
---

## KMeans

### Advantages

* Good when you have an idea of an ideal number of clusters
* Can scale well with lots of samples, scale medium with number of clusters

### Disadvantages

* Doesn't handle missing values very well
* Can't find clusters that aren't circular or spherical

### Choosing the value of K

For choosing the value of k cluster we can use the elbow method:

```python
from sklearn.clusters import Kmeans
from sklearn.metrics import silhouette_score

X = pd.DataFrame(...)

possible_k_values = range(2, len(X)+1, 5)

scores = []
for k in possible_k_values:
    model = Kmeans(n_clusters=k).fit(X)
    prediction = model.predict(X)
    score = silhouette_score(X, predictions)
    scores.append((k, score))
```

Then find the best numbers of clusters by choosing a k that has a lower 
score of errors but can still be good enough for your problem.

## Hierarchical Clustering

### Advantages

* Resulting hierarchical representation can be very informative
* Provides an additional ability to visualize 
* Especially potent when the dataset contains real hierarchical relationship (e.g. Evolutionary biology)

### Disadvantages

* Sensitive to noise and outliers
* Computationally intensive O(N^2)

### Implementation on Sklearn

```python
from sklearn import cluster

X = pd.DataFrame(...)

cls = cluster.AgglomerativeClustering(n_clusters=3, linkage='ward')
labels = cls.predict(X)
``` 

### Get a dendrogram from a hierarchical clustering

```python
from scipy.cluster.hierarchy import dendogram, ward
import matplotlib.pyplot as plt

X = pd.DataFrame(...)
linkage_matrix = ward(X)

dendogram(linkage_matrix)
plt.show()

```

## DBSCAN

### Advantages:

* We don't need to specify the number of clusters
* Flexibility in shapes and sizes of clusters
* Able to deal with noise and outliers

### Disadvantages

* Border points that are reachable from two clusters is assigned to the cluster that finds it first
* Faces difficulty finding clusters of varying densities

### Tips:

* Small min samples and small episilon results in many small clusters
* Small min samples and large episilon results in most points being on the same cluster
* Large min samples results in most of points being classified as noise, except on desen regions when episilon is high
* Do not use silhouetter coefficient to test this model! [Recomendado](http://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=83C3BD5E078B1444CB26E243975507E1?doi=10.1.1.707.9034&rep=rep1&type=pdf)

## Gaussian Mixture Model

### Advantages

* Soft-clustering (you can see percentages of cluster participation on each sample)
* Cluster shape flexibility

### Disadvantages

* Sensitive to initialization values
* Possible to converge to a local optimum
* Slow convergence rate

# General References

* [Choosing a machine learning classifier](http://blog.echen.me/2011/04/27/choosing-a-machine-learning-classifier/)
* [1](https://kevinzakka.github.io/2016/07/13/k-nearest-neighbor/#pros-and-cons-of-knn)
* [Sklearn documentation on Neighbors](http://scikit-learn.org/stable/modules/neighbors.html#neighbors)
* [3](http://people.revoledu.com/kardi/tutorial/KNN/Strength%20and%20Weakness.htm)
* [Sklearn documentation on Stochatic Gradient Descent](http://scikit-learn.org/stable/modules/sgd.html)
* [Sklearn documentation on Ensemble Methods](http://scikit-learn.org/stable/modules/ensemble.html)
* [Logistic Regression Wikipedia](https://en.wikipedia.org/wiki/Logistic_regression)
* [Logistic Regression for machine learning](https://machinelearningmastery.com/logistic-regression-for-machine-learning/)
* [What are the advantages of logistic regression](https://www.quora.com/What-are-the-advantages-of-logistic-regression)
* [The disadvantages of Logistic Regression](https://classroom.synonym.com/disadvantages-logistic-regression-8574447.html)