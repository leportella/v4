---
layout: post
title: "Pytest"
slug: pytest
page-description: A cheatsheet of useful pytest commands
aliases: 
  - /cheatlist/2019/01/24/pytest-cheatsheet.html
  - /cheatsheet-pytest.html
date: 2019-01-24T14:25:52-05:00
---

## Pytest minimum example

```python
# test_basic.py

def test_something():
    assert True
```

## Parametrize example

Creating multiple tests with a single function

```python
import pytest

def is_even(input):
    if input % 2 == 0:
        return True
    return False

@pytest.mark.parametrize("input,expected", [
    (2, True),
    (3, False),
    (11, False),
])
def test_is_even(input, expected):
    assert is_even(input) == expected
```

## Assert raises an error

```python
import pytest

def do_something(input):
    if input == 0:
        raise ValueError('A very specific bad thing happened.')
    return True

def test_do_something():
    with pytest.raises(ValueError):
        do_something(0)
```
 
## Basic example of fixtures

```python
import pytest

@pytest.fixture
def user():
    return {
        'name': 'John Snow',
        'email': 'john@snow.wes'
    }

def test_do_something(user):
    assert user['name'] == 'John Snow'
```
