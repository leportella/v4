---
layout: post
title: "SQL - My Cheat Sheet"
categories:
  - english
  - cheatsheet
tags:
  - en
  - python
  - pytest
  - cheatlist
  - cheastsheet
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
  - sql
  - database
featured-img: search
slug: sql
aliases:
  - /cheatsheet-sql.html
date: 2020-04-25T14:25:52-05:00
---

## Query if a string is in a list

```sql
select name, 
    from my.table
where name IN ('jon', 'mary')
```

## Query within a timestamp

```sql
select record
    from my.table
where
    created > timestamp '2019-10-01 00:00' AND
    created < timestamp '2019-10-01 23:59'
```

## Creating temporary table

```sql 
with my_new_table as (
  -- something here
  select *
  from another.table
)

select *
from my_new_table
```

## String comparison

```sql
select
    *
from my_table
where my_table.items LIKE '%something%'
limit 10
```

## Search for empty or null strings

```sql
where (surname is null or surname = '')
```