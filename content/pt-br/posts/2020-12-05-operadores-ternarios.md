---
layout: post
title: "Dando nome às coisas: Operadores ternários"
categories:
  - scala
  - python
  - javascript
  - ruby
  - ciência da computação
  - linguagens de programação
tags:
  - scala
  - python
  - javascript
  - ruby
  - ciência da computação
  - linguagens de programação
  - operadores ternários
  - nomeando coisas
featured-img: tag
slug: ternary-operators
date: 2020-12-05T08:28:52-03:00
---

Uma coisa que eu sempre digo que é difícil ao aprender ciência da computação sozinha, é não saber o que você não sabe. Hoje eu aprendi o nome de alguns conceitos que vou compartilhar, para que as pessoas saibam que elas existem 😊

Quando comecei a estudar Python, se uma nova variável dependesse de outra variável booleana, eu escreveria algo assim:

```python
uma_variavel_booleana = True
if uma_variavel_booleana:
    nova_variavel = 1
else:
    nova_variavel = 2
```

Quando eu fui aprender Scala, toda vez que eu caia num caso semelhante eu tentava fazer a mesma coisa, mas aprendi o jeito mais adequado era fazer isso

```scala
val umaVariavelBooleana = true
val novaVariavel = if (umaVariavelBooleana) 1 else 2
```

Eu então descobri que no JavaScript (and Ruby), eu poderia fazer isso:

```scala
val umaVariavelBooleana = true
val novaVariavel = umaVariavelBooleana ? "retorne se true" : "retorne se false" 
```

O símbolo `?` irá verificar se a expressão anterior é verdadeira ou falsa. Se for verdadeira, ele retornará o primeiro valor após ele, se for falsa, ele retornará o valor após o símbolo `:` .

Eu não tinha nenhuma ideia de que esse tipo de expressão, de verificação booleana de uma linha só,  tinha um nome: [Operadores Ternários](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Reference/Operators/Operador_Condicional).

Eu sei que parece super simples escrever um texto inteiro só sobre isso, mas um dos principais problemas de não saber como algo é chamado é que fica muito difícil procurá-lo em uma nova linguagem de programação! Agora, na próxima linguagem de programação que eu começar a estudar, posso procurar por "operadores ternários em X". Saber o nome torna muito mais fácil entender o conceito e extrapolá-lo!

E pra minha completa surpresa, eu acabei descobrindo que Python também tem uma maneira de usar operadores ternários! 

```python
nova_variavel = 1 if uma_variavel_booleana else 2
```

Espero que tenha aprendido algo novo hoje!

---

Photo by Brett Jordan from Pexels

---
