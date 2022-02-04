---
layout: post
title: "Tutorial passo a passo para criar e publicar seu blog bilíngue - Parte 4"
categories:
  - open-source
  - blog
  - tutorial
tags:
  - open-source
  - blog
  - tutorial
featured-img: staircase
img-description: Uma imagem preto e branco de uma escada sob um fundo branco
translationKey: blog-step-by-step-IV
slug: blog-passo-a-passo-IV
date: 2022-02-10T19:45:52+01:00
---

Este é o quarto texto sobre como criar seu site passo a passo. Neste texto vamos tornar o site bilíngue!

<!--more-->

**Tabela de conteúdo**

- [Part 1 - Mínimo exemplo](https://leportella.com/pt-br/blog-passo-a-passo-i/)
- [Part 2 - Adicionando uma seção de blog e publicando!](https://leportella.com/pt-br/blog-passo-a-passo-ii/)
- [Part 3 - Adicionando comentários](https://leportella.com/pt-br/blog-passo-a-passo-iii/)
- **Part 4 - Suporte à múltiplas línguas**
- Part 5 - Adicionando um domínio personalizado
- Part 6 - Adicionando estatísticas
- Part 7 - Adicionando um formulário para emails

## Porque adicionar suporte à múltiplas línguas?

Eu sempre digo às pessoas que aprender a falar inglês em um país em que inglês não é a língua nativa geralmente é um grande privilégio. Ser capaz de criar um ótimo conteúdo em diferentes idiomas é algo que pode ajudar muitas pessoas a entrar no mundo da tecnologia e dar a elas oportunidades que talvez não tivessem de outra forma. Por isso, sempre tive meus posts traduzidos (com o melhor de minhas habilidades) e ter um suporte multilíngue foi algo fundamental para o meu site.


Com Hugo, eu consegui fazer isso com tanta facilidade que me deixou perplexa! Então... você está pronta para adicionar suporte multilíngue ao seu site? Como partimos nos textos anteriores pela língua inglesa, nos exemplos abaixo vou usar o português como segunda língua 😊


{{<figure src="https://media3.giphy.com/media/1wmOUUYKe1CpOLFjE3/giphy.gif?cid=ecf05e47fhts5iygmniw661ehmeopqlucv5c8d7h2o07j49j&rid=giphy.gif#center" lt="A gif of a puppet horse wearing the Brazilian soccer t-shirt and a flag from Brazil">}}

## Reorganizando o diretório de conteúdo 

Primeiro precisamos criar uma nova pasta dentro do diretório `/content` chamada `en` e vamos mover todos os arquivos e pastas do diretório `/content` para o novo diretório `/content/en`. A ideia é que para cara nova língua nós adicionemos uma pasta específica . 

A estrutura que tínhamos até agora era:

```bash
|____content
| |____blog
| | |____my-first-post.md
| |____about.md
| |_____index.md
```

Essa é a nova estrutura que vamos ter:

```bash
|____content
| |____en
| | |____blog
| | | |____my-first-post.md
| | |____about.md
| | |_____index.md
```

## Mudanças no `config.toml`

Agora precisamos dizer ao Hugo que o formato interno do nosso site está um pouco diferente, então precisamos adicionar a seguinte configuração no `config.tml`:

```bash
[languages]
  [languages.en]
    weight = 1
    contentDir = "content/en"
    languageName = "English"
```

Aqui estamos basicamente dizendo ao Hugo que inglês é a primeira língua do site (`weigth = 1`) e que os arquivos estarão dentro do diretório `/content/en` que acabamos de criar. 

Se você rodar o servidor agora deve ver que nada mudou e tudo ainda funciona perfeitamente!

## Adaptando o menu esquerdo 

O menu da lateral esquerda também pode ficar configurado por língua, então você precisa mudar do formato atual:

```bash
[[menu.main]]
 identifier = "blog"
 name = "blog"
 title = "Blog"
 url = "/blog"

[languages]
  [languages.en]
    weight = 1
    contentDir = "content/en"
    languageName = "English"
```

Para o seguinte:

```bash
[languages]
  [languages.en]
    weight = 1
    contentDir = "content/en"
    languageName = "English"
    twitter = "https://twitter.com/leportella"     
[[languages.en.menu.main]]
     identifier = "blog"
     name = "blog"
     title = "Blog"
     url = "/blog"
```

De novo, essa mudança não vai alterar nada no site. Nós simplesmente estamos mudando a organização interna, fazendo como que o Hugo esteja ciente que o site está formatado para uma determinada língua.

## Hora de adicionar uma nova língua!

Agora estamos completamente prontas para adicionar um novo idioma! Vamos voltar para a pasta `/content`, e adicionar uma nova pasta com o idioma desejado. Neste caso, usaremos `pt-br` para identificar que o conteúdo vai ser em português:

```bash
mkdir content/pt-br
```

Vamos também copiar o arquivo `_index.md` da pasta de inglês para a pasta de português:

```bash
cp content/en/_index.md content/pt-br
```

E agora podemos traduzir o arquivo `/content/pt-br/_index.md` para a nova língua. Cuidado para traduzir apenas os *valores* e não as *chaves*: 

```bash
heading: "Olá, Eu sou o Codex"
subheading: "Este é um tema minimalista"
handle: "hugo-theme-codex-em-portugues!"
```

Finalmente, vamos copiar a pasta com o conteúdo do blog:

```bash
cp -r content/en/blog content/pt-br
```

E já que só temos um texto, podemos rapidamente traduzi-lo para português:

```bash
---
title: "Meu primeiro post!"
date: 2021-08-14T14:59:13+01:00
draft: false
---

Este é meu primeiro post!
```

Quase lá! A última coisa que precisamos fazer é dizer ao Hugo que temos um idioma adicional a bordo! Podemos fazer isso copiando a configuração em inglês em `config.toml` . Como o inglês foi o idioma de preferência, podemos atribuir `weight = 2` ao português:

```bash
[languages.pt-br]
    weight = 2
    contentDir = "content/pt-br"
    languageName = "Português"
    twitter = "https://twitter.com/leportella"
```

Podemos também alterar o menu lateral e ao invés de um simples `blog` podemos colocar `meu blog` para que os usuários saibam que esta é a lista das versões em português dos textos:

```bash
[languages.pt-br]
    weight = 2
    contentDir = "content/pt-br"
    languageName = "Português"
    twitter = "https://twitter.com/leportella"
  [[languages.pt-br.menu.main]]
     identifier = "blog"
     name = "meu blog"
     title = "Blog"
     url = "/pt-br/blog
```

Se agora acessarmos o site e adicionarmos um `/pt-br` na URL, veremos que os nomes já estão traduzidos! Você pode ver que tanto o menu quanto o título principal foram traduzidos usando os nomes definidos no `config.toml` :

{{<figure src="/assets/img/posts/step-by-step/04-01.png#center" lt="">}}


E se você clicar em *meu blog* você verá apenas a listagem de textos em português:

{{<figure src="/assets/img/posts/step-by-step/04-02.png#center" lt="">}}

## Menus laterais

Agora precisamos de uma maneira de acessar o menu de outros idiomas. Você pode adicionar um link para a versão em português no menu em inglês e vice-versa, para que os usuários possam alterar o idioma sem problemas. 

Então, primeiro precisamos adicionar peso aos menus que já temos. Como os links do blog devem ser prioritários, adicionaremos `weight = 1` a ambos:



```bash
[languages]
  [languages.en]
    weight = 1
    contentDir = "content/en"
    languageName = "English"
    twitter = "https://twitter.com/leportella"     
[[languages.en.menu.main]]
    **weight = 1**
    identifier = "blog"
    name = "blog"
    title = "Blog"                                   
    url = "/blog"

  [languages.pt-br]
    weight = 1
    contentDir = "content/pt-br"
    languageName = "Português"
    twitter = "https://twitter.com/leportella"
  [[languages.pt-br.menu.main]]
     **weight = 1**
     identifier = "blog"
     name = "meu blog"
     title = "Blog"
     url = "/pt-br/blog"
```

Agora podemos adicionar o menu da outra língua em cada configuração. No menu em inglês queremos que os usuários possam passar para o site em português. Como esta não é a prioridade, devemos adicionar um `weight = 2` a este menu:

```bash
[[languages.en.menu.main]]
    weight = 1
    identifier = "blog"
    name = "blog"
    title = "Blog"                                   
    url = "/blog"
  [[languages.en.menu.main]]
    weight = 2
    identifier = "pt"
    name = "🇧🇷 Pt"
    title = "Português"
    url = "/pt-br"
```

Agora podemos adicionar o link para o site em inglês no menu em português:

```bash
[[languages.pt-br.menu.main]]
    weight = 1
    identifier = "blog"
    name = "meu blog"
    title = "Blog"
    url = "/pt-br/blog"
  [[languages.pt-br.menu.main]]
    weight = 2
    identifier = "en"
    name = "🇮🇪 En"
    title = "English"
    url = "/"
```

Esse é o resultado do site em inglês:

{{<figure src="/assets/img/posts/step-by-step/04-03.png#center" lt="">}}

E o resultado para a versão em português:

{{<figure src="/assets/img/posts/step-by-step/04-04.png#center" lt="">}}

Prontinho! Agora você tem um site bilíngue e sabe como adicionar quantos idiomas quiser!