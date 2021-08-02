---
layout: post
title: "Injecting authenticated user when creating a model with CreateView"
categories:
  - Class Based Views
  - Django
  - Python
tags:
  - Django
  - Python
  - Frameworks
  - Class Based Views
  - CBV
featured-img: pencils
translationKey: inject-auth-user-cbv
slug: inject-auth-user-cbv
date: 2021-08-02T14:25:52+01:00
---

I had a Django model that had 2 regular attributes and a user Foreign Key:

<!--more-->

```python
from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    user = models.ForeignKey(
            User, 
            on_delete=models.CASCADE)
```

The problem started when I wanted to create a new instance using a `CreateView` but I wanted to create the model with the user being the logged in user.  In the form, however, I would only display the fields `text` and `title`, but internally I wanted to fill the model with the authenticated user.

First I created a simple CreateView class:

```python
class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes'
    fields = ('title', 'text')
```

But when I tried to save the model to the database, I would get an error: `NOT NULL constraint failed: notes_notes.user_id`.

The problem was that [when calling the method `form_valid`]() , the CreateView would call the method `form.save()`  that would try to go to the database. Since we have no user, the error happens at the database layer.

My first approach was trying to add the user in the form or even in the `cleaned_data`. If I done it this way, when I called the `form.save()` method, it would just work. Although I tried a lot, I couldn't do it. So I needed something a bit more tricky. Here is the solution:

```python
class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes'
    fields = ('title', 'text')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
```

What is happening here is that I tell the `.save()` method to **not** save anything on the database. This way, we get an instance of the model, but no commitment, and thus, no errors. Once we have the object we can inject the logged user and finally save the object to the database, which can happen with no errors. 

There you go :) Now your models are created with an associated user. Nice and easy!
