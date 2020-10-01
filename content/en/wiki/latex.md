---
title: "Latex"
date: 2020-10-01T16:59:37+01:00
last_mod: 2020-10-01T16:59:37+01:00
draft: false
---

## Minimum working example

```latex
% mydoc.tex
\documentclass[12pt,openany]{memoir}
\usepackage{graphicx}                      % allow images
\usepackage{float}                         % image location ([H])

\title{My LaTeX book}
\author{Leticia Portella}

% ============= DOCUMENT =================
\begin{document}
\maketitle

\include{chapter1}

\bibliography{mydoc}                       % bib file 
\bibliographystyle{plain} 

\end{document}
```

```latex
% mydoc.bib

@book{Armour,                                         % Armour will be the id 
  author    = "P. G. Armour",
  title     = "The Laws of Software Process",
  publisher = "Auerbach",
  year      = "2003",
}
```

```latex
% chapter1.tex
\chapter{My first chapter}

As written by \cite{Armour}...
```