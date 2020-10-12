---
layout: post
title: "Pandas - My Cheatsheet"
categories:
  - english
  - cheatsheet
tags:
  - en
  - python
  - pandas 
  - cheatlist
  - python
  - community 
  - pyladies
  - technology
  - tecnologia
  - programador
  - programadora
  - developer
  - mulheres na tecnologia
  - woman in tech
  - girls in tech
  - computação
  - ciência de computação
  - software development
  - software engineering
  - engenharia de software
  - desenvolvimento
  - auto-ensino
  - self-taught engineer
  - code
  - Django
  - software
  - career
  - tech career
  - open-source
  - no cs degree
  - cs
  - computer science
  - data science
  - ciência de dados
featured-img: panda
slug: pandas
aliases:
  - /cheatsheet-pandas.html
  - /cheatlist/2017/11/22/pandas-cheat-list.html
date: 2017-11-22T14:25:52-05:00
last_mod: 2018-05-01T14:25:52-05:00
---


Sometimes I get just really lost with all available commands and tricks one can make on pandas. 
This way, I really wanted a place to gather my tricks that I really don't want to forget.

{{<figure src="https://media.giphy.com/media/EwO9pwLnPlttu/giphy.gif#center">}}


# My Pandas Cheatsheet


## How to list available columns on a DataFrame

```python
df.columns.values
```

## How to make multiple filters

```python
df[(df.column > value1) & (df.column < value2)]
```

## How to iterate over a Dataframe

```python
for item, row in df.iterrows():
  print row()
```

## How to count the ocurrences of each unique values on a Series

```python
df[column].value_counts()

# get indexes
df[column].value_counts().index.tolist()

# get values of occurrences
df[column].value_counts().values.tolist()
```

## How to save a DataFrame by chunks

```python
df = pd.DataFrame([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

df1 = df.iloc[0:2,:]
df2= df.iloc[2:,:]

df1.to_csv('./teste1.csv', index=False, header=False)
df2.to_csv('./teste1.csv', index=False, header=False, mode='a')

df_final = pd.read_csv('./teste1.csv')
df_final.head()
```

## A groupby example

```python
df_grouped = df.groupby(
        by=['first_column', 'second_column']
    )['third_column'].mean().reset_index(name='mean_values_grouped')
```

## How to fill values on missing months

If you have a dataframe with 2 columns: year and month. But data is not available for all months, so you need to enter missing months on 
your dataframe with empty values on them.

```python
# Original data with months not available
df1 = pd.DataFrame({
    'month': [1, 2, 4, 5, 6, 8, 9, 10, 11, 12, 1, 2, 3, 4,
              5, 8, 9, 10, 11, 12],
    'year': [2011, 2011, 2011, 2011, 2011, 2011, 2011, 2011,
             2011, 2011, 2012, 2012, 2012, 2012, 2012, 2012, 
             2012, 2012, 2012, 2012],
    'qty': [5, 7, 3, 6, 7, 8, 3, 5, 7, 10, 12,
            5, 7, 8, 1, 3, 5, 7, 8, 20]
})

# List of all months
df2 = pd.DataFrame({'month': list(range(1,13))})
```
 
Now we create an empty dataframe with all available years and months:

```python
from itertools import product

years_months = pd.DataFrame(list(product(np.unique(df2.month), np.unique(df1.year))), columns=['month', 'year'])
```

Now we can just merge both dataframes with an outer join:

```python
pd.merge(years_months, df1, how='outer')
```

## How to filter column elements by multiple elements contained on a list

```python
df[df['A'].isin([3, 6])]
```

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


