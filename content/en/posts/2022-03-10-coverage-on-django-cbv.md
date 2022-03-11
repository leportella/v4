---
layout: post
title: "Python Coverage reports 100% coverage on an untested Class Based View!"
categories:
  - Python
  - class based views
  - django
  - test
  - pytest
tags:
  - Python
  - class based views
  - Django
  - test
  - pytest
  - pytest-cov
  - coverage
  - unit testing
  - test coverage
  - CBV
  - Django Views
  - testing framework
featured-img: pedestre
img-description: a blackboard with 3 chalk lines
translationKey: coverage-and-cbvs 
slug: coverage-and-cbvs 
date: 2022-03-10T00:26:52+01:00
---

While trying to check test coverage for a file that had multiple Class Based Views (CBV) everything was returning as coverage but they weren’t! I couldn’t understand why and it took me days until I get to an answer! So I wrote this post to make it more easily accessible 😊 

<!--more-->

## Testing a Class Based View

It all started when I had a `views` file that had a couple of very basic views: a welcome page (simple template), login and logout pages and a signup page. The Signup page has a small rewrite of the `get` method, that redirects the user to an internal page if they are already logged in. 

```python
# home/views.py

from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import redirect

class SignupView(CreateView):
    form_class = UserCreationForm
    template_name = 'home/register.html'
    success_url = '/smart/notes'

    def get(self, request, *args, **kwargs):
				# redirects user to an internal page if they are logged in 
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)

class LogoutInterfaceView(LogoutView):
    template_name = 'home/logout.html'

class LoginInterfaceView(LoginView):
    template_name = 'home/login.html'

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}
```

I wanted to add some tests to my Class Based Views, so I created the most basic one: a test that checks that my home page returns a 200 and the correct template:

```python
# home/tests/test_home_views.py

def test_home_endpoint_returns_welcome_page(client):
    response = client.get(path='/')

    assert response.status_code == 200
    assert 'home/welcome.html' in response.template_name
```

## Test coverage

I decided I wanted to evaluate the coverage of my Django app, so I installed the [coverage](https://coverage.readthedocs.io/en/6.3.2/) library and ran the following command:

```bash
$ coverage run -m pytest
$ coverage html
$ open htmlcov/index.html
```

This open a browser where I could see the complete report per file:


{{<figure src="/assets/img/posts/cbv-coverage/01.png#center" lt="A screenshot of a list of files with the percentage of lines coverage">}}

## The problem

This got me by surprise! I only tested 1 of the multiple views I had on the file! How could I ever get the 88% coverage reported there!?

I opened the file for the specific view, and it showed me that *all* CBVs were being set as covered with the only exception being the code I had overridden in the get method of the `SignupView`:

{{<figure src="/assets/img/posts/cbv-coverage/02.png#center" lt="A screenshot of almost all code shown before as covered by tests">}}

This took me by surprise! I only tested `HomeView`, why is `LoginInterfaceView`, `LogoutInterfaceView` and `SignupView` being shown as tested as well!?

## What happened

Well after *days* trying to understand what i was doing wrong I got to [this answer](https://stackoverflow.com/a/65003581/3538098):

> [*Coverage.py](http://coverage.py/) can only tell you whether a line of code has been executed.*

Then the additional comment gives an extra flavor to it:

> *During the test, Django has to load the classes and other modules into the memory, and hence the program (your class and settings and many other parts) get executed.*
    
    

So what’s happening here, is that CBVs are classes, when you run the tests Django will load them into memory, which means that they will be executed. When I ran the coverage, it will look for “executed” code and they will appear as tested.

The Class Based View method I have overridden is not run while loading Django and that’s why it isn’t considered as tested!

I continue to love Class Based Views buuuut you should be careful when using Coverage to check if you have tested them enough! 

{{<figure src="https://media3.giphy.com/media/l4FGyRwwFPBFQt4cg/giphy.gif?cid=ecf05e47rg5zmu35kfsimam8i1s98ohoxujshkq2bwq743fy&rid=giphy.gif&ct=g#center" lt="Gif of a cartoon bull in the middle of a porcelain room">}}
