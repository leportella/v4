---
layout: post
title: "SQL"
slug: sql
page-description: A cheatsheet of useful SQL commands
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