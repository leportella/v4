---
layout: post
title: "Minhas bibliotecas favoritas para testes no Django"
categories:
  - django
  - python
  - testes
tags:
  - en
  - open-source
  - python
  - testes
  - código
  - Django
  - pytest
  - factory-boy
  - testes unitários
featured-img: board-chalk-chalkboard-459793
slug: django-testes
translationKey: testing-tools-django
date: 2020-12-07T09:28:52-03:00
---

Ao desenvolver um projeto, testes são uma ferramenta fundamental para manter as coisas fáceis e agradáveis além de ajudar a manter a sanidade da pessoa que está programando. Eu tenho usado um conjunto de ferramentas para desenvolver minhas aplicações web com Django e é hora de compartilhar um pouco sobre elas.
<!--more-->

![https://media.giphy.com/media/12WhkSmwGOGIUM/giphy.gif](https://media.giphy.com/media/12WhkSmwGOGIUM/giphy.gif)

*Mudando um código sem testes*

Para exemplificar o que podemos fazer com as ferramentas, usaremos um projeto Django que possui dois modelos: `Student` (Aluno/Aluna) e `Parent` (Mãe/Pai). `Parent` é um modelo simples com apenas dois atributos, mas  `Student` tem muitos atributos.

```python
from django.db import models

class Parent(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    address = models.CharField(max_length=300)
    resume = models.TextField()
    age = models.PositiveSmallIntegerField()
    email = models.CharField(max_length=250)
    date_started = models.DateTimeField()
    gender = models.CharField(max_length=200)
    parent = models.ForeignKey(Parent, related_name='children',
                               on_delete=models.CASCADE)

```

Observação: O código completo do projeto está disponível [aqui](https://github.com/leportella/testing-tools) :) mas o post original foi lançado em 2018 então deve ter algumas coisas desatualizadas!

## Lazy shell

![https://media.giphy.com/media/UiCSHJrkCr02Y/giphy.gif](https://media.giphy.com/media/UiCSHJrkCr02Y/giphy.gif)

Assim que tivermos nosso modelo configurado e nosso banco de dados instalado e funcionando, podemos verificar o que está acontecendo em nosso banco de dados usando o *shell* padrão do Django executando (usando [pipenv](https://pipenv.pypa.io/en/latest/)):

```bash
$ pipenv run school/manage.py shell
```

Depois disso, o *prompt* do *shell* está disponível para nós. Podemos importar nosso modelo `Parent`, por exemplo, e verificar quantas instâncias já temos em nosso banco de dados. 

Agora imagine que você está trabalhando com um grande projeto com muitas classes de modelo para importar. Importar cada classe de modelo torna-se uma tarefa entediante e demorada. Vamos fazer isso de maneira mais inteligente!

{{<figure src="https://i.imgur.com/OygSiVi.png#center">}}

Eu uso o `django_extensions` para me ajudar a lidar com isso. Quando você usa ele, todas as classes de modelo são importadas por padrão assim que o *shell* é iniciado. Tem muitas coisas legais também, mas, para mim, apenas as importações são suficientes para tornar crucial o uso dele no desenvolvimento do dia-a-dia.

Uma vez que você instalou a biblioteca, você deve adicioná-la no `INSTALLED_APPS`:

```python
# settings.py

INSTALLED_APPS = [
    ...

    # bibliotecas externas
    'django_extensions', 
]

```

Para acessar o novo terminal aprimorado, use:

```bash
pipenv run school/manage.py shell_plus
```

Prontinho! Com uma linha apenas você consegue ver quantas instâncias você tem!

{{<figure src="https://i.imgur.com/uZ4lsSj.png#center">}}

## Configurando o Pytest

Para testar seu código, você realmente deveria usar o [Pytest](https://docs.pytest.org/en/latest/), que é uma ótima ferramenta
especializado em testes. Pytest é um framework cheio de extensões e truques que estão longe do escopo deste post, mas você totalmente deveria investir e aprender!

Bruno Oliveira [lançou um livro para te ajudar a aprender](https://www.packtpub.com/web-development/pytest-quick-start-guide) :) Vai lá conferir se gostar do que vê aqui, ok?

Para configurar o `pytest` para funcionar com Django, crie um arquivo `pytest.ini` na mesma pasta que você mantém o `manage.py`.

O arquivo deve ser semelhante a este:

```
# pytest.ini
[pytest]
DJANGO_SETTINGS_MODULE = school.settings
python_files = tests.py test_*.py *_tests.py

```

Não esqueça de mudar  `school` para o nome do seu projeto!

Vamos testar?

`$ pipenv run pytest`

O resultado é bem legal mas nenhum teste foi encontrado...

{{<figure src="https://i.imgur.com/uVwLcSG.png#center">}}

Vamos verificar se está funcionando ... crie uma pasta `tests` no nosso app `student` e adicione um arquivo `tests.py`. Não se esqueça de adicionar um arquivo vazio `init.py` na mesma pasta, para que o Pytest seja capaz de encontrar a pasta. No arquivo `tests.py` criamos um teste simples que irá falhar com certeza, apenas para fazer as coisas andarem ...

```python
# student/tests/tests.py

def test_something():
    assert True == False
```

Rode de novo e.... voilá! Ele encontrou o teste e o alerta aparece na tela em vermelho.

{{<figure src="https://i.imgur.com/bQVyEFA.png#center">}}

Se consertarmos o teste, tudo fica verdinho:

{{<figure src="https://i.imgur.com/ltr7cL1.png#center">}}

## Lazy records

Para ter algo para testar, vamos usar um exemplo de endpoint simples que mostra detalhes de um aluno específico. Usaremos a biblioteca `restless` para isso, a mesma que mostrei como escrever endpoints [neste post](https://leportella.com/restless/).

Você pode ver a variável `preparer` que vai fazer nosso endpoint retornar apenas o nome do estudante:

```python
from restless.dj import DjangoResource
from restless.preparers import FieldsPreparer

from .models import Student

class StudentResource(DjangoResource):
    preparer = FieldsPreparer(fields={
        'name': 'first_name',
    })

    def detail(self, pk):
        return Student.objects.get(pk=pk)

```

Vamos testar nosso novo endpoint ... e temos um problema: não há nada em nosso banco de dados para testar a resposta:

{{<figure src="https://i.imgur.com/d6LEYcq.png#center">}}

Podemos abrir nosso novo `shell_plus` e começar a adicionar coisas. Bem, `Student` depende de uma instância `Parent`, então primeiro adicionamos um novo `Parent`. Não podemos esquecer de salvá-lo, caso contrário não funcionará (acredite, eu fiz isso enquanto escrevia isso). Agora temos uma tonelada de informações que precisamos encontrar para criar um novo registro de banco de dados. E novamente ... não se esqueça de salvá-lo.

Agora podemos manualmente testar nossa API:

{{<figure src="https://i.imgur.com/ODgKrIF.png#center">}}

Tudo funciona mas o processo é bem manual.

Conforme o projeto cresce, testar coisas fica mais e mais difícil, e mais instâncias são requeridas para testar funcionalidades complexas. Portanto, escrever tudo à mão toda vez realmente não parece uma boa abordagem.

Eu uso uma biblioteca chamada `factory-boy` para criar essas informações para mim. Vamos começar com o modelo `Parent`. Nós criamos uma classe chamada `ParentFactory` que herda a `factory.DjangoModelFactory`. Na classe `Meta`, dizemos à esta fábrica, 
o modelo ao qual esta fábrica se refere. Agora pegamos todos os atributos do modelo e os adicionamos nesta fábrica usando  `factory.Faker`. Sim, ele aparecerá com nomes de maneira coerente e você não precisa se preocupar com inventar sobrenomes.

```python
# student/tests/factories.py

import factory
from student.models import Parent

class ParentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Parent

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')

```

Agora vamos ver ... começamos sem nenhum registro de `Parent` em nosso banco de dados. Depois de instanciar nossa `ParentFactory`, temos um novo registro salvo em nosso banco de dados. Maravilha! E você pode ver agora que este novo `Parent` é chamado de `Karen Palmer`, ou seja, nossa fábrica criou uma nova instância no banco de dados com um nome normal (não apenas um monte de letras embaralhadas).

{{<figure src="https://i.imgur.com/OJdQkyh.png#center">}}

Agora podemos fazer o mesmo com a classe `Student`. `Factory boy` tem muitas ferramentas que podem ajudá-lo nessa tarefa:
`Fakers` para nome, sobrenome, endereço e texto, número inteiro, criam e-mails com base no nome e sobrenome da instância, e escolha aleatória para o gênero.

Precisamos não apenas dessas muitas informações sobre o aluno, mas também de outra instância do banco de dados. Para isso, o adicionamos como uma subfábrica do
`ParentFactory`. Isso garante que toda vez que uma nova instância de `Student` é criada, uma instância `Parent` é criada com ela para preencher essa necessidade.

```python
class StudentFactory(factory.DjangoModelFactory):
    class Meta:
        model = Student

    parent = factory.SubFactory(ParentFactory)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    address = factory.Faker('address')
    resume = factory.Faker('text')
    age = fuzzy.FuzzyInteger(6, 12)
    email = factory.LazyAttribute(
        lambda o: f'{o.first_name.lower()}.{o.last_name.lower()}@mail.org')
    date_started = fuzzy.FuzzyDateTime(datetime.now(tz=utc))
    gender = fuzzy.FuzzyChoice(['male', 'female', 'other'])

```

Agora vamos testar essa configuração. Podemos criar uma nova instância de `Student` e, mesmo já tendo uma instância de `Parent` no banco de dados, o `Factory` cria uma nova instância de `Parent` para adicionar à nova instância de `Student` sendo criada. 

{{<figure src="https://i.imgur.com/kiMtm4t.png#center">}}

Agora, se quisermos criar um outro `Student` que tem o mesmo `Parent` que este aluno anterior, só precisamos passar para a nova `StudentFactory` uma instância já criada
de `Parent`. Dessa forma, ele não criará uma nova instância, mas adicionará a instância que você acabou de passar para ele.
Agora mantivemos o mesmo número de `Parent`s que já tínhamos em nosso banco de dados, mas agora temos dois `Student`s com o mesmo `Parent`:

{{<figure src="https://i.imgur.com/VhvUavi.png#center">}}

Isso, por si só, já faz a nossa vida ser muito mais fácil... mas tem mais! Você também pode criar múltiplas instâncias de uma vez só. Então você consegue encher o banco de dados com apenas uma linha!

{{<figure src="https://i.imgur.com/ky1zjCC.png#center">}}

Mais simples, impossível!

{{<figure src="https://media.giphy.com/media/l0MYtTptyL8h88UHm/giphy.gif#center">}}

## Testes automatizados de API

Anteriormente, nós testamos nosso `endpoint` manualmente, mas essa não é a melhor maneira de fazer isso. Precisamos criar um teste unitário para garantir
ele está funcionando agora e estará no futuro, quando adicionarmos mais coisas ao nosso projeto. Para testar o endpoint, precisaremos
usar um cliente do Django (ou algo semelhante) pra conseguir chamar o `endpoint` de dentro do ambiente de tests. Usar um cliente com `pytest` é suuuper difícil. Brincadeira 😅 Na verdade, só precisamos instalar o `pytest_django` e pronto.

{{<figure src="https://media.giphy.com/media/l0K4jrpWppNAAzucU/giphy.gif#center">}}

Agora, apenas criamos um teste e passamos, magicamente,  um parâmetro `client` para a função. Pronto! Só isso! Pytest fará sua mágica e tudo funciona.
Agora temos nosso cliente instalado e pronto para testes. Neste teste, criamos uma nova instância de `Student`, e depois usamos o método`client.get` para acessar o `endpoint`. O url
é montado usando o id da instância que acabamos de criar.

Por enquanto, vamos apenas nos certificar de que nossa resposta receba um código `200`:

```python
# student/tests/tests.py

import pytest
from .factories import StudentFactory

@pytest.mark.django_db
def test_endpoint(client):
    student = StudentFactory()
    response = client.get(f'/api/{student.id}', follow=True)
    assert response.status_code == 200

```

Você notou que acima de nossa função de teste eu adicionei um decorador `@pytest.mark.django_db`? Este é um *helper* e é dessa forma que marcamos que esta função de teste está exigindo integração com o banco de dados. Isso garantirá que o banco de dados seja configurado corretamente para este teste em particular. Mais
informações sobre os ajudantes podem ser vistas [aqui](https://pytest-django.readthedocs.io/en/latest/helpers.html).

Também podemos carregar o conteúdo da resposta usando a lib `json` e ter certeza de que o nome que a API retornou é o nome que realmente queremos.

```python
import json
import pytest
from .factories import StudentFactory

@pytest.mark.django_db
def test_endpoint(client):
    student = StudentFactory()
    response = client.get(f'/api/{student.id}', follow=True)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content['name'] == student.first_name

```

Agora imagine que temos vários testes que precisam de um registro de `Student`. É um desperdício continuar a criá-lo de novo e de novo. O `pytest` permite criar `fixtures`, que são funções que podem ser adicionadas em seu teste.
Por exemplo, no código abaixo você vê que criamos uma `fixture` que retorna uma instância de `Student`. Para usá-la em nosso teste, basta adicionar `user` (o nome da função) como um parâmetro de entrada do nosso teste. A única coisa é que o `client` sempre deve ser o primeiro parâmetro da função de teste.

Agora, não precisamos mais criar este `Student` em nenhuma outra linha.
A instância criada pela `fixture` estará disponível neste e em qualquer outro teste que adicione a função `user` à função de teste.

```python
import json
import pytest

from .factories import StudentFactory

@pytest.fixture
def user():
    return StudentFactory()

@pytest.mark.django_db
def test_endpoint(client, user):
    response = client.get(f'/api/{user.id}', follow=True)
    content = json.loads(response.content)
    assert response.status_code == 200
    assert content['name'] == student.first_name

```

E se você precisar usar o `ipdb` com esse teste, apenas execute `pytest` com um parâmetro extra: `pipenv run pytest -s`

É isso ... com o combo `django_extensions` +`factory boy` + `pytest`, testes se tornam uma coisa muito divertida de fazer :)

![https://media.giphy.com/media/aiE3JQU3vLqTK/giphy.gif](https://media.giphy.com/media/aiE3JQU3vLqTK/giphy.gif)
