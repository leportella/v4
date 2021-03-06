---
layout: post
title: "Data Visualization - My Cheat Sheet"
categories:
  - english
  - cheatsheet
tags:
  - en
  - python
  - pytest
  - cheatlist
  - cheastsheet
  - data visualization
  - matplotlib
  - seaborn
  - dataviz
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
  - pizza de dados
featured-img: dataviz
slug: data-visualization
aliases: 
  - /cheatlist/2019/02/19/data-visualization-cheatsheet.html
  - /cheatsheet-data-visualization.html
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
