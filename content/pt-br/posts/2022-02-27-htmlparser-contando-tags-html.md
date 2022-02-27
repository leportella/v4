---
layout: post
title: "Contando tags HTML com HTMLParser"
categories:
  - Python
  - tutorial
tags:
  - HTMLParser
  - Python
  - tutorial
  - HTML
  - BeautifulSoup
  - HTML
  - Tags HTML
featured-img: count
img-description: Quadro negro com três riscos em giz
translationKey: htmlparser
slug: contador-htmlparser
date: 2022-02-27T00:00:52+00:00
---

Eu caí em um caso em que queria contar quantas tags que estavam presentes em um arquivo HTML e não queria baixar nenhuma biblioteca (como BeautifulSoup) para fazer isso. Pesquisei online e percebi que poderia usar o HTMLParser para fazer isso.
 <!--more-->
O problema começou quando eu comecei a estudar essa biblioteca e achei ela *muito* pouco intuitiva. Demorei uma eternidade para entender como fazer isso. Vou explicar passo a passo a solução mas você pode pular para o final desse texto para ver o resultado  👾

## Meu problema com o HTMLParser

O problema começou quando a minha primeira intuição foi fazer isso:


```python
from html.parser import HTMLParser

parser = HTMLParser()
parser.feed(html) # html é uma string
```

...e nada aconteceu. Eu dei uma pesquisada no `parser` e não havia nenhum método que pudesse me ajudar a fazer a contagem. Pesquisei online e todos os tutoriais e respostas estavam me dizendo para criar uma nova classe antes, mas não entendi o porquê.

Depois de algum tempo questionando minha sanidade, percebi que esperava que o HTMLParser funcionasse da mesma forma que o BeautifulSoup, que traduz o HTML em uma estrutura na qual posso pesquisar. No entanto, HTMLParser não faz isso. Na verdade, quando eu passo um HTML pro parsers, ele *itera* sobre as tags HTML, mas não *faz* nada com elas. A razão pela qual você precisa implementar uma classe e herdar do HTMLParser é implementar os métodos que de fato vão fazer algo com o HTMLparser!

A razão pela qual eu não fui capaz de *fazer* nada com o analisador uma vez que eu o alimentei com o HTML é porque o HTML é analisado assim que eu passei ele pro `parser`, mas não há nada o que fazer com o `parser` depois disso. Porque eu não implementei nada... Não consegui ver nada!

O que eu precisava fazer na verdade era implementar uma classe e toda vez que encontrava uma nova tag, aumentava um contador... algo assim:

```python
count_h1 = 0 

class MeuHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
    	if tag == 'h1':
        	count_h1 += 1
```

## Solução

Finalmente eu decidi usar o `defaultdict`. O `defaultdict` me permite iniciar um dicionário com um valor padrão, nesse caso 0. Eu só preciso adicionar a contagem cada vez que uma tag estiver presente. A solução final é essa:

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

def contando_tags(html):
  parser = MyHTMLParser()
  parser.feed(html)
  return parser.count
```

O método `handle_starttag` lida com as tags que tem uma tag de abertura e uma tag de fechamento (como `<h1></h1>`) enquanto o método `handle_startendtag` é usado em tags que não precisam de uma segunda tag de fechamento  (como `<link />`).

## Resultado

Se eu pegar um HTML como esse:

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

E passar essa string pela função que acabamode sde criar, o resultado vai ser:

```python
tags = contando_tags(html)
print(tags) # defaultdict(<class 'int'>, {'html': 1, 'head': 1, 'link': 1, 'body': 1, 'nav': 1, 'div': 7, 'a': 5, 'h1': 1, 'h3': 2})
```

E eu posso acessar a contagem de tags da mesma forma que um dicionário comum:

```python
print(tags['html']) # 1
```

E porque usamos o `defaultdict`, nós podemos tentar acessar qualquer tag, mesmo que ela não esteja presente e não vamos ver um erro:

```python
print(tags['h6']) # 0
```

---
*Photo by Miguel Á. Padriñán*
