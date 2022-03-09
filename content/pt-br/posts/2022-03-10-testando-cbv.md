---
layout: post
title: "Python Coverage reporta 100% de cobertura em uma Class Based View não testada!"
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
img-description: um quadro negro com três riscos em giz
translationKey: coverage-and-cbvs 
slug: coverage-e-cbvs 
date: 2022-03-10T00:26:52+01:00
---


Eu estava tentando ver a cobertura de testes para um arquivo que tinha múltuplas Class Based Views (CBV). Apesar de não haver *nenhum* teste disponível, o relatório reportava que o meu arquivo estava todo coberto por tests! Eu realmente não consegui entender o que estava acontecendo e eu demorei dias até finalmente ter alguma resposta! Esse texto deixa a resposta um pouco mais acessível pras próximas pessoas que passarem por isso 😊

<!--more-->

## Testando uma Class Based View

Tudo começou quando eu tinha um arquivo `views` que tinha algumas *views* bem básicas: uma página de boas vindas (um template apenas), páginas de login e logout e uma página pra criar uma conta (signup). A `view` do Signup era a única que tinha um método sendo sobrescrito pela minha `view`: o método  `get`. O método apenas redirecionaca o usuário para uma página interna caso já estivesse autenticado.

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
        # redireciona o usuário para uma página interna se autenticado
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

Eu queria testar essas views então eu criei o teste mais básico possível: checava que a página de boas vindas retornava 200 (sucesso) e que o template retornado era o correto:

```python
# home/tests/test_home_views.py

def test_home_endpoint_returns_welcome_page(client):
    response = client.get(path='/')

    assert response.status_code == 200
    assert 'home/welcome.html' in response.template_name

```

## Cobertura de testes

Antes de continuar adicionando testesd, eu decidi dar uma olhada na cobertura, pra planejar minha estratégia de testes. Eu instalei a biblioteca [coverage](https://coverage.readthedocs.io/en/6.3.2/) e rodei os seguintes comandos:

```
$ coverage run -m pytest
$ coverage html
$ open htmlcov/index.html

```

O último comando vai abrir um nevegador onde eu posso ver o relatório completo por arquivo:

{{<figure src="/assets/img/posts/cbv-coverage/01.png#center" lt="Uma captura de tela mostrando uma lista de arquivos e o percentual de linhas cobertas em cada arquivo">}}

## O problema

Esse relatório foi uma completa surpresa pra mim! Eu só tinha testado uma view das múltiplas views que eu tinha no arquivo. Como que o relatório chegou a um total de 88% do arquivo sendo coberto por testes?

Eu abri o arquivo do relatório do arquivo que eu havia testado, e ele me mostrava que quase *todas* as Class Based Views estavam sendo testadas, com a única exceção sendo o código que eu havia sobreescrito no `SignupView`:

{{<figure src="/assets/img/posts/cbv-coverage/02.png#center" lt="Uma captura de tela que mostra quase todas as linhas de um arquivo sendo cobertas por testes (em verde)">}}

De novo, fiquei extremamente surpresa! Eu apenas testei a  `HomeView`, porque a `LoginInterfaceView`, `LogoutInterfaceView` e `SignupView` estavam sendo marcadas como testadas?

## Entendendo o que aconteceu

Bem... depois de *dias* buscando uma resposta eu encontrei [essa resposta](https://stackoverflow.com/a/65003581/3538098): 

> *Coverage.py apenas te mostra quais linhas de código foram executadas.*


E um segundo comentário na mesma conversa abre ainda mais os olhos:

> Durante os testes, Django tem que carregar todas as classes e módulos em memória então o programa (suas classes e configurações) são executadas.


O que está acontecendo aqui, é que CBVs são classes, quando você executa os testes, o Django vai carregá-las na memória, o que significa que elas serão executadas assim que o teste começa a rodar. Quando eu rodei o `coverage`, ele procurou quais partes do código foram executadas. Como as classes foram pra memória (foram executadas) elas foram mostradas como testadas.

O método `get` que eu substituí não é executado enquanto os testes são executados, e por isso ele foi marcado como não-testado!

Eu continuo adorando as *Class Based Views*, mas você deve ter cuidado ao usar a biblioteca `coverage` para verificar se você as testou o suficiente!

{{<figure src="[https://media3.giphy.com/media/l4FGyRwwFPBFQt4cg/giphy.gif?cid=ecf05e47rg5zmu35kfsimam8i1s98ohoxujshkq2bwq743fy&rid=giphy.gif&ct=g#center](https://media3.giphy.com/media/l4FGyRwwFPBFQt4cg/giphy.gif?cid=ecf05e47rg5zmu35kfsimam8i1s98ohoxujshkq2bwq743fy&rid=giphy.gif&ct=g#center)" lt="Um gif de um touro em desenho animado no meio de um quarto cheio de porcelana e itens delicados">}}