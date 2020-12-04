---
layout: post
title: "Learning the name of things: Ternary Operators"
categories:
  - scala
  - python
  - javascript
  - ruby
  - computer science
  - programming language
tags:
  - scala
  - python
  - javascript
  - ruby
  - computer science
  - programming language
  - ternary operators
  - naming things
featured-img: tag
slug: ternary-operators
date: 2020-12-04T08:28:52-03:00
---

One thing that I always say that is hard from learning computer science by yourself, is not knowing what you don't know. I learned the name of a couple of concepts that I am going to share, so people know they exist 😊

When I started studying Python, if a new variable depended on another variable, I would write something like this:

<!--more-->

```python
a_boolean_variable = True
if a_boolean_variable:
    new_variable = 1
else:
    new_variable = 2
```

When I started to learn Scala, every time I found myself in this position, trying to create a new variable that depended on another condition, I tried to follow a similar structure. After some time, I discovered I could do this:

```scala
val aBooleanVariable = true
val newVariable = if (aBooleanVariable) 1 else 2
```

Then I discovered that in JavaScript (and Ruby), I could this:

```scala
val aBooleanVariable = true
val newVariable = aBooleanVariable ? "return if true" : "return if false" 
```

The `?` symbol will check if the expression before is true or false. If it is `true` it will return the first value after it, if it is `false` it will return the value after the `:` symbol.

I had absolutely no idea that this type of one-line, boolean check expression has a name: [Ternary Operators](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Conditional_Operator).  

I know it sounds super simple to write a whole post about it, but one of the main problems of not knowing how something is called is how to look for it in a new language! Now, next programming language I start studying, I can look for "ternary operators in X". Knowing the name makes it so much easier to understand the concept and extrapolate it!

To my complete surprise, I found that Python also have a way of implementing ternary operators!

```python
new_variable = 1 if a_boolean_variable else 2
```

Hope you learned something new today!

---

*Photo by Brett Jordan from Pexels*

---
