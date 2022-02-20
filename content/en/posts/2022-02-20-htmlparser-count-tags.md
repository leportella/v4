---
layout: post
title: "Counting tags with HTMLParser"
categories:
  - Python
  - tutorial
tags:
  - HTMLParser
  - Python
  - tutorial
  - HTML
  - BeautifulSoup
  - HTML Tags
featured-img: count
img-description: a blackboard with 3 chalk lines
translationKey: htmlparser
slug: htmlparser-count-tags
date: 2022-02-20T14:26:52+01:00
---

I fell into a case where I wanted to count the tags that were present in an HTML file and I didn't want to download any library (like BeautifulSoup) to do so. I searched online and realized I could use the HTMLParser to do that. <!--more-->
The problem was that I found this library to be *very* unintuitive and it took me forever to understand how to do that. I will explain the solution step by step but you can skip to the end to see the final result 👾

## My problem with HTMLParser

The problem I had was that my first intuition was to do this: 


```python
from html.parser import HTMLParser

parser = HTMLParser()
parser.feed(html) # html is a string
```

...and nothing happened. I looked around and there wasn't any method that could help me do the count. I searched online and all the tutorials and answers was telling me to create a new class, but I didn't understand why.

After some time questioning my sanity, I realized that I was expecting HTMLParser to be just like BeautifulSoup which translates the HTML into a structure I can search on. However, HTMLParser doesn't do that. It's actually *iterating* over the HTML tags but doesn't *do* anything with it. The reason why you need to implement a class to inherit from the HTMLParser is to actually implement the methods! 

The reason I was not able to *do* anything with the parser once I fed it the HTML is because the HTML is parsed once I fed it, but there isn't anything to do with it after it was parsed. Because I hand't implemented anything.... I couldn't see anything!

What I needed to do is actually implement a class and everytime I found a new tag, I would increase a counter... something like this:

```python
count_h1 = 0 

class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
    	if tag == 'h1':
        	count_h1 += 1
```

## Solution

Finally I decided to use a `defaultdict` so I could count every tag once it appeared. The final solution was this:

```python
from html.parser import HTMLParser
from collections import defaultdict

class MyHTMLParser(HTMLParser):
    def __init__(self):
        self.count = defaultdict(int)
        super().__init__()

    def handle_starttag(self, tag, attrs):
        self.count[tag] += 1

    def handle_startendtag(self, tag, attrs):
        self.count[tag] += 1

def count_tags(html):
  parser = MyHTMLParser()
  parser.feed(html)
  return parser.count
```

The `handle_starttag` investigates tags that have an opening and a closing tag (like `<h1></h1>`) while the `handle_startendtag` is used in tags that don't have a closing argument (like `<link />`).

## Result

If I take this html:

```python
html = """
<html>
  <head>
    <link rel="stylesheet" type="text/css" href="style.css"/>
  </head>
  <body>
        <nav class='navbar navbar-dark bg-dark'>
            <div class='ms-auto'>
                <a href="/smart/notes" class="btn btn-outline-light me-1">Home</a>
                <a href="/smart/notes/new" class="btn btn-outline-light me-1">Create</a>
                <a href="/logout" class="btn btn-outline-light me-1">Logout</a>
            </div>
        </nav>
        <div class="my-5 text-center container">
            <h1 class="my-5">These are the notes:</h1>
                <div class="row row-cols3 g-2">
                    <div class="col">
                        <div class="p-3 border">
                            <a href="/smart/notes/1" class="text-dark text-decoration-non"><h3>An unique note title</h3></a>
                                some text
                        </div>
                    </div>
                    <div class="col">
                        <div class="p-3 border">
                            <a href="/smart/notes/2" class="text-dark text-decoration-non"><h3>Anoter note</h3></a>
                                another text
                        </div>
                    </div>
                </div>
        </div>
    </body>
</html>
"""
```

And pass it to the function we just created, the result will be:

```python
tags = count_tags(html)
print(tags) # defaultdict(<class 'int'>, {'html': 1, 'head': 1, 'link': 1, 'body': 1, 'nav': 1, 'div': 7, 'a': 5, 'h1': 1, 'h3': 2})
```

And I can access any HTML tag to see the count:

```python
print(tags['html']) # 1
```

And because we used a defaultdict, we can actually try to get an HTML tag that isn't there, and it won't fail:

```python
print(tags['h6']) # 0
```

---
*Photo by Miguel Á. Padriñán*


