
---
layout: post
title: "The complete step-by-step guide to create and deploy your multi-language website - Part 4"
categories:
  - open-source
  - blog
  - tutorial
tags:
  - open-source
  - blog
  - tutorial
  - hugo
  - disqus
featured-img: staircase
img-description: A black and white picture of a staircase over a white wall
translationKey: blog-step-by-step-IV
slug: blog-step-by-step-IV
date: 2022-02-10T14:26:52+01:00
---

This is the forth post on how to create your website step by step! 

<!--more-->

**Table of content for the whole tutorial**

- [Part 1 - Minimum working example](https://leportella.com/blog-step-by-step-i/)
- [Part 2 - Adding a blog section and deploy it!](https://leportella.com/blog-step-by-step-ii/)
- [Part 3 - Adding comments](https://leportella.com/blog-step-by-step-iii/)
- **Part 4 - Multi-language support**
- Part 5 - Adding a personalized domain
- Part 6 - Adding statistics
- Part 7 - Adding a email inbound section

## Why add multi-language support?

I always tell people that learning to speak English in a country that is not English speaking is usually a huge privilege. Being able to create great content in different languages is something that can help many people to get in the technology world and give them opportunities they might not have otherwise. Because of that, I always had my posts translated (to the best of my abilities) and having a multi-language support was something critical to my website.

With Hugo, I was able to do this so easily that I really fell in love with it. So... are you ready to add multi-language support to your website? In the examples below I will use Portuguese as the second language since it's my native language 😊 

{{<figure src="https://media3.giphy.com/media/1wmOUUYKe1CpOLFjE3/giphy.gif?cid=ecf05e47fhts5iygmniw661ehmeopqlucv5c8d7h2o07j49j&rid=giphy.gif#center" lt="A gif of a puppet horse wearing the Brazilian soccer t-shirt and a flag from Brazil">}}

## Reorganize the content folder

First we need to  create a new folder inside the `/content` called `en` and move all files that were in the `/content` folder to `/content/en` folder. The idea here is that for every new language you will add support to your website, you will have a folder for it. 

This is what we had until now:

```bash
|____content
| |____blog
| | |____my-first-post.md
| |____about.md
| |_____index.md
```

This is what we should have now:

```bash
|____content
| |____en
| | |____blog
| | | |____my-first-post.md
| | |____about.md
| | |_____index.md
```

## Changes in `config.toml`

Now we need to tell Hugo that our website content is language aware, and we need to add support for the English language like this on the `config.tml`:

```bash
[languages]
  [languages.en]
    weight = 1
    contentDir = "content/en"
    languageName = "English"
```

In here we are basically telling Hugo that English is the priority language (`weigth = 1`) and that the files will be found in the `/content/en` folder we just created.

If you run the server now, you should find out that nothing changed and everything is working just fine! 

## Adapting the left menu

The left menu should be language aware as well, so we need to move from this:

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

To this:

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

Again, if you check your website nothing will change until now but Hugo is now completely aware of language! 

## Now let's add a new language!

Right now we are completely ready to add a new language! Let's go back to the  `/content` folder, add a new folder with the language you want. In this case, we will use `pt-br` (Brazilian Portuguese) as the secondary language of our website:

```bash
mkdir content/pt-br
```

Let's copy the `_index.md` file from the English folder to the Portuguese folder:

```bash
cp content/en/_index.md content/pt-br
```

And we can translate the `/content/pt-br/_index.md` with the new language. Make sure you only translate the *values* and not the *keys*: 

```bash
heading: "Olá, Eu sou o Codex"
subheading: "Este é um tema minimalista"
handle: "hugo-theme-codex-em-portugues!"
```

And finally, we can copy the blog folder:

```bash
cp -r content/en/blog content/pt-br
```

And since we only have one blog post, we quickly translate it to Portuguese:

```bash
---
title: "Meu primeiro post!"
date: 2021-08-14T14:59:13+01:00
draft: false
---

Este é meu primeiro post!
```

Almost there! The last thing we need to do is tell Hugo that we have an additional language onboard! We can do that by basically copying the English configuration on `config.toml` . Since English was the preference language, we can assign `weight = 2` to Portuguese:

```bash
[languages.pt-br]
    weight = 2
    contentDir = "content/pt-br"
    languageName = "Português"
    twitter = "https://twitter.com/leportella"
```

We may also change the lateral menu and instead of a simple `blog` we can say `meu blog` (my blog), so users know this is the list of the Portuguese versions of the posts:

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

If we now access the website but add a `/pt-br` at the end of it we can see that the names are now translated! You can see that both the menu and the main title was translated using the names defined in the `config.toml` :

{{<figure src="/assets/img/posts/step-by-step/04-01.png#center" lt="">}}


And if we click the *meu blog*  menu, you'll get redirected to the portuguese list of blog posts!

{{<figure src="/assets/img/posts/step-by-step/04-02.png#center" lt="">}}

## Lateral menus

Now we need to be able to access the menu of other languages! So you can add a link to the Portuguese version on the English menu and vice versa, to users can change the language seamlessly.

So first we need add weight  to the menus we already have. Since blog links should be priority, we will add `weight = 1`  to both of them:

 

```bash
[languages]
  [languages.en]
    weight = 1
    contentDir = "content/en"
    languageName = "English"
    twitter = "https://twitter.com/leportella"     
[[languages.en.menu.main]]
    weight = 1
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
     weight = 1
     identifier = "blog"
     name = "meu blog"
     title = "Blog"
     url = "/pt-br/blog"
```

Now we can add the menu to each . In the english menu we want users to be able to move to the Portuguese website. Since this is not the priority, we should add a `weight = 2` to this menu:

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

Now let's add the link to the English website in the Portuguese menu:

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

This is the result for the English version:

{{<figure src="/assets/img/posts/step-by-step/04-03.png#center" lt="">}}

And the result for the Portuguese version:

{{<figure src="/assets/img/posts/step-by-step/04-04.png#center" lt="">}}

That's it! Now you have a bilingual website and know how to add as many languages as you want!