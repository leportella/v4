---
layout: post
title: "O que fazer quando faltam dados?"
categories:
  - ciência de dados
tags:
  - ciência de dados
  - interpolação
  - dados
  - dados ausentes
  - python
  - pandas
featured-img: interp
slug: dados-ausentes
aliases: 
  - /pt-br/2018/12/27/o-que-fazer-quando-faltam-dados.html
date: 2018-12-27T11:10:52-05:00
last_mod: 2019-01-02T11:10:52-05:00
translationKey: missing-data
---


Podemos dividir, de forma bastante grosseira, qualquer tipo de dado em duas categorias: temporais e atemporais. Dados atemporais são bastante comuns nos datasets mais utilizados nos tutoriais de ciência de dados: as características dos sobreviventes do Titanic, os tamanhos de pétalas de flores ou as características de um tumor. <!--more-->Estes, podem ter dados temporais, como o momento em que o usuário tomou uma determinada atitude, mas o dado temporal é uma característica secundária, não sua essência.

Os dados temporais, por outro lado, foram criados em um momento de extrema importância. Exemplos clássicos são as variações cambiais ao longo de um dia ou o tráfego de usuários por hora.

Quando tratamos um dado atemporal que tem dados ausentes, normalmente vemos explicações de que o mais simples é remover as linhas que têm falta de dados. Isso porque muitos algoritmos não conseguem fazer análises com dados ausentes e, na maioria dos casos, eles são abundantes o suficiente para que a remoção de algumas linhas tenha pouca influência.

No entanto, quando falamos de dados temporais, a remoção de um dado pode ser bastante problemática. Os dados precisam de cadência, padrão, especialmente se formos fazer análises de frequência. Então, quais são as alternativas? Esse texto é justamente para ilustrar algumas dessas alternativas :)

Gostou? Confira [o texto completo na Revista do Data Bootcamp](https://medium.com/databootcamp/o-que-fazer-quando-faltam-dados-255ef5508a4f)
