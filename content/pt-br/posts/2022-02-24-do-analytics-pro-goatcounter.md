---
layout: post
title: "Mudando do Google Analytics para o GoatCounter: 6 meses depois"
categories:
  - estatística
  - blog
tags:
  - stats
  - blog
  - go
  - goatcounter 
  - GoogleAnalytics
  - tracking
  - GoLang
  - open-source
featured-img: goatcounter
img-description: Uma captura de tela do site do GoatCounter dizendo em inglês Análise de web fácil e sem rastreamento de dados pessoais
translationKey: analytics2goatcounter
slug: analytics2goatcounter
date: 2022-02-24T00:00:52+00:00
---

Ano passado (2021)[eu decidi começar a usar o GoatCounter como ferramenta de análise de tráfego do meu site](https://rgth.co/blog/replacing-google-analytics-with-goatcounter/). Algumas razões me levaram a essa decisão, mas a maior delas com certeza foi privacidade. Eu queria sair um pouco do mundo Google e procurava algo diferente. 

<!--more-->

Desde que eu instalei o GoatCounter, eu não removi o código que o Google Analytics usava e agora eu tenho dados suficiente (6 meses) para analisar a diferença entre os dois, e o que eu deveria esperar uma vez que eu parasse de usar o Google Analytics.

Os dados que eu analisei foram coletados entre 13 de Julho de 2021 e 13 de Janeiro de 2022. 

# Por onde as pessoas estão vindo?

A primeira métrica que eu decidi olhar é de onde estão vindo as pessoas que acessam o site. O Google oferece várias maneiras de visualizar e baixar esses dados. Como você pode ver no gráfico abaixo, a grande maioria das requisições (>75%) vem de busca orgânica, com requisições diretas (pessoas digitam direto o link para o site) em segundo (17,7%). O Google Analytics perdeu a origem de algumas poucas requisições, mas nas estatísticas gerais, ele reconhece a origem cerca de 100% das origens das requisições.

{{<figure src="/assets/img/posts/analytics2goatcounter/01.png#center" lt="A screenshot of a pipe chart with 75% of organic search, 17.7% of direct and 2 smaller pieces of Referral and Social">}}

GoatCounter mostra uma lista de origem em vez dos dados já classificados. Isso não foi útil para comparar com os dados do Google, então copiei os dados em uma planilha e os classifiquei manualmente.

{{<figure src="/assets/img/posts/analytics2goatcounter/02.png#center" lt="A screenshot of a list of links with Google having 64%, unknown having 12% and leportella.com havin 5%, all other links have 1%, most of them are links to leportella.com pages">}}

Como você pode ver, o GoatCounter confirma que a grande maioria das requisições (>69%) são provenientes de busca orgânica, e em segundo lugar vêm as requisições que vieram diretamente para o site (15,1%). A principal diferença é que o número de origens desconhecidas se tornou muito alto do que quando comparado ao Google (>12%).

{{<figure src="/assets/img/posts/analytics2goatcounter/03.png#center" lt="A screenshot of a pipe chart with 69.4% of organic search, 12.2% of unknown, 15.1% of direct and 2.6% of social">}}

Então, saindo do Google Analytics, esses são os resultados percentuais:


| Type | Google Analytics | GoatCounter | Diferença (indo p/ GoatCounter) |
| --- | --- | --- | --- |
| Organic Search | 75.7% | 69.4% | -6.3% |
| Direct | 17.7% | 15.1% | -2.6% |
| Referral | 3.7% | 0.6% | -3.1% |
| Social | 3% | 2.6% | -0.4% |
| Other | 0% | 12.2% | +12.2% |

O GoatCounter manteve as tendências da origem de requisições (maioria de busca orgânica seguida de requisições diretas).

A principal diferença foi a quantidade de requisições desconhecidas, o que pode ser explicado pelo fato desse projeto focar em *privacidade*. Já que o GoatCounter não guarda dados do usuário ele tem, portanto, menos dados para inferir sobre os usuários.

# Quantas pessoas estão acessando?

O Google tem o conceito de *usuários* que contam quantas pessoas únicas acessou o site. O GoatCounter só tem o conceito de sessões, então teremos que comparar essa métrica ao invés do número de usuários. O GoogleAnalytics tem algumas ferramentas bem legais como número de sessões por usuário, número de páginas acessadas a cada sessão e quanto tempo as pessoas ficam em cada sessão. Esse último número é bem baixa, então talvez as pessoas não estejam lendo os textos, mesmo que eu tenha uma quantidade grande de visualizações 😅.

{{<figure src="/assets/img/posts/analytics2goatcounter/04.png#center" lt="A screenshot of several numbers from Google Analytics, including Users, new users, sessions, number of sessions per user, page views, etc.">}}

Os dados do GoatCounter são mostrados apenas como um gráfico de barras e dois números totais: número de visitas (ou sessões) e visualizações de página. 

{{<figure src="/assets/img/posts/analytics2goatcounter/05.png#center" lt="A screenshot of GoatCounter histogram of sessions over time, with the total number of visits and pageviews in that period (26802 and 28018, respectively)">}}

Eu analisei o número total de sessões e visualizações durante os 6 meses. O GoatCounter contou 10% mais sessões do que o Google. Isso faz sentido para mim porque as pessoas que usam AdBlockers e ferramentas antirastreamento podem ser contadas pelo GoatCounter, enquanto que essas visualizações tavam bloqueando o sistema de rastreamento do Google.

No entanto, a métrica interessante é que o número de visualizações de página é 10% menor. Eu não tenho idéia de por que isso pode estar acontecendo. Achei absolutamente fascinante que as métricas mudam exatamente na mesma quantidade, mas em direções opostas! Penso que pode ser pelo o mesmo motivo, mas... não sei na verdade.

Eu também olhei para a métrica de um dia apenas. No GoatCounter, 30 de agosto foi o pico de sessões, com 280 sessões nesse dia enquanto o total do Google foi de apenas 194. Essa foi uma diferença de 44% entre os dois! Da mesma forma, o Google mostrou um dia de pico em 20 de julho e a diferença foi de -80% no Goat Counter.

|  | Google Analytics | GoatCounter | Moving to GoatCounter |
| --- | --- | --- | --- |
| Number of users | 19711 | - | -100% |
| Number of sessions | 24262 | 26802 | 10.47% |
| Page views | 31300 | 28018 | -10.49% |
| Peak GoatCounter day (30 Aug) | 194 | 280 | 44.33% |
| Peak Google day (20 July) | 781 | 157 | -79.90% |

De forma geral, acho que a métrica é sólida, com ~10% de diferença entre ambas as ferramentas. No entanto, em um único dia as diferenças podem ser enormes!

{{<figure src="/assets/img/posts/analytics2goatcounter/06.png#center" lt="A screenshot of GoatCounter histogram of sessions over time, showing the number for 30 of August, where there were 280 visits and 303 pageviews">}}

{{<figure src="/assets/img/posts/analytics2goatcounter/07.png#center" lt="A screenshot of Google Analytics chart with sessions over time, showing the number for 30 of August, where there were 194 sessions">}}


# De onde as pessoas estão vindo?

Eu sempre gostei muito do mapa-múndi colorido do Google Analytics para me mostrar de onde vêm os usuários. Posso ver todas as métricas que falei antes, mas por país, o que é legal.


{{<figure src="/assets/img/posts/analytics2goatcounter/08.png#center" lt="A screenshot of Google Analytics chart with sessions over time, showing the number for 30 of August, where there were 194 sessions">}}


O GoatCounter mostra apenas gráficos de histograma e apenas para sessões:

{{<figure src="/assets/img/posts/analytics2goatcounter/09.png#center" lt="A screenshot of GoatCounter histogram with sessions per country with Brazil having 46%, US 14% and India 4%">}}


Pesquisei os 5 principais países para cada ferramenta e, surpreendentemente, há muita diferença! Podemos ver um aumento de 300% para a Irlanda e uma diminuição de 89% para a China!

|  | Google Analytics | GoatCounter | Indo p/ o GoatCounter |
| --- | --- | --- | --- |
| Brazil | 10895 | 12373 | 14% |
| US | 3692 | 3677 | 0% |
| India | 1054 | 1030 | -2% |
| Germany | 616 | 897 | 46% |
| UK | 678 | 872 | 29% |
| Ireland | 145 | 578 | 299% |
| China | 771 | 86 | -89% |

Acho que essa é, de longe, a métrica em que eu menos posso confiar em ambas as ferramentas. Posso imaginar que o GoatCounter é muito mais focado em privacidade, tendo provavelmente menos ferramentas para definir de onde está vindo uma sessão. Mas a não ser que a maioria dos acessos na Irlanda tenham sistemas anti-rastreio, não consigo explicar o crescimento gigantesco em termos de número. O mesmo com os números menores da China.


# Conclusão

No geral acho que o GoatCounter se mostrou uma boa ferramenta, e as métricas mais importantes para mim (sessões e visualizações de página) estão muito próximas do número que eu tinha no Google Analytics.

Acho que o que mais sentirei falta são os gráficos e dashboards, que tornam a visualização mais interessante. Como eu mesma rodo o serviço do GoatCounter local eu mesma posso baixar os dados e gerar os gráficos se quiser. E além disso o GoatCounter é de código aberto. Eu poderia implementá-los eu mesmo, o que também é legal.

Por hoje é só. Agora que eu sei o que esperar eu posso dizer... tchau Google Analytics 😎