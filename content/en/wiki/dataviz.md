---
layout: post
title: "Data Visualization"
slug: data-visualization
page-description: How to create plots based on your pandas dataframe
date: 2019-02-19T14:25:52-05:00
---

## Seaborn Heatmap

Simple example with a colormap with light colors on small values and black colors on high values:

```python
grouped = df.groupby(['column1', 'column2']).size().unstack()
h = sns.heatmap(grouped, cmap='bone_r')
```

Show values of each group:

```python
grouped = df.groupby(['column1', 'column2']).size().unstack()
h = sns.heatmap(grouped, annot=True)
```

Changing colorbar limits:

```python
grouped = df.groupby(['column1', 'column2']).size().unstack()
h = sns.heatmap(grouped, vmin=0, vmax=100)
```

Change annotation fontsize:

```python
grouped = df.groupby(['column1', 'column2']).size().unstack()
h = sns.heatmap(grouped, annot=True, annot_kws={"size": 12})
```

Full example:
```python
grouped = df.groupby(['column1', 'column2']).size().unstack()
h = sns.heatmap(grouped, cmap='bone_r', annot=True, 
                annot_kws={"size": 12}, vmin=0, vmax=100)
```
