---
layout: post
title: "Supervised"
slug: supervised
date: 2018-05-20T14:25:52-05:00
---

## Logistic Regression

### Advantages

* Don't have to worry about features being correlated
* You can easily update your model to take in new data (unlike Decision Trees or SVM)

### Disadvantages

* Deals bad with outliers
* Must have lots of incomes for each class
* Presence of multicollinearity

## Decision Tree

### Advantages

* Easy to understand and interpret (for some people)
* Easy to use - Doesn’t need data normalisation, dummy variables, etc 
* Can handle multi-output models
* Easily handle feature interactions
* Don't have to worry about outliers

### Disadvantages

* It can be easily overfitted
* Stability —> small changes in data can lead to completely different trees
* If a class dominates, it can easily be biased
* Don't support online learning --> you should rebuilt the tree when new data comes


## Ensemble Methods

### Advantages

* Harder to overfit
* Usually better perfomance than a single model

### Disadvantages

* Scaling —> usually it trains several models, which can have a bad performance with larger datasets
* Hard to implement in real time platform
* Complexity increases
* Boosting delivers poor probability estimates (https://arxiv.org/ftp/arxiv/papers/1207/1207.1403.pdf)

## K-nearest Neighbors

### Advantages

* Little training time
* Works well with multiclass datasets 
* Good for highly unusual data

### Disadvantages

* Need to determine value of k (distance)
* Neighbors-based methods are known as non-generalizing machine learning methods, since they simply “remember” all of its training data
* The accuracy of KNN can be severely degraded with high-dimension data because there is little difference between the nearest and farthest neighbor.

## Gaussian Naive Bayes

### Advantages

* Need less training data tran models like logistic regression
* Highly scalable
* Not sensitive to irrelevant features
* Returns the degree of certanty of the answer
* Good when you need something fast and that perfoms well

### Disavantages

* Can't learn interactions between features e.g., it can’t learn that although you love movies with Brad Pitt and Tom Cruise, you hate movies where they’re together).

## SVM

### Advantages

* High accuracy
* Nice theoretical guarantees regarding overfitting
* Especially popular in text classification problems

### Disavantages

* Memory-intensive
* Hard to interpret
* Complicated to run and tune

## Stochastic Gradient Descent

### Advantages

* Efficiency
* Ease implementation

### Disavantages

* A lot of hyperparameters to tune
* Sensitive to feature scaling


## General References

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
