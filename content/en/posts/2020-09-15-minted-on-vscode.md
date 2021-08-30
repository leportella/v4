---
layout: post
title: "Configuring VSCode to work with Minted (LaTeX)"
categories:
  - latex
tags:
  - blog
  - blogging
  - tech blog
  - writing
  - tech writing
  - technical post
  - technical article
  - technical writing
  - latex
  - minted
  - vscode
featured-img: engrenagem
img-descritiong: A photo with lots of golden engine pieces
slug: minted-vscode
translationKey: minted
last_mod: 2020-09-15T18:25:52-05:00
date: 2020-09-15T18:25:52-05:00
---

I was handling some LaTeX files and I needed code coloring. I found the package [minted](https://www.ctan.org/pkg/minted) and it seemed perfect, but it required a couple of things that made my life a bit more complicated on VSCode.
<!--more-->


## Installing the package

I installed the package as normally you would in LaTeX:

```latex
\usepackage{minted}                        % code color
```

The problem is that minted require Python 2.7 and a package call Pygments. So I created a virtualenv using Python 2.7 and added the packaged using pip

```latex
pip install Pygments
```

## VSCode went crazy now...

The problem is that this broke my VSCode setup, because `minted` required me to add `--shell-escape` to the pdflatex, and the default way of running LaTeX of VSCode didn't include that. Because of that, my document that was all nice and compiling when I ran on the terminal, was resulting in this:

{{<figure src="/assets/img/posts/minted2.png#center" alt="A screenshot of the VSCode interface showing several problems listed where the first is: Package minted you must invoke Latex with the shell-escape flag">}}

And VSCode went crazy and showed a lot of errors when automatically compiling:

{{<figure src="/assets/img/posts/minted1.png#center" alt="A screenshot of the VSCode interface showing an error with the message Package minted you must have pygmentize installed to use this package">}}

## Let's fix VSCode

So I went to `Code > Preferences > Settings > Extensions` and rolled until the end to get to a configuration that said Edit in `settings.json` and added the following configuration:

```latex
"latex-workshop.latex.tools": [
        {
            "name": "latexmk",
            "command": "latexmk",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "-outdir=%OUTDIR%",
                "%DOC%"
            ]
        },
        {
            "name": "pdflatex",
            "command": "pdflatex",
            "args": [
                "--shell-escape",
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "%DOC%"
            ]
        },
        {
            "name": "bibtex",
            "command": "bibtex",
            "args": [
                "%DOCFILE%"
            ]
        }
    ]
```

Also wanted VSCode to run within my virtualenv, so on extensions, I added the Python extension. 

{{<figure src="/assets/img/posts/minted3.png#center" alt="A screenshot showing VSCode extension marketplace with a filter for Python extensions.">}}

Once installed I used `Cmd+Shift+P` and  used `Select Interpreter` to select my current virtualenv.

{{<figure src="/assets/img/posts/minted4.png#center" alt="A screenshot showing how to select the Python Interpreter in the VSCode interface">}}

Now I got no errors and the VSCode is happy again:

{{<figure src="/assets/img/posts/minted5.png#center" alt="A screenshot showing how VSCode displays the selected Python interpreter on the lower area of its interface">}}

## Using it!


Now I can add any language the package supports and some additional configuration! For instance, in here `linenos` will add line numbers ;)


```latex
\begin{minted}[linenos]{python}
  for i in range(0,2):
      print(i)
\end{minted}
```


PS 1: Yes, I created a virtualenv called banana but I was lazy to create cute one for this tutorial 🥺

PS 2: I used miniconda to create this venv and VSCode required some extra config for this but they had a pop for this and did it automatically 

That's it for now 😉


--
*This post includes and expands [Wu Sun's post](https://wusun.name/blog/2019-01-17-minted-vscode/) that was super helpful to me*

-- 
*Image cover by Miguel Á. Padriñan in Pexels*