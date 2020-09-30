---
layout: post
title: "Dataframes"
slug: dataframes
date: 2017-12-31T19:55:58+01:00
last_mod: 2018-05-01T14:25:52-05:00
---

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