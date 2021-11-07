---
layout: post
title: "Tutorial passo a passo para criar e publicar seu blog bilíngue - Parte 1"
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
translationKey: blog-step-by-step-I
slug: blog-passo-a-passo-I
date: 2021-08-21T00:25:52+01:00
---

Eu escrevi muitos posts falando sobre como eu acredito que [você deveria ter um blog e escrever nele](https://leportella.com/pt-br/porque-ter-um-blog/). Eu fiz este blog usando nada além de ferramentas gratuitas. A única coisa que eu paguei foi pelo meu domíbio (leportella.com) e eu acho isso incrível! 🤩

Quando eu estava desenvolvendo esse site, eu tive que usar múltiplos tutoriais, um para cada parte. Esse processo pode ser bem complicado, então eu decidi criar esse tutorial, passo-a-passo do começo ao fim!

<!-- more -->

Nesse tutorial vamos abordar os seguintes tópicos:

- Um site funcionando com suporte à múltipas páginas e textos de blog
- Deploy usando Github e Netlify
- Suporte para múltiplas línguas
- Estatísticas
- Configuração de domínio
- Comentários
- Formulário para recebimento de emails

Esse tutorial vai ser dividido em algumas partes:

- **Part 1 - Mínimo exemplo** 
- **Part 2** - [Adicionando uma seção de blog e publicando!](https://leportella.com/pt-br/blog-passo-a-passo-i/)
- **Part 3** - Adicionando comentários
- **Part 4** - Suporte à múltiplas línguas
- **Part 5** - Adicionando um domínio personalizado
- **Part 6** - Adicionando estatísticas
- **Part 7** - Adicionando um formulário para emails

Para ter um website publicado, você só vai precisar seguir as partes 1 e 2. Todas as outras partes são opcionais e você pode segui-las ou não conforme preferir.

Esta é a primeira parte e você vai precisar:

- De um terminal
- Git instalado
- Uma conta no Github

## Instalando Hugo

Neste tutorial eu vou usar [Hugo](https://gohugo.io/), um gerador de site estático de código aberto e escrito em Go. Eu já usei outros geradores antes, mas Hugo é tão fácil e rápido que ele rapidamente virou uma das minhas ferramentas preferidas! 


Eu instalei no meu computador usando brew:

```bash
brew install hugo
```

Se você tiver um sistema diferente do MacOS, [pode checar o guia oficial de instalação](https://gohugo.io/getting-started/installing/).

## Começando um novo projeto

É hora de criar um novo projeto! Nós vamos chamá-lo de `my-blog` (*meu-blog*, em inglês):

```bash
hugo new site my-blog
```

Esse comando irá criar um novo diretório chamado `my-blog`, que contém a infraestrutura básico para o seu site. Nós vamos usar basicamente 3 coisas aqui:


- **content/** : é o diretório que vai conter o conteúdo do seu site, como páginas e posts
- **config.toml**: o arquivo de configuração desse projeto
- **themes/** : é o diretório onde vamos adicionar temas que serão usados no projeto

## Instalando um novo tema

Nosso projeto foi criado mas se tentarmos rodá-lo, só vamos ver uma página em branco. Precisamos de um tema para fazê-lo funcional. 

Você pode criar seu próprio tema do zero, mas Hugo tem uma série de temas prontos para usar! Você pode ir em [https://themes.gohugo.io/](https://themes.gohugo.io/) e escolher o tema que achar melhor! Nesse tutorial eu vou usar um [template minimalista](https://themes.gohugo.io/themes/hugo-theme-codex/) que é bem bonito e fácil de usar 😉

Primeiro precisamos que esse diretório seja um ambiente git:

```bash
git init
```

Agora podemos adicionar o tema como um submódulo dentro da pasta `themes/`:

```bash
git submodule add https://github.com/jakewies/hugo-theme-codex.git themes/hugo-theme-codex
```

Submódulos são uma ferramenta do Git. Eles permitem que você mantenha um repositório Git como um subdiretório de outro repositório Git. Isso significa que os repositórios ficam linkados. Dessa forma, o repositório do tema escolhido pode ser constantemente atualizado com as novas atualizações!

Após rodar esse comando você vai perceber que vai ser criado um novo repositório chamado PaperMod que contém tudo o que precisamos.

## Usando um novo tema

O que precisamos agora é dizer ao Hugo que esse é o tema que vamos usar. No arquivo `config.toml` você vai encontrar algumas definições e nós vamos adicionar o tema ali:

```bash
baseURL = "http://example.org/"
languageCode = "en-us"
title = "My New Hugo Site"

theme = "hugo-theme-codex"
```

## Vamos começar!

Agora vamos criar um novo arquivo, `_index.md`, no diretório `content` e nele vamos adicionar o seguinte:

```yaml
---
heading: "Hi, I'm Codex"
subheading: "A minimal blog theme for hugo."
handle: "hugo-theme-codex"
---
```

Essa vai ser nossa página inicial! Vamos testá-la?

Podemos começar criando nosso servidor rodando o comando:

```bash
hugo server -D
```

Você vai ver que dentro do que é retornado pelo sistema, vai ter uma mensagem com o endereço em que o servidor está rodando:

```bash
Web Server is available at http://localhost:1313/ (bind address 127.0.0.1)
```

Podemos usar um browser pra abrir esse endereço, [http://localhost:1313](http://localhost:1313), e testar nosso site :) 

{{<figure src="/assets/img/posts/step-by-step/01-01.png#center">}}

Uma das coisas que mais me impressionaram é como o Hugo é rápido. Alguns segundos e pronto! Antes de usar ele, eu usava um outro gerador de site estático chamado Jekyll. Meu site tinha mais de 100 posts e o build demorava minutos cada vez que eu queria atualizar e testar uma mudança. Quando eu troquei pro Hugo, passou a demorar segundos!

Você pode deixar esse servidor rodando enquanto trabalha nos arquivos e ele será automaticamente recompilado cada vez que um arquivo for alterado.

E você também vai poder ver algumas estatísticas do que foi considerado na compilação:

```yaml
| EN
-------------------+-----
  Pages            |  3
  Paginator pages  |  0
  Non-page files   |  0
  Static files     |  0
  Processed images |  0
  Aliases          |  0
  Sitemaps         |  1
  Cleaned          |  0
```

## Algumas configurações 

Esse tema tem algumas configurações que permitem que adicionemos links para redes sociais. Por exemplo, vamos adicionar um link para o twitter dentro do arquivo `config.toml` :

```bash
[params]
  twitter = "https://twitter.com/leportella"
```

Esse template em particular tem suporte à uma série de redes sociais e seus ícones. Aqui estão as redes que você pode adicionar ao arquivo de configuração:

```bash
# supported links
twitter = "https://twitter.com/<your handle>"
github = "https://github.com/<your handle>"
email = "mailto:<your email>"
mastodon = "https://mastodon.social/@nickname"
facebook = "https://facebook.com/<your handle>"
gitlab = "https://gitlab.com/<your handle>"
instagram = "https://instagram.com/<your handle>"
linkedin = "<link to your profile>"
youtube = "https://www.youtube.com/channel/<your channel>"

```

Você também pode alterar a posição dos ícones adicionando uma lista chamada `iconOrder`, da seguinte forma:

```bash

iconOrder = [
  "Twitter", 
  "GitHub", 
  "Email", 
  "Mastodon", 
  "Facebook", 
  "GitLab", 
  "Instagram", 
  "LinkedIn", 
  "YouTube",
]
```

Uma vez que você salvar o arquivo, pode já verificar que o site está mostrando o ícone com o link:

{{<figure src="/assets/img/posts/step-by-step/01-02.jpg#center">}}


Yay! Parabéns! Agora você tem uma landing-page! 

## Enviando para o Github!

Agora é hora de garantir que você não vai perder nada! Crie um repositório no Github. Uma vez que tiver o seu link, pode adicioná-lo como o *remote origin* desse repositório local:

```bash
git remote add origin git@github.com:leportella/hugo-blog-example.git
```

Agora é hora de adicionar e commitar:

```bash
git add .
git commit -m "initial commit"
git push origin main
```

Se quiser, [você pode verificar como esse commit ficou no meu repositório de exemplo](https://github.com/leportella/hugo-blog-example/commit/1c2ee29973d390a2e0dc0ba4390b4d48786681f9) 🥰

## Próximos passos

Se você gostou desse tutorial, vá pra parte 2 onde vamos adicionar uma seção de blog e publicar (fazer o deploy) dele!
