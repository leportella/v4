---
layout: post
title: "Git - My Cheat Sheet"
categories:
  - english
  - cheatsheet
tags:
  - en
  - python
  - git
  - cheatlist
  - python
  - community 
  - pyladies
  - technology
  - tecnologia
  - programador
  - programadora
  - developer
  - mulheres na tecnologia
  - woman in tech
  - girls in tech
  - computação
  - ciência de computação
  - software development
  - software engineering
  - engenharia de software
  - desenvolvimento
  - auto-ensino
  - self-taught engineer
  - code
  - Django
  - software
  - career
  - tech career
  - open-source
  - no cs degree
  - cs
  - computer science
featured-img: code
slug: git
aliases: 
  - /cheatsheet-git.html
  - /cheatlist/2018/01/05/git-cheat-list.html
date: 2018-01-05T14:25:52-05:00
---


## Undo commits

1 commit: 

```
$ git reset HEAD~ 
```

2 commits

```
$ git reset HEAD~~ 
```

## How to rebase a forked repository

On the cloned repository

```
$ git checkout master
$ git remote add upstream git@github.com.../other/repo.git
$ git fetch upstream
$ git rebase upstream/master
$ git checkout my-branch
$ git rebase master
```

## How to add a default editor to git

```
$ git config --global core.editor vim
```

## Delete changes on conflict while rebasing

If you generated an automatic file, pushed it but then there was a conflict because the file was updated by someone else, sometimes the easiest thing is to just throw away your changes and run the script again. To do that while you are rebasing you just

```
$ git rebase master

... CONFLICT: file.ext

$ git checkout file.ext
$ git add file.ext

$ run_automatic_script
```


## How to amend to some old commit?

```
$ git log
```

Get the hash of the commit you wish to edit

```
$ git rebase -i 123456
```

It will open your editor with the commit options written as *pick*

{{<figure src="https://i.imgur.com/6jbkv2b.png#center">}}

Change it to *edit*

{{<figure src="https://i.imgur.com/vbPbIAe.png#center">}}

Your branch name is now changed to the commit's hash. Edit your files then:

```
$ git add yourfile
$ git commit --amend
```

Once you have finished all changes:

```
$ git rebase --continue 
```

Everything is back to normal. Since you made a rebase, you need a "forced" push:

```
$ git push -f 
```



## How to amend delete merged branches?

This delete all merged branch. Do NOT use `-D`.

```
$ for branch in `git branch | grep -v master`; do git branch -d $branch; done
```