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
translationKey: blog-step-by-step-III
slug: blog-passo-a-passo-III
date: 2022-01-30T19:45:52+01:00
---

Este é o terceiro texto sobre como criar seu site passo a passo! Neste texto, eu vou mostrar como você pode receber comentários nos seus textos!

<!--more-->

### **Tabela de conteúdo**

- **Part 1** - [Mínimo exemplo](https://leportella.com/pt-br/blog-passo-a-passo-i/)
- **Part 2** - [Adicionando uma seção de blog e publicando!](https://leportella.com/pt-br/blog-passo-a-passo-ii/)
- **Part 3 - Adicionando comentários**
- **Part 4** - Suporte à múltiplas línguas
- **Part 5** - Adicionando um domínio personalizado
- **Part 6** - Adicionando estatísticas
- **Part 7** - Adicionando um formulário para emails

## Comentários vindo de fábrica!

O Hugo já vem com [suporte para você usar diversas plataformas de comentário](https://gohugo.io/content-management/comments/). Neste tutorial, eu vou usar o  [Disqus](https://disqus.com/) como a plataforma de comentários. Eu tenho usado essa plataforma há muitos anos e ele tem me servido muito bem. Existem algumas alternativas, mas decidi usar a que eu estou mais familiarizada!

## Configurando o Disqus

Uma vez que você criou sua conta, você pode ir no menu na lateral direita e clicar em *Add Disqus To Site*:

{{<figure src="/assets/img/posts/step-by-step/03-01.png#center" lt="">}}

Você vai ser redirecionada para uma página bem cheia de coisas, mas se você rolar pra baixo você consegue encontrar um botão chamado *Get Started* button:

{{<figure src="/assets/img/posts/step-by-step/03-02.png#center" lt="">}}

E aí você pode clicar em *I want to install Disqus on my site*: 

{{<figure src="/assets/img/posts/step-by-step/03-03.png#center" lt="">}}

## Passo 1: defina um id único

Agora vamos começar a configuração específica para o seu site. Você vai precisar criar um ID único que identifique seu site. Isso é o nome que vai no campo *Website Name*:

{{<figure src="/assets/img/posts/step-by-step/03-04.png#center" lt="">}}

Tenha certeza que você escolheu um nome único. Disqus mostra embaixo se o ID não é único e adiciona um número para torná-lo único. O problema é que não é muito óbvio que ele mudou o que você colocou! Fique atenta para ter certeza de qual é o resultado final:

{{<figure src="/assets/img/posts/step-by-step/03-05.png#center" lt="">}}

Anote qual foi o ID único final, vamos precisar dele depois!

## Passo 2: Escolha o plano

O Disqus vai oferecer uma série de planos pagos. Eu selecionei o plano Básico que é gratuito:

{{<figure src="/assets/img/posts/step-by-step/03-06.png#center" lt="">}}

No próximo passo, você deve selecionar qual plataforma você vai usar pro seu blog. Infelizmente, o Hugo não está listado como opção. Não tem problema! Você pode selecionar Jekyll, que é uma ferramenta bem similar. Você vai ver uma tela sobre como instalar, mas pode clicar em *Configure* e seguir pra próxima tela. 

## Passo 3: Mais configurações

Nessa parte, você pode adicionar mais configurações, como o tema (claro ou escuro), nome do site, etc. Você não precisa necessariamente de nada disso, pode deixar tudo branco e seguir em frente. Se quiser voltar depois e preencher tudo, zero problemas :) 


## Passo 4: Defina o estilo de moderação

Finalmente você pode decidir o tipo de moderação que seu site vai ter. Como todas as configurações aqui, você pode alterar isso depois dependendo do que você encontrar pela frente: 

{{<figure src="/assets/img/posts/step-by-step/03-07.png#center" lt="">}}

## Passo 6: Adicione no seu site!

Agora podemos voltar ao arquivo  `config.toml` e adicionar a seguinte linha (usando o ID único que você configurou no passo 1):

```bash
disqusShortname = "my-multilanguage-blog"
```

Se você rodar o Hugo lecalmente e for a qualquer um dos posts, você verá a seguinte mensagem:

{{<figure src="/assets/img/posts/step-by-step/03-08.png#center" lt="">}}

Pode fazer o *commit* da sua única linha de código e dar o *git push* 🙂

```bash
git add config.toml
git commit -m "add disqus"
git push 
```

Assim que o site tiver o deploy completo no Netlify (alguns segundos) [você pode ir ao seu post](https://leportella-hugo-tutorial.netlify.app/blog/my-first-post/) e ver que os comentários estão lá \o/ :

{{<figure src="/assets/img/posts/step-by-step/03-09.png#center" lt="">}}

Prontinho! Você está pronta pra receber comentários nos textos incríveis que você escrever :) Parabéns!