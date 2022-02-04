---
layout: post
title: "Tutorial passo a passo para criar e publicar seu blog bilíngue - Parte 2"
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
translationKey: blog-step-by-step-II
slug: blog-passo-a-passo-II
date: 2021-08-28T00:25:52+01:00
---

Este é o segundo post sobre como criar seu site passo a passo!

<!--more-->


**Tabela de conteúdo**

- [Part 1 - Mínimo exemplo](https://leportella.com/pt-br/blog-passo-a-passo-i/)
- **Part 2 - Adicionando uma seção de blog e publicando!**
- [Part 3 - Adicionando comentários](https://leportella.com/pt-br/blog-passo-a-passo-iii/)
- [Part 4 - Suporte à múltiplas línguas](https://leportella.com/pt-br/blog-passo-a-passo-iv/)
- Part 5 - Adicionando um domínio personalizado
- Part 6 - Adicionando estatísticas
- Part 7 - Adicionando um formulário para emails

Nesta parte você vai precisar: 

- Uma conta no [Netlify](https://www.netlify.com/)

## Primeiro texto no blog

No último post, nós criamos uma *landing page* mas que tal adicionarmos uma seção de blog?

Nós podemos criar um diretório chamado `blog`  usando o seguinte comando:

```bash
hugo new blog/my-first-post.md
```

Se você abrir este novo arquivo, você pode ver que ele contém algumas informações básicas:

```bash
---
title: "My First Post"
date: 2021-08-14T14:59:13+01:00
draft: true
---

This is my first blog post!
```

Estas informações são metadados do texto. Qualquer coisa adicionada entre os `---`  não será mostrada no texto. O texto do blog deve ser escrito justamente depois do segundo `---`. 

Se salvarmos esse arquivo, não conseguimos ver nada de diferente! Como fazer? Ainda não temos um menu, mas se acessarmos `/blog` nós podemos ver uma listagem e esse nosso texto já está disponível lá!

{{<figure src="/assets/img/posts/step-by-step/02-01.png#center" alt="Uma captura de tela de uma tela em branco com a data, Agosto 14 2021 e um grande titulo escrito My First Post">}}

## Vamos adicionar um menu!

Agora que sabemos qual o link pros nossos textos, precisamos criar um menu para que outras pessoas possam acessá-lo. Nós podemos fazer isso adicionando a seguinte configuração no arquivo  `config.toml`:

```bash
[[menu.main]]
  identifier = "blog"
  name = "blog"
  title = "Blog"
  url = "/blog"
```

Agora se nós checarmos o nosso site de novo, podemos ver que apareceu um menu na parte esquerda do site:

{{<figure src="/assets/img/posts/step-by-step/02-02.png#center" alt="Uma captura de tela de uma tela em branco om a data, Agosto 14 2021 e um grande titulo escrito My First Post. Na lateral esquerda tem a palavra blog que é um link de menu que redireciona para a listagem de textos.">}}

*🚨 Atenção: Você precisa muder de `draft: true` para `draft: false` ou a listagem não vai funcionar porque o sistema não vai ter nenhum artigo publicado (que não seja rascunho).* 



## Entendendo como a pasta content/ funciona

Por enquanto temos 2 coisas dentro da pasta `content/`: um arquivo, `_index.md`, e um diretório chamado `blog/`. Independente de onde ele fica, cada arquivo representa uma página do site. Neste caso o tema que estamos usando usa o arquivo `_index.md` como base para a página principal, mas podemos criar uma nova página para uma seção  *Sobre mim* (About), por exemplo:

```bash
hugo new about.md
```

Você pode acessar essa página no  `/about`.

Agora, se ao invés de um único arquivo você criar uma pasta chamada `portifolio`, e adicionar um arquivo para um projeto:

```bash
hugo new portifolio/my-first-project.md
```

E tentar acessar o link  `/portifolio`, você vai perceber que essa nova página também apresenta uma listagem, igual ao que acontece ao link  `/blog`. 

Dessa forma no Hugo, cada diretório vai gerar uma página de listagem de arquivos enquanto que cada arquivo vai gerar uma página. Agora que você sabe como criar páginas e listagens e como adicioná-las no menu lateral você pode modelar o site pra ficar do jeito que você quiser!

Adicione as mudanças num commit e garanta que elas vão para o repositório remoto do Github!

## Vamos publicar!

É hora de acessar sua conta do [Netlify](https://www.netlify.com/) . Uma vez que você tenha ela configurada, você pode ir em  *Sites* e daí clicar em *New site from Git.*

{{<figure src="/assets/img/posts/step-by-step/02-03.png#center" alt="Uma captura de tela do sistema da Netlify. Tem várias abas na parte superior e no canto direito um botão verde escrito New site from Git">}}

Selecione Github (se você estiver usando) e selecione o repositório que contém o código do seu site. 

{{<figure src="/assets/img/posts/step-by-step/02-04.png#center" alt="Uma captura de tela do sistem da Netlify one você pode associar um repositório do Git com esse sistema.">}}

🚨*Atenção: se você não vê o repositório que deseja aqui, pode ser que você não tenha autorizado o Netlify a acessar ele. [Vá neste link](https://github.com/apps/netlify/installations/new) e configure corretamente.* 

Na última etapa podemos deixar todas as configurações com os valores originais. Clique no botão *Deploy site* e pronto!

## Dando um nome apropriado

Como você pode ver, o seu site foi publicado mas com um nome aleatório. Você pode acessá-lo agora para verificar se deu tudo certo!

{{<figure src="/assets/img/posts/step-by-step/02-05.png#center" alt="Uma captura de tela do sistema da Netlify mostrando um nome aleatório que foi dado para o seu site assim que ele foi publicado. Na parte inferior é possível ver dois botões: Site settings e Domain settings">}}

Legal, não? Mas esse nome não é muito bonito. Você pode clicar em *Site Settings* e depois *Change site name* e finalmente escolher um nome mais apropriado. O nome que você escolher vai ter o domínio  `.netlify.app` junto. Se você quiser, pode checar o meu: [leportella-hugo-tutorial.netlify.app](http://leportella-hugo-tutorial.netlify.app) 🤩

## Checando as publicações

No menu superior, você pode clicar na aba *Deploys*. Nessa seção você pode ver a listagem de publicações e o status delas. Toda vez que você mandar um commit pro repositório remoto, ele vai aparecer aqui e gerar um deploy novo. Você também pode iniciar uma publicação manualmente se você quiser!

{{<figure src="/assets/img/posts/step-by-step/02-06.png#center" alt="Uma captura de tela do sistema da Netlify mostrando o status dos últimos deploys onde tem apenas um deploy. Nele tem um cartão verde mostrando que o site foi publicado com sucesso e ao lado direito a data da publicação. ">}}


## Pera... onde estão as imagens?

Se você abrir o seu site você vai ver que o ícone do Twitter não está aparecendo. Se você inspecionar o site você vai ver que o SVG está sendo obtido de `https://example.org/svg/twitter.svg`. Isso não está nada certo!

{{<figure src="/assets/img/posts/step-by-step/02-07.png#center" alt="A screenshot from the website with the inspector open and selecting an empty image with the url https://example.org/svg/twitter.svg">}}

Agora que o seu site já tem uma URL do netlify precisavmos mudar a configuração do baseURL no seu arquivo de configuração config.toml:

```
baseURL = "https://leportella-hugo-tutorial.netlify.app"
```

Uma vez que você faça o commit disso, o deploy será acionado e tudo funcionará :)  


## Próximos passos

Como pode ver, é bem simples para criar um site e um blog simples. No entanto, ainda tem um monte de coisas que você pode personalizar! Todos os próximos passos desse tutorial são opcionais, você pode escolher os que quiser!

Como sempre, você pode ver todo o código (commit por commit) [no meu repositório de exemplo](https://github.com/leportella/hugo-blog-example/).