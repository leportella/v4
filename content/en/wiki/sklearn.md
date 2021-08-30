---
layout: post
title: "Sklearn"
page-description: A cheatsheet of useful sklearn commands
slug: sklearn
aliases: 
  - /cheatsheet-sklearn.html
  - /cheatlist/2018/05/01/sklearn-cheat-list.html
date: 2018-05-01T14:25:52-05:00
---

## How to check results of accuracy for each of the classes available on a classification problem?

```python
from sklearn.metrics import classification_report

classification_report(y_test, y_pred, target_names=['A', 'B', 'C']

# Results:

             precision    recall    f1-score 

A              0.9         ...         ...
      
B              0.9         ...         ...
 
C              0.9         ...         ...
 
avg/total      0.9         ...         ...
```

## How to normalize features?

```python
from sklearn import preprocessing

normalized_X = preprocessing.normalize(X)
```

## How to create a bag of words dataframe matrix

```python
import pandas as pd
from sklearn.feature_extraction.text imprt CountVectorizer

documents = ['Hello, how are you!',
             'Win money, win from home.',
             'Call me now.',
             'Hello, Call hello you tomorrow?']

count_vector = CountVectorizer()
count_vector.fit(documents)

doc_array = count_vector.transform(documents).toarray()

freq_matrix = pd.DataFrame(doc_array, columns=count_vector.get_feature_name())
```

## How to export a trained model

```python
from sklearn.externals import joblib

joblib.dump(model, 'name.pkl')

# to read
model = joblib.load('name.pkl')
```
