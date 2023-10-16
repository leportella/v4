---
layout: post
title: "Crescendo como uma desenvolvedora na Stripe"
categories:
  - carreira
  - pessoal
tags:
  - eventos
  - tecnologia
  - Stripe
  - San Francisco
  - Dublin
  - engenharia de software
  - desenvolvimento
  - desenvolvedores
  - desenvolvedora de sofwtare
  - python
  - book
  - friendly guide to software development
featured-img: bucharest
slug: crescendo-na-stripe
date: 2023-10-15T18:25:52-05:00
translationKey: growing-at-stripe
---


Há um século atrás, [eu escrevi um post](https://leportella.com/pt-br/nova-eng-stripe/) falando sobre como foram os meus primeiros 6 meses na Stripe. Desde então muitas coisas aconteceram, inclusive uma pandemia e eu usando todo o meu tempo livre pra escrever [meu livro](https://leportella.com/book/). Por causa disso e muitas outras coisas, eu acabei nunca escrevendo uma sequência para o que eu gostaria que fosse uma série anual. Recentemente eu fui convidada para contar um pouco sobre a minha carreira na Stripe no nosso evento de lançamento do escritório de Bucareste. Isso ativou a escritora que há em mim. Esse texto é uma versão expandida da palestra que eu dei naquele evento e conta um pouco como eu cresci e continuo crescendo como uma engenheira de software na Stripe.

## Trabalhando em um produto muito, muito legal

Depois de alguns meses que eu entrei eu tive a oportunidade maravilhosa de me junto a um projeto novinho em folha. O projeto eventualmente virou o que agora é o [Stripe Tax](https://stripe.com/ie/tax). Imposto é um tópico extremamente complexo e todas conhecemos a frase “a única coisa certa na vida são a morte os impostos”. No entanto, quando negócios começam a vender no mundo todo, a complexidade de impostos aumenta exponencialmente e eles se vêem de repente sujeitos a muitas regras esquisitas. Por exemplo, não importa se você vendou apenas um real na Suíça. [Se você tem uma certa renda global](https://stripe.com/docs/tax/threshold-rules#europe,-the-middle-east-and-africa), assim que você vendo um produto na Suíça, você deveria pagar imposto pro governo suíço.

Como você pode imaginar, saber dessas regras ja é complicado. Conseguir cumprir com todas ela é algo ainda pior.

Quando me juntei ao projeto, ainda era apenas uma ideia de um produto que queríamos construir ou, mais precisamente, um produto que os usuários estavam implorando para que construíssemos. Tive a sorte de de estar presente quando apresentamos o projeto inicial e nas discussões sobre como modelar e criar um produto simples que soluciona um tópico tão complexo.

O time trabalhou desde a ideia, passando por uma iteração inicial de um MVP até finalmente liberarmos acesso para qualquer cliente da Stripe usar. O dia do lançamento foi um dos melhores dias da minha carreira. Aquilo era meu "bebê", algo em que eu e minha equipe trabalhamos tão árduamente e por tanto tempo. Essa sou eu e a incrível Kelly Moriarty, nossa Gerente de Produto, no dia do lançamento do Stripe Tax:

{{<figure src="/assets/img/posts/eng_at_stripe/1.jpg#center" lt="A photo of two women with champagne glasses and a computer">}}


Se você quiser saber mais sobre como construímos o Stripe Tax, recomendo [este post do blog da Kelly](https://stripe.com/blog/building-stripe-tax) que conta tudo em detalhes.

Antes que você pense que eu sabia algo sobre impostos, pode ter certeza: eu não sabia absolutamente nada. Nada mesmo! Tive que aprender *muito*. Mas felizmente tive especialistas em impostos ajudando nossa equipe de engenharia a aprender um monte de fatos interessantes que nos ajudavam a criar o produto. Por exemplo, um dos meus fatos favoritos é que em Nova York um bagel não está sujeito a impostos sobre venda. A menos que você o corte, então ele se torna um sanduíche e agora deve ser taxado. A menos que você compre doze. Então ele não é tributado novamente. Você consegue imaginar descobrir isso sozinhoa!? Mas definitivamente meu fato favorito sobre impostos é sobre os bonecos de gengibre (daqueles de natal, tipo o do Shrek). Do post da Kelly:

- *No Reino Unido, se um boneco de gengibre tem apenas dois olhos de chocolate, ele é legalmente um biscoito (isento de impostos). No entanto, se esse boneco de gengibre também estiver vestindo calças ou uma camisa de chocolate, ele agora está sujeito a impostos a uma taxa padrão de 20%.*

A Stripe é uma empresa obcecada pela experiência do usuário, então sabíamos que nosso produto de impostos precisava ser incrivelmente fácil de adotar e usar. Com um tópico tão complexo, tivemos inúmeras discussões sobre como poderíamos tornar os impostos *o mais simples possível*. Externamente, o que fizemos foi adicionar um único parâmetro à nossa API:

{{<figure src="/assets/img/posts/eng_at_stripe/3.jpg#center" lt="">}}

Parece simples, mas como qualquer desenvolvedor sabe, uma experiência de usuário realmente simples esconde uma enorme quantidade de complexidade no sistema. A quantidade de discussões e iterações que tivemos para garantir que essa fosse a melhor maneira possível (naquele momento) foram empolgantes. A Kelly mencionou no blog que tivemos discussões sobre se algum dia precisaríamos de um parâmetro como `boneco_de_gengibre_esta_usando_calca` na API. Parece uma piada, mas nossas discussões *foram a fundo* e tópicos como esse surgiram muitas vezes!

{{<figure src="/assets/img/posts/eng_at_stripe/2.jpg#center" lt="">}}

Trabalhando com impostos, eu me sempre vi mais como uma engenheira de produto, o que significa que meu principal trabalho era resolver os problemas dos nossos clientes. Um bom exemplo é que quando estávamos construindo uma nova API e um dos nossos clientes Beta disseram que um webhook tornaria sua vida melhor. Internamente, discutimos quando e como acionaríamos o webhook e se isso era a coisa certa para todos os clientes que quisessem usar essa API. Perguntas como "poderíamos melhorar a experiência de uma maneira que eles nem precisassem desse webhook?" eram coisas que constantemente nos perguntávamos. Depois de adicionar o webhook, nunca mais precisei me preocupar se o webhook seria entregue, quando ou como. Eu apenas sabia que seria. Meu trabalho era garantir que estávamos ajudando nossos clientes a terem as melhores funcionalidades o mais rápido possível.

Conforme nosso produto de Stripe Tax cresceu e se tornou mais complexo, começamos a abraçar novos desafios.

Quando criamos o produto consideramos apenas uma relação 1:1 entre um comerciante e um cliente, para simplificar o nosso MVP.

No entanto, um dos maiores produtos da Stripe é o [Connect](https://stripe.com/ie/connect), que permite que várias empresas diferentes estejam envolvidas em um mesmo pagamento. Pense no Doordash ou Ifood, por exemplo. Você, o cliente, faz um único pagamento para comprar um bagel, mas a empresa está pagando ao motorista e ao restaurante, o que significa que você tem vários comerciantes envolvidos nessa única transação.

Eu liderei a primeira iteração sobre como faríamos o Stripe Tax funcionar com o Connect. Este foi um projeto muito desafiador em que tinha que entender profundamente ambos os produtos para descobrir como poderíamos mesclá-los de uma maneira que o cliente tivesse uma ótima experiência. Lançamos essa funcionalidade no mês passado, e eu estou super feliz que o nosso produto agora está disponível em cenários tão complexos como os que o Connect permite que nossos clientes desenvolvam.

Eu tive a sorte de trabalhar em um produto incrível. Trabalhei em muitos projetos desafiadores com um grupo de pessoas que admiro profundamente. Mas eu também queria contar para vocês que houve muitas outras maneiras de continuar aprendendo além desses projetos.

### Logs de atrito

À medida que você adquire conhecimento especializado, é fácil cair na armadilha de construir um produto que não é acessível *a menos que* as pessoas sejam especialistas. Para evitar isso e garantir que o Stripe Tax sempre tivesse a melhor experiência do usuário, pelo menos uma vez por semestre realizamos sessões de *Logs de atrito*, onde todos os membros da equipe, sejam recém-chegados ou não, tentam usar nosso produto do zero, tentando pensar como um cliente pensaria. Fazemos anotações sobre quais partes foram difíceis, quais documentações podem ser aprimoradas e quais partes do sistema não faziam sentido e precisavam ser melhoradas. Além de gerar uma lista de coisas que podemos melhorar, esse exercício também nos ajuda a não criar um produto apenas para nós, que falamos sobre impostos todos os dias. Tem sido uma ótima maneira de desenvolver essa mentalidade de *usuários em primeiro lugar* e nunca perder o foco em quem realmente importa em tudo isso.

### Revisões de API

Temos um processo para projetar novas APIs e adicionar melhorias às APIs existentes. Posso propor um design e iterar com desenvolvedores mais experientes para aprender as melhores práticas de design de API, e temos um grupo que garante que nossas APIs sejam consistentes em todos os aspectos. Isso é especialmente útil, pois, no meu dia a dia, posso não saber sobre uma nova API sendo desenvolvida por uma equipe distante que possui um padrão útil para eu seguir.

Mais recentemente, comecei a estudar e me aprofundar como Avaliadora de API, onde tive a oportunidade de aprender esses designs com mais profundidade e aprender com várias APIs sendo desenvolvidas em toda a Stripe. Fico feliz em compartilhar que acabei de me "formar" como avaliadora e agora faço parte do grupo que está ajudando a Stripe a ter APIs de alta qualidade que todos conhecemos e amamos.

### Aprendendo com outras equipes

O que gosto na Stripe é que amamos documentação - e muito. Portanto, você tem a oportunidade de aprender com outras equipes e projetos que lhe interessam, mesmo que você nunca trabalhe neles. Há muito o que podemos aprender uns com os outros, então gosto de observar a documentação aleatória e aprender com a experiência de outras pessoas.

### Orçamento para educação

Como uma pessoa nerd, uma das coisas que mais gosto para continuar aprendendo é o orçamento para educação que temos. Em nossa equipe do Stripe Tax, frequentemente compartilhamos sugestões de livros e tínhamos um documento com uma lista muito longa de livros que você deveria ler.

{{<figure src="/assets/img/posts/eng_at_stripe/4.jpg#center" lt="">}}

*Observação: eu REALMENTE uso isso! Esta é apenas uma parte dos livros que adquiri com meu orçamento ao longo dos anos*. Eu recomendaria muito o livro "The Staff Engineer's Path" de Tanya Reilly.

### Comunidades

Temos uma comunidade de engenharia muito forte. Temos vários cursos internos, palestras técnicas e apresentações de projetos que você pode acompanhar para aprender com outras equipes e pessoas. Em particular, gosto do trabalho que estamos fazendo em Dublin, para garantir que os engenheiros tenham uma rede de apoio para se apoiar.

Além das comunidades focadas em engenharia, também faço parte da comunidade Unidos para hispânicos e latinos. Como imigrante brasileira, tive que enfrentar muitos desafios ao me mudar para um país novo e trabalhar em um idioma que não é o meu nativo. Até pequenas coisas que eu achava que seriam *normais* em um ambiente de trabalho eram bastante diferentes (recomendo muito "[The culture map](https://erinmeyer.com/books/the-culture-map/)" se você quiser entender melhor). Encontrar uma comunidade com a qual eu pudesse compartilhar tudo isso foi super valioso. Isso me deu uma sensação de pertencimento e também me ajudou a me conectar com diferentes partes da empresa.

{{<figure src="/assets/img/posts/eng_at_stripe/5.jpg#center" lt="">}}

### Mudando de funções e compartilhando conhecimento

A Stripe incentiva os engenheiros a aplicarem o que aprenderam, a desenvolver mais habilidades e a compartilhar conhecimento de forma ampla dentro da empresa. Temos um quadro de empregos interno onde você pode verificar as oportunidades disponíveis em toda a empresa e é incentivado a mudar de função se estiver em seu cargo por mais de um período. Essa é uma das razões pelas quais, após 4 anos trabalhando com o Stripe Tax e uma engenharia mais focada em produtos, decidi me mudar para um desafio diferente.

Recentemente, mudei para a equipe responsável pela infraestrutura de nossas APIs, chamada API Platform. É algo completamente novo em que não tenho experiência, mas estou feliz por ter a oportunidade de trabalhar em algo novo e desenvolver uma área na qual ainda não havia me concentrado.

### Aprendendo com pessoas de diferentes áreas

Por fim, gostaria de compartilhar que temos muitas pessoas incríveis em toda a empresa. Tive a oportunidade de trabalhar com muitas pessoas de diferentes equipes, funções e organizações. Aprendi muito com todas elas!

{{<figure src="/assets/img/posts/eng_at_stripe/6.jpg#center" lt="">}}


Minha experiência foi tão incrível que me ajudou com muitas das habilidades que eu precisei pra escrever um livro técnico sobre desenvolvimento de software para pessoas que não são desenvolvedores mas que precisam entender como software é feito. Eu lancei ele no ano passado e estou muito feliz que todos os meus aprendizados agora ajudam pessoas em outras empresas também. 

{{<figure src="/assets/img/posts/eng_at_stripe/7.jpg#center" lt="">}}


—

Enfim, esse foi um resumo *bem resumido* dos meus últimos 4 anos e meio na Stripe. Enquanto penso sobre esse tempo eu percebo que daria um outro livro inteiro com o tanto de coisas que aconteceram! Eu só estou feliz que continuo aqui e crescendo. E espero que não demore 4 anos pra eu escrever um outro post sobre a Stripe!