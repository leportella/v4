---
title: "Series"
slug: series
page-description: A cheatsheet of useful Pandas Series commands
date: 2017-11-30T19:55:58+01:00
last_mod: 2020-09-30T19:55:58+01:00
original: 2017-11-22T14:25:52-05:00
---

## How to change a Series type?

```python
import pandas as pd

serie = pd.Series([1, 2, 3, 4])
series.astype(float)
```

## How to apply a function to every item of my Serie?

```python
import pandas as pd

serie = pd.Series(['a', 'b', 'b', 'a'])
series.apply(lambda x: 0 if x=='a' else 1)
```

## How to prepare my DataFrame to apply get_dummies?

```python
import pandas as pd

X = pd.read_csv(..)
categorical = ['x1', 'x2', 'x4']  # columns that have categorical features in your X

for cat in categorical: 
    X[cat] = X[cat].astype(object)

X_dummy = pd.get_dummies(X)
```

## read_csv errors of encoding

Usually you can read a csv just by doing something like:

```python
pd.read_csv('file.csv')
```

Sometimes, an encoding error appears. The first option is to pass 'utf8' as a value of 
the parameter `encoding`.  

```python
pd.read_csv('file.csv', encoding='utf8')
```

But there are some cases where this is not enough and the following error keeps appearing:

`UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc7 in position 4: invalid continuation byte`

The only thing that could resolve this was:

```python
pd.read_csv('file.csv', encoding='latin-1')
```


## Sum values of all columns

```python
df.sum(axis=1)
```


## Use apply for multiple columns

```python
def my_function(a, b):
  return a + b


df.apply(lambda row: my_function(row['a'], row['b']), axis=1)
```


