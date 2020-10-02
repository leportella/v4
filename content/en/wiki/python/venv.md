---
title: "Venv"
date: 2020-10-02T12:08:36+01:00
last_mod: 2020-10-02T12:08:36+01:00
---

## Create a venv with python3

```bash
python3 -m venv MyFirstVenv
```

## Create a venv with conda

```bash
conda create -n MyFirstVenv python=2.7
```

## Understanding VirtualEnvs

[Virtualenv](https://virtualenv.pypa.io/en/latest/) is a Python tool developed to isolate development environments. It is really handy when you need to isolate projects that use different versions of Python and packages. It is specially good if you consider that some operational systems use Python as a default tool. Imagine that your system uses a specific library with a specific version. Change it can cause severe complications on your whole system. So, you definetely should be careful.

Imagine that your computer (and operational system) is a huge box that has a lot of packages:

{{<figure src="/assets/img/posts/venv2.png#center" width="400px">}}

*Your operational system is like a box, with a specific version of Python and the Python libraries it needs, which specific versions it needs.*


Creating a virtualenv is like you created a "little box", and inside it you can install whatever you eant: any version of Python and any version of the libraries you need. Since you created a "little box", what's in it is completely isolated from your general environment, and it can be easily deleted if you stop working on that project.

{{<figure src="/assets/img/posts/venv1.png#center" width="400px">}}
*Example on how a virtualenv is a "little box" inside the "big box" that is your operational system*


Since you can create multiple virtualenvs, each project can (and normally should) have its own "box", making easier to manage packages and libraries for each project, always keeping your operational system intact.

{{<figure src="/assets/img/posts/venv3.png#center" width="400px">}}
*You can have as many virtualenv as you like inside your operational system.*