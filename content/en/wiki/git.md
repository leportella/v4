---
layout: post
title: "Git"
slug: git
page-description: A cheatsheet of useful git commands
aliases: 
  - /cheatsheet-git.html
  - /cheatlist/2018/01/05/git-cheat-list.html
date: 2018-01-05T14:25:52-05:00
---


## Undo commits

1 commit: 

```bash
$ git reset HEAD~ 
```

2 commits

```bash
$ git reset HEAD~~ 
```


## How to rebase a forked repository

On the cloned repository

```bash
$ git checkout master
$ git remote add upstream git@github.com.../other/repo.git
$ git fetch upstream
$ git rebase upstream/master
$ git checkout my-branch
$ git rebase master
```

## How to add a default editor to git

```bash
$ git config --global core.editor vim
```

## Delete changes on conflict while rebasing

If you generated an automatic file, pushed it but then there was a conflict because the file was updated by someone else, sometimes the easiest thing is to just throw away your changes and run the script again. To do that while you are rebasing you just

```bash
$ git rebase master

... CONFLICT: file.ext

$ git checkout file.ext
$ git add file.ext

$ run_automatic_script
```


## How to amend to some old commit?

```bash
$ git log
```

Get the hash of the commit you wish to edit

```bash
$ git rebase -i 123456
```

It will open your editor with the commit options written as *pick*

{{<figure src="https://i.imgur.com/6jbkv2b.png#center">}}

Change it to *edit*

{{<figure src="https://i.imgur.com/vbPbIAe.png#center">}}

Your branch name is now changed to the commit's hash. Edit your files then:

```bash
$ git add yourfile
$ git commit --amend
```

Once you have finished all changes:

```bash
$ git rebase --continue 
```

Everything is back to normal. Since you made a rebase, you need a "forced" push:

```bash
$ git push -f 
```

## How to amend delete merged branches?

This delete all merged branch. Do NOT use `-D`.

```bash
$ for branch in `git branch | grep -v master`; do git branch -d $branch; done
```