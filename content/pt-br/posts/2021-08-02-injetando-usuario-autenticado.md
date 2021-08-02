---
layout: post
title: "Injetando um usuário autenticado num modelo criado via CreateView"
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
slug: injetando-usuario-autenticado
date: 2021-08-02T14:25:52+01:00
---

Eu tinha um modelo específico que continha dois atributos regulares e uma Chave Estrangeira (Foreign Key) com um usuário:

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

O problema começou quando eu queria criar uma nova instância usando como base a *Class Based View* `CreateView`, mas queria que o usuário fosse preenchido com o usuário que estava autenticado. No `form`, entretanto, eu queria exibir apenas os campos `text` e `title`, mas internamente queria preencher o modelo com o usuário autenticado.

Primeiro eu criei uma classe base usando o `CreateView`:

```python
class NotesCreateView(CreateView):
    model = Notes
    success_url = '/notes'
    fields = ('title', 'text')
```

Quando eu tentei usar essa classe para salvar a instância no banco de dados, eu recebia um erro dizendo que o usuário estava nulo: `NOT NULL constraint failed: notes_notes.user_id`.

O problema era que [quando a CreateView chamava o método `form_val`](), esse método chamada `form.save()` que tentaria ir ao banco de dados salvar essa nova instância. Como o form não tinha usuário, o erro acontecia na camada do banco de dados.

Minha primeira tentativa foi adicionar o usuário direto no `form` ou mesmo injetá-lo no atributo `cleaned_data`. Se feito dessa forma, uma vez que eu chamasse o  `form.save()`, tudo funcionaria muito bem. Eu tentei bastante, mas não consegui seguir por esse caminho. No final, precisei de algo um pouco mais complexo. Aqui está:

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

O que está acontecendo aqui é que eu digo ao método `.save ()` para **não** salvar nada no banco de dados. Dessa forma, eu consigo obter uma instância do modelo, mas sem que ela esteja  no banco e, portanto, sem erros. Assim que eu pego este objeto, eu consigo injetar o usuário logado e finalmente salvar o objeto no banco de dados, o que acontece sem erros.

Pronto :) Agora seus modelos são criados com o usuário autenticado! Chatinho, mas fácil!
