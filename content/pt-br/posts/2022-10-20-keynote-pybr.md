---
layout: post
title: "O que raios eu faço aqui?"
categories:
  - desenvolvimento de software
  - palestra
tags:
  - palestras
  - pythonxp
  - pycon
  - pybr 
  - python brasil
  - python brazil
  - eventos
  - tecnologia
featured-img: pybr22
remove-inside-img: true
slug: keynote-pybr
last_mod: 2022-10-20T18:25:52-05:00
date: 2022-10-20T18:25:52-05:00
---

Vídeo e transcrição da minha palestra durante a Python Brasil 2022 :) 

<!--more-->

{{<youtube "Hqcj2MhtKso&t=373s">}}

## Transcrição 

Sabe, quando eu fui chamada pra palestrar aqui eu fiquei me perguntando “o que eu tenho pra falar”? Comecei a pensar em tudo o que eu vivi nos últimos 6 anos, desde o primeiro dia que meu emprego profissional se chamava *desenvolvedora de software*. Eu olhei pra meus empregos e o que eu faço hoje e ficava perguntando **“O que raios eu faço aqui?”**, em busca de um tópico que eu pudesse falar aqui nesse palco que é tão importante pra mim.

Pra quem não me conhece, eu sou oceanógrafa de formação mas troquei a vida de estudo dos oceanos pra me tornar desenvolvedora. Antes dessa minha versão 2.0 de carreira, eu ganhava minha vida trabalhando em uma empresa de consultoria de engenharia portuária.

Essa empresa tinha um simulador de navios, como esse que você pode ver aqui nessa foto (esquerda), e a gente usava esse simulador pra conseguir analisar a viabilidade de um novo navio conseguir manobrar em um porto que já existe ou se o projeto para um novo porto funciona para os tipos navio que eles esperavam receber.


{{<figure src="/assets/img/posts/o_que_raios/8.jpg#center" alt="Duas imagens lado a lado. A da esquerda mostra quatro telas mostrando um simulador de navios. A imagem da direita são duas pessoas, um homem e uma mulher, de costas, olhando pra telas do mesmo simulador.">}}


Então a gente ia lá, reproduzia as correntes e marés e colocava isso dentro do simulador para que os pilotos pudessem ter um ambiente realístico para tomar as decisões. Quando tudo estava pronto, levávamos o simulador para os portos e fazíamos workshops onde os pilotos, os donos dos portos, representantes dos navios e autoridades da Marinha se reuniam para avaliar o que estava sendo proposto.

No meu primeiro dia de trabalho, no entanto, eu não sabia nada daquilo. E logo no meu primeiro dia a minha empresa estava recebendo um desses workshops. Para uma pessoa novata como eu aquilo não fazia o menor sentido. O workshop funcionava assim: a gente tinha várias telas reproduzindo o que se via da cabine de comando. Aqui embaixo ficavam os controles do navio, essas telas aqui reproduziam o que se via da cabine de comando, na direita a gente via as informações sobre o navio e na esquerda ficava a carta náutica, onde dava pra ver o layout do canal, do porto e a situação das correntes a cada minuto.

{{<figure src="/assets/img/posts/o_que_raios/13.jpg#center" alt="Uma sala com várias telas que compõe um simulador de um navio. Embaixo em cima de uma mesa tem um console (físico), em uma das telas vê-se uma carta náutica, cinco telas no centro formam a cabine de comando e uma tela apresenta informações sobre o navio.">}}

Bom, aí uma vez que um piloto começava uma manobra, ficávamos lá, umas 15 pessoas numa sala escura olhando para umas telas e vendo um navio se mexer *muito devagar*. Sério, muito devagar. Ficamos lá horas a fio olhando esse navio lentamente se aproximar do porto. Eu achei aquilo a coisa mais entediante do mundo e não conseguia entender o propósito de tudo aquilo. Porque aquelas manobras eram tão críticas? Quão complexo pode ser?

Algum tempo depois eu tive oportunidade de falar com o piloto de uma das manobras e perguntar: “quão difícil pode ser manobrar um navio a ponto de precisar disso tudo?”. A resposta dele foi rápida “Realmente. Não é nada complexo. É como se você quisesse estacionar um carro. Só que o carro tem 350 m, não tem freio, você não vê a pista e o chão se mexe.” Oops.

{{<figure src="/assets/img/posts/o_que_raios/20.jpg#center" alt="Um slide com o título 'é como manobrar um navio' e várias caixas que dizem em sequência: de 350m, que não tem frio, você não vê a pista e o chão se mexe.">}}

Quando eu comecei a olhar pro que eu faço hoje, eu percebi que, de certa forma, o que eu faço é manobrar navios metafóricos. Os projetos que eu lidero são tão complexos quanto um navio sendo manobrado e igualmente difíceis de entender e explicar da onde realmente vem a complexidade.

.   .   .

Se olharmos com um pouco mais de cuidado no nosso navio metafórico, podemos traçar correlações.

Quando trabalhamos em empresas um pouco maiores, os projetos mais complexos demandam uma quantidade de times, pessoas e processos que é enorme. São muitas coisas que tem que funcionar em conjuntos para fazer a coisa andar e, da mesma forma que acontece com o navio, a inércia pode ser grande e pequenas mudanças demandam tempo para causar efeitos reais.

Em um navio, temos que ficar conferindo sempre se estamos dentro do caminho correto, ja que o caminho fica escondido e temos apenas algumas sinalizações para nos guiar. No nosso mundo precisamos sempre estar ajustando o nosso rumo para garantir que estamos entendendo e atendendo às necessidades dos nossos clientes.

O chão que se mexe o tempo todo são os infinitos projetos, decisões e mudanças que acontecem à sua volta. São milhares de coisas acontecendo ao mesmo tempo e que você tem que se adaptar a todos os momentos, ajustando o rumo conforme as condições mudam.

{{<figure src="/assets/img/posts/o_que_raios/24.jpg#center" alt="Uma foto de um homem pilotando um navio. Da cabine de comando vê-se a parte de frente do navio e um mar revolto. Uma seta mostra o tamanho do navio e diz 'times, processos e pessoas', outra seta aponta pra uma das telas na cabine de comando e diz 'desejos dos clientes', uma seta aponta pro mar revolto e diz 'infinitos processos e decisões'.">}}

No meu primeiro encontro de Python, quando eu ainda estava trabalhando nessa empresa, me perguntaram quem eu era e o que eu fazia e fiz questão de falar que não era programadora. Naquela época, eu escrevia pequenos scripts que me ajudavam a resolver alguns problemas, então se eu não escrevia sistemas eu não poderia ser chamada de programadora.

Quando me fizeram a pergunta novamente, eu já tinha conseguido meu primeiro emprego de desenvolvedora e ainda assim disse que eu tinha dificuldades de me considerava uma desenvolvedora. O motivo? Eu nunca tinha feito um *deploy em produção*.

Passando pros dias de hoje e me perguntando “o que raios eu faço aqui” me veio aquele pânico de que eu, na verdade, não tenho nada que valesse a pena trazer de conteúdo técnico. Me peguei pensando em tudo o que eu não sei e acho que eu deveria aprender antes de me achar competente o suficiente para estar aqui falando com vocês.

É sempre fácil arrumar falhas de conhecimento para desmerecer meu título de desenvolvedora e duvidar dos caminhos que eu tracei até aqui. Sempre vai existir algo que eu não sei que vai me fazer duvidar de quem eu sou. Sempre vou achar que me o que me “falta” (entre bastante aspas) pra conseguir me apoderar desse título é aprender  essa ou aquela ferramenta, framework ou linguagem de programação.

Mas pensando nos navios que navego, eu percebi que nada disso de fato representa o meu trabalho. O meu trabalho é lidar com complexidades, resolver problemas e manobrar esses navios metafóricos. Código é apenas uma das ferramentas que eu uso pra isso.

{{<figure src="/assets/img/posts/o_que_raios/27.jpg#center" alt="Duas formas coloridas onde lê-se 'Meu trabalho é resolver complexidades '">}}


Quando eu comecei a minha carreira, eu jamais poderia imaginar que eu teria que e conseguiria manobrar esses navios. Como eu falei no começo, se você não está na cabine de comando, é muito difícil entender da onde vem a complexidade. Fiquei pensando em como melhor mostrar isso e achei que a melhor maneira era trazer um navio desses, pra gente manobrar juntos aqui. Eu queria convidar todos vocês a pensarem o que você faria em cada uma dessas situações. O que você faria?

Vamos imaginar por um momento que nós somos acabamos de entrar no time de desenvolvimento numa empresa chamada JollyCo. A empresa vende produtos da fazenda direto pra pessoas em aplicativos que personalizam os pedidos direto com o que as pessoas cozinham em casa. É um aplicativo bem inovador em que as pessoas selecionam quais receitas elas pretendem fazer naquela semana e o aplicativo monta uma lista de produtos necessários para a quantidade de comida e pessoas e já faz o pedido dos produtos direto das fazendas mais próximas.

Na verdade, estamos bem felizes de fazermos parte desse time. A empresa tem crescido bem e o produto é um sucesso, já estando disponível na Argentina, Uruguai e Chile, além do Brasil. Ok, tudo certo até que um belo dia de sol, sua gerente pede que você lidere o projeto de expansão do produto para Nárnia.

Navio a ser manobrado definido, todos a bordo!

.   .   .

Qual é a primeira coisa que você faria agora nesse momento, assim que sobe na cabine de comando?

É sempre importante começar entendendo exatamente onde o meu trabalho se encaixa dentro do contexto geral do meu time e da empresa. Da onde veio esse pedido? De um cliente pedindo esse novo país ou foi uma decisão vinda do negócio? Alguém já fez uma pesquisa de mercado na região? Temos alguns clientes que estão presentes naquele país que possamos conversar? Tem algum tipo de dado que podemos analisar para ajudar a entender melhor o cenário e a situação?

Quando eu comecei nessa carreira, uma das coisas mais assustadoras era fazer perguntas. Perguntas técnicas eram assustadoras mas perguntas de *negócio*… pareciam totalmente desnecessárias. Eu partia do princípio que se aquela decisão foi tomada, *alguma pessoa muito mais esperta do que eu claramente sabe o que está fazendo*, certo?

Tem um ditado russo que eu aprendi e que eu gosto muito que diz: “confie, mas verifique”. Garantir que as perguntas que você tem foram todas respondidas é fundamental para um projeto de sucesso. E isso vale do estagiário à pessoa sênior.

Nunca ouvi ninguém reclamar “acho que precisamos que os desenvolvedores façam mais código e fiquem menos tempo entendendo o problema”.

{{<figure src="/assets/img/posts/o_que_raios/35.jpg#center" alt="Uma tela amarela que diz 'acho que essas devs deveriam gastar mais tempo no código e menos tempo entendendo o problema' e embaixo lê-se 'disse ninguém, nunca'">}}

É parte do nosso trabalho fazer perguntas. Você consegue imaginar um piloto recebendo um navio completamente desconhecido, entrando na cabine de comando e dizendo “não preciso de contexto, bora lá manobrar essa bagaça!” Não, certo? Ninguém espera isso e seria até… perigoso. Gastar um tempo entrando na cabine, olhar as cartas náuticas pra ver o trajeto, dar uma conferida na previsão do tempo… como estão as correntes hoje? Tem alguma tempestade vindo? Tudo isso faz parte, mesmo que isso atrase levemente a nossa partida.

Bom, vamos lá. Gastamos o nosso primeiro momento para entender o ambiente. Estamos confiantes de que esse projeto tem tudo para ter sucesso. O time de pesquisa e negócio tem excelentes documentos explicando o contexto, lemos as notas das entrevistas com empresas locais… tudo nos conformes. Estamos confiantes que entendemos o problema e que as nossas principais perguntas foram respondidas. Ótimo! E ai? Qual é o próximo passo?

Bom… toda a documentação que nós lemos dá uma ideia *de negócio* sobre o problema. É hora de começar a entender qual o tamanho do buraco olhando pra parte de código. Temos que definir o que deve ser feito e quebrar em tarefas menores, definir o famoso *escopo* do projeto.

{{<figure src="/assets/img/posts/o_que_raios/44.jpg#center" alt="Uma tela com o titulo escopo e vários retangulos coloridos que se sub-dividem em mais retângulos coloridos">}}

Mas vamos lá… a gente acabou de começar nessa empresa, não temos muita ideia da base de código e já temos alguém no nosso pescoço perguntando quando que podemos entregar o projeto pra aquele cliente mais que especial que está realmente precisando disso pra anteontem. O que você faria?

Acho que daria para falar uma palestra inteira sobre escopo, porque esse é um assunto bem difícil. A minha estratégia é bem simples: se eu não entendo muito bem a área que eu vou trabalhar, eu começo pedindo ajuda dos meus colegas mais experientes na área. Eu pergunto para várias pessoas diferentes quais são os problemas que eu vou encontrar, as coisas que elas imaginam que eu preciso fazer de qualquer forma e se tem alguma armadilha que eu possa encontrar que vai fazer todo meu planejamento ir por água abaixo.

E é para essas pessoas que a gente também vai fazer a perguntinha mágica: quanto tempo cada uma dessas coisas deve demorar. De novo, nós não temos experiência ainda nesse código! Precisamos nos basear em alguma coisa. E experiência passada é sempre melhor do que chutes aleatórios, certo?

O que eu faço pra ser feliz nessa hora, quando eu sei que o projeto pode ser longo, é dobrar a medida. Falaram que vai demorar 2 dias? Coloca 4 no planejamento. Falou que vai demorar 1 semana? Coloca 2. Se o negócio vai demorar mais de 2… melhor começar a quebrar em tarefas menores…. senão der, talvez seja melhor colocar mais uma gordurinha…

.   .   .

Uma das maiores falácias é a gente achar que um dia nós vamos olhar para um código, vai descer uma luz e vamos saber exatamente o que precisa ser feito e quanto tempo vai demorar. Você não precisa fazer tudo você mesma. Na verdade, o seu trabalho é se fazer com que as coisas andem, e se elas não andam… o seu trabalho é pedir ajuda.

Então tá, fomos falar com o nosso time e todas as pessoas que conversamos estão confiantes que esse projeto vai ser simples. O produto já está disponível em outros países, já tem suporte à internacionalização da documentação e do site, e o último país que foi feito foi desenvolvido há pouco tempo, a documentação está toda atualizada e o código genérico o suficiente. O projeto todo demorou apenas 2 meses para ser concluído e não houve nenhum problema pelo caminho.

Ok, fizemos nosso escopo… temos a lista de tarefas que precisam ser feitas e também temos uma ideia de onde estão as possíveis armadilhas. Nosso trabalho está completo?

Esse é um momento crucial da manobra: antes de começarmos a executá-la, todas as pessoas envolvidas precisam estar cientes de onde estão os riscos e as incertezas. É fundamental que nós comuniquemos claramente onde estão nossas incertezas, quais pontos nos preocupam e o que estamos fazendo para mitigá-los.

{{<figure src="/assets/img/posts/o_que_raios/42.jpg#center" alt="Uma tela com o duas formas coloridas onde lê-se 'Comunicação clara dos riscos e incertezas e o que estamos fazendo para mitigá-los'">}}

Deixar o mais explícito possível todos esses pontos faz com que todas as pessoas envolvidas nessa manobra estejam cientes de que você fez o seu melhor para encontrar e mitigar esses problemas, e não surpreende ninguém caso eles apareçam de repente. Eu gosto de deixar bastante exposto em que áreas eu deixei uma gordurinha pra compensar pelas incertezas que eu tenho e escrever documentos pra deixar registrado as pesquisas e pequenas decisões que foram tomadas no caminho.

Ótimo. E agora? É hora de colocar a massa? Uma vez que você tem uma lista de tarefas bem definidas… tudo está certo?

Antes de colocar a mão na massa, quando eu tenho uma lista do que precisa ser feito, eu gosto de analisar quais são as tarefas que são *fundamentais* pra que as coisas funcionem no novo país e quais são apenas *cosméticas* e que podem esperar um pouco mais. Eu quero saber exatamente o que, dessa lista que talvez seja bem grande, pode me ajudar a colocar esse produto na mão do cliente o mais rápido possível, mesmo que com todas as limitações que possam existir, seja de funcionalidade ou de experiência de usuário.

Nem sempre a tarefa mais fácil ou legal é a que vai me ajudar a entregar uma solução primeiro, então essa priorização ajuda a manter a perspectiva e não ficar apenas focada no que é tecnicamente mais desafiador ou interessante.

Ok! Acho que agora estamos com tudo certo para colocar a mão na massa! Hora de fazermos o que mais gostamos: escrever o bom e velho código!

{{<figure src="https://media.giphy.com/media/y93slPbDMdeXJQONHa/giphy.gif#center" width="250px" alt="Uma animação com um desenho de um ursinho digitando rapidamente e feliz">}}

Mas código não é o foco. É claro que poderíamos gastar horas aqui falando sobre essa etapa. Eu tenho certeza que vão ter muitas outras palestras nesse e em vários outros eventos que te permitam aprimorar essa parte.

O que eu quero falar é sobre outra coisa. Nesse processo todo a gente gastou um tempão entendendo o que precisa ser feito, fizemos o escopo e temos consciência dos problemas. Podemos dizer que temos tudo para ter um projeto de sucesso, certo?

Vamos dizer que começamos o projeto e logo em seguida percebemos que Nárnia ao invés de usar a representação de dinheiro que a gente usa, usa os símbolos de dinheiro a direita do valor monetário, mas nosso sistema não está preparado para essa variação. E aí!?

Bom, precisaremos adaptar todas nossas interfaces para lidar com isso. Isso com certeza não vai ser simples. Ninguém tem certeza quantas interfaces e APIs apresentam o formato de moeda desse jeito, então teremos quer fazer uma busca pelos confins do sistema pra modificar todos os lugares. Bom, podemos começar alinhando com todas as partes interessadas que essa é uma mudança longa mas estética, então podemos deixar para depois do lançamento. Ótimo, crise resolvida e o navio está de volta ao rumo.

Alguns dias recebemos um comunicado que o governo de Nárnia aprovou uma legislação nova, que qualquer cliente tem o direito de cancelar qualquer ordem, esteja ela no estado que estiver (paga, ou recebida) por até 48 horas após o pedido inicial. O nosso sistema não está preparado pra isso. Vamos precisar reescrever uma boa parte do sistema de reembolsos e precisamos de um sistema para gerenciar esse retorno com produtos altamente perecíveis, como aqueles que dependem de geladeira. Pelas nossas estimativas, isso vai demorar pelo menos 2 meses a mais e não podemos escapar: precisamos disso antes do projeto ser entregue.

Finalmente, quando tudo parece estar sob controle, alguém sutilmente chega pra você e diz: “ei… você viu que Nárnia tem uma lei bem rígida de proteção de dados!?”. Isso acende todos as bandeiras vermelhas na nossa cabeça. Isso não é uma mudança de vento ou uma virada da maré. Isso é um iceberg. E daqueles grandes! E agora?

{{<figure src="/assets/img/posts/o_que_raios/53.jpg#center" alt="Uma tela amarela escrito bem grande 'ei você viu que nárnia tem uma lei bem rígida de proteção de dados?">}}

Bom… agora é hora de investigar com muita calma e cuidado para ter certeza do que estamos fazendo. Pior do que um projeto atrasado é um projeto que infrinja leis e coloque nossa empresa e clientes em risco.

Ao investigar com mais calma, vemos que Nárnia tem uma lei extremamente rígida de proteção de dados, em que nenhum dado dos clientes pode sair do solo nacional. Todo o nosso sistema foi baseado em computadores no Brasil, com tráfego livre entre os países. Esse iceberg é dos grandes e o projeto simples de 2 meses, é algo que vai exigir uma mudança de estrutura do sistema inteiro da empresa inteira.

Inclusive precisamos analisar como que um requisito tão complexo como esse passou completamente despercebido por todas as pessoas envolvidas no projeto. Esse é o tipo de coisa que não poderia passar despercebido e foi uma falha bem grande. Precisamos inclusive documentar o que aconteceu para que isso não aconteça novamente, já que, como vocês podem ver, o projeto “tranquilinho” se tornou um monstrengo enorme que faz com que precisemos reavaliar completamente a estrutura do nosso sistema.

{{<figure src="/assets/img/posts/o_que_raios/56.jpg#center" alt="Uma tela com o título 'falhas acontecem' e uma sequência de desenhos embaixo que diz: entender, lidar, aprender e documentar">}}

Talvez você esteja pensando agora “ahhh não Letícia, isso é muito viagem sua.” Pois é… mas isso acontece. Há muito tempo atrás, em um dos projetos que eu liderei, eu fiz tudo bonitinho. Logo em seguida veio o primeiro problema. Chegou o segundo, o terceiro e assim por diante. Lá pelas tantas eu me deparei com um mega iceberg. Era um problema gigantesco que ia atrasar todo o fluxo do projeto e com certeza impactar o prazo final. O projeto estava com muitos riscos de não dar certo, o lançamento dessa funcionalidade estava atrelado a prazos externos bem curtos e lá estava eu, tentando gerenciar o Titanic. Já vi acontecer com diversas devs em diversas empresas.

{{<figure src="https://media.giphy.com/media/SLbZ0D6YoO7io/giphy-downsized-large.gif#center" width="250px" alt="Um gif com o personagem Jack Sparrow no topo de um mastro de um navio que afunda">}}

Aí vem uma parte difícil: conseguir comunicar abertamente e claramente o que está acontecendo. Um iceberg enorme que está no seu rumo é ruim. Mas fica ainda pior se o olheiro, com vergonha de não ter visto ele se aproximar, decide não comunicar que ele está ali.

Quando o meu iceberg estava vindo, nítido e claro na minha frente, a minha primeira reação foi de pânico. Eu tive a certeza que claramente eu não servia para aquilo. Que se esse projeto estava tão caótico (e atrasado) eu não poderia ser de fato a pessoa para liderá-lo. Mas como diria o velho ditado… “mar calmo nunca fez bom marinheiro”. Eu percebi que liderar bem um projeto não era liderar um bom projeto, mas liderar um projeto quando tudo dá errado. Levantei as mangas e comecei a lidar com o meu iceberg até que o navio estivesse de volta ao rumo, são e salvo.

.  .  .

Da mesma forma que saber exatamente como funcionam os botões e controles de um navio, não significa que você consiga de fato manobrá-lo. Isso também é válido aqui, no nosso mundo. Saber programar um projeto complexo não é toda a habilidade que você precisa. Como você pode ver, o buraco é muito mais embaixo.

Enquanto eu pensava nessa palestra e construía essa analogia, comecei a pensar no que tudo isso significava. Se nós eu sou uma capitã, manobrando navios por mares revoltos e desafios escondidos, o que eu posso fazer para me tornar melhor? Que habilidade pode me levar mais longe e me tornar efetivamente a melhor capitã que eu posso ser?

Quando eu comecei a refletir sobre isso, uma habilidade me veio em mente. Algo que jamais tivesse visto antes como uma habilidade fundamental para o meu papel, mas quanto mais eu pensava, mais fazia sentido. Pra mim, essa habilidade é a empatia.

Por empatia eu quero dizer:

{{<figure src="/assets/img/posts/o_que_raios/62.jpg#center" alt="Uma tela onde lê-se 'Empatia é a arte de, de maneira imaginária se colocar no lugar de outra pessoa, entendendo seus sentimentos e perspectivas e usando-os para guiar suas ações'">}}

Existem duas formas que podemos fazer isso: a primeira é a mais conhecida chamada *empatia afetiva*. Nesse caso, a gente compartilha uma resposta emocional. Um exemplo claro de empatia afetiva é quando alguém que você ama sofrendo e é como se você se sentisse da mesma forma.

O tipo de empatia que eu vi como parte do meu trabalho é o segundo tipo: a *empatia cognitiva*. Nesse tipo de empatia a gente passa a pegar a perspectiva alheia e tomá-la como nossa. Nesse caso é necessário reconhecer que outras pessoas tem diferentes gostos, experiências e visões de mundo das nossas.

Vamos olhar com calma todos os pontos que conversamos quando estamos liderando um projeto. Vocês conseguem ver a empatia exalando em cada uma dessas etapas?

Quando eu falei que eu preciso entender o porque eu estou fazendo a tarefa que eu faço, é porque eu tenho empatia com meu eu futuro. É apenas com projetos relevantes, desafiadores e de impacto é que eu vou conseguir galgar minha carreira para direções mais altas.

Não só isso, mas é  apenas perguntando e entendendo as motivações de um projeto que eu consigo começar a entender razões, analisar as escolhas por trás de cada decisão e assim começar a construir a bagagem de experiência necessária para que eu, um dia, possa fazer o mesmo quando estiver nesta posição.

Quando estamos definindo o escopo e quebrando requisitos em tarefas menores e bem delineadas estamos tendo empatia com nosso time. Muitas vezes quem define o escopo não é quem trabalha em uma tarefa. Então tê-las bem dividas, com claridade no que precisa ser feito e organização é ter certeza que você está deixando o seu time na melhor posição possível para conseguir ter sucesso nesse projeto, mesmo que você deixe o projeto por qualquer motivo que seja.

E quando falamos em prazos, aquela gordurinha extra que deixamos nada mais é que saber que as coisas acontecem, e dar espaço e tempo para que as pessoas respirem, trabalhem tranquilamente e tenham tempo para lidar com quaisquer pequenas incertezas que apareçam. Porque elas tem mais chances de acontecer quando estamos falando de projetos longos.

Tudo isso gera bons frutos no seu time, mesmo que pareça, a princípio, que o trabalho é irrelevante.

Comunicação talvez seja o ponto em que você mais associe com empatia, já que comunicação é pensar nos múltiplos times e pessoas envolvidas no projeto. É saber que todas as pessoas que vão se beneficiar da comunicação clara e efetiva, estão com seus desejos e ansiedades atrelados ao projeto e que saber o que está acontecendo, seja para o bem ou seja para o mal, vai deixá-las mais aptas a lidar com as circunstâncias.

Da mesma forma, definir prioridades e garantir que a gente consegue entregar algo de valor o mais rápido possível é ter empatia com seu cliente. Se estamos investindo nosso tempo em construir algo para melhorar a vida de alguém, queremos que esse problema seja resolvido o mais rápido possível, certo? Como desenvolvedores, talvez estejamos na melhor posição possível para conseguir analisar o que de fato é possível construir primeiro e mais rápido.

Saber analisar o que é viável e o que é prioridade dentro do contexto onde v*ocê está é quase um super poder*: você ajuda o seu cliente, você ajuda o seu time e ainda permite desenvolver um pensamento criativo mais aguçado, já que você está vendo problemas de uma perspectiva completamente nova!  Tudo em um pequeno ato, que talvez não te demore mais do que algumas horas para conceber.

Quanto a gente documenta os aprendizados a gente está tendo empatia com o futuro tanto nosso quanto o de pessoas que talvez ainda nem trabalhem conosco. É só sentando o bumbum na cadeira, e gastando tempo pensando nos nossos aprendizados e documentando nossas descobertas que podemos fazer com que o futuro seja melhor do que o que estamos vivendo agora.


{{<figure src="/assets/img/posts/o_que_raios/68.jpg#center" alt="Uma tela onde vê-se várias etapas e a empatia que ela necessita. Em sequência: 1) Entender o problema exige empatia com o meu eu futuro 2) definir o escopo em pequenas tarefas exige empatia com meu time 3) comunicação sobre incertezas exige empatia com as pessoas envolvidas no projeto 4) definição de prioridades exige empatia com meus clientes 4) documentação de aprendizados exige empatia com o meu futuro ">}}

Finalmente, lidar com as incertezas vai exigir de você um pouco de todas os níveis de empatia que conversamos até aqui. Cada iceberg no seu trajeto, seja ele grande ou pequeno, é como um pequeno projeto, com todas as esferas que conversamos até agora.

O que eu estou fazendo aqui, no fim das contas, é ter empatia. De múltiplas formas, em múltiplos momentos e em múltiplas esferas.

Quando você escreve um código que é bom, você está tendo empatia com as pessoas que vão manter esse código. Quando você gasta o seu tempo dando um bom feedback ao seu colega, você está tendo empatia com a profissional que essa pessoa pode se tornar.

Quando introduzimos uma nova configuração num sistema e ela quebra no meio da noite e a pessoa que está de plantão acorda no meio da noite, com a produção quebrada e o sono embaraçando a mente e ela não encontra um documento que explique como consertar esse problema… É a falta de empatia com essa pessoa que é a causa da frustração.

Quando fazemos um comentário ríspido durante uma revisão de código, é a falta de empatia que nos distancia e cria barreiras.

Quando uma nova pessoa entra no time e é “jogada no fogo”, é a falta de empatia que a empurra pra fora desse mundo.

E além disso, temos que também ter empatia com quem nós éramos no passado.

Quem nunca chegou em um código antigo, que faz uma volta esquisita e tem uma complexidade desnecessária, e pensou: “isso aqui não faz o menor sentido! Porque raios alguém fez uma coisa dessas?”. A gente vai lá, coça a cabeça enquanto os olhos se enchem de frustração.

Ao mesmo tempo, quantas vezes estamos fazendo um código e não conseguimos nos esquivar dessas curvas e quinas que temos que colocar? Quantas vezes tentamos alinhar expectativas e opiniões diferentes?

Quando olhamos um código passado e pensamos isso, a realidade é muito diferente do que quando ele foi criado. O conhecimento e compreensão do tema hoje, que faz a gente ver um caminho mais fácil a trilhar, era completamente obscuro e inalcançável há alguns anos atrás.

Eu, como talvez muitas de vocês, sempre achei que empatia era um dom: ou você tem, ou você não tem. No entanto, os estudos mais recentes mostram que empatia é como uma habilidade musical: algumas pessoas nascem com uma vocação maior, mas todos nós podemos treinar e nos aperfeiçoar.

Existem inúmeros livros sobre como desenvolver e melhorar a empatia, e eu recomendo o “Empathy: why it matters and how to get it”. Mas eu queria dar alguns exemplos que eu vivi recentemente.

Por exemplo, eu trabalho com um software que ajuda a calcular imposto sobre vendas. São raras as vezes em que eu falo isso e a resposta é “caramba que interessante!”. Mas eu gosto bastante porque é um assunto denso e complexo, nada fácil de ser transformado em código. Só que, após muito tempo trabalhando com esse tópico, é muito fácil assumir que as pessoas sabem o tanto que sabemos e é muito fácil começar a criar um produto difícil de ser usado.

Para empatizar com nossos clientes, ao menos uma vez por semestre nós fazemos sessões onde todas as pessoas do time, sejam elas novatas ou não, tentam usar o nosso produto do zero, tentando pensar como um cliente pensaria. Nós fazemos anotações de que partes foram difíceis, quais documentações eram confusas e que partes do sistema não faziam sentido. Além de gerar uma lista de coisas que podemos melhorar, esse exercício também nos ajuda a não fazer um produto pra nós mesmos, que estamos todo dia falando sobre o assunto.

Por conta dessa complexidade toda, também temos que ter empatia com quem chega depois, já que é natural ter uma curva de aprendizado mais lenta. Outro dia um colega comentou comigo que uma determinada parte do sistema era muito obscura para ele e ele sempre estava inseguro de entrar de plantão, já que ele teria que lidar com problemas ali. Ele queria aprender mais mas achava a documentação sobre o assunto muito densa.

Sabendo que esse problema não era incomum, propus ao meu gerente que fizéssemos um treinamento um pouco mais… mão na massa. Eu peguei a parte do sistema que era a mais obscura e introduzi um bug bem pequeno em um ambiente de testes. Para garantir que todos estariam envolvidos, marquei uma reunião com o time todo e apresentei o problema da mesma forma que um usuário nosso faria.

O time foi formando duplas para encontrar o problema, compartilhando técnicas de encontrar o problema, ferramentas que poderiam ser usadas e que documentos poderiam ajudar nesse caso. Foi um exercício interessante em que todos aprenderam um pouquinho sobre como encontrar problemas mas também conseguimos conversar sobre o código de maneira muito mais prática, já que todo mundo teve contato com ele antes.

Bom, espero que tenha ficado um pouco mais fácil entender como aplicar empatia com seu cliente e com seu time, mas ainda tem pelo menos mais uma peça faltando aqui: nós mesmas.

Todas nós queremos, de uma maneira ou de outra, sermos melhor no que fazemos, certo? E como eu falei no começo da conversa… é muito fácil, especialmente em um dia ruim, esquecer de tudo o que fizemos e do quanto lutamos para chegar onde estamos. [Em 2020 eu fiz uma palestra](https://leportella.com/pt-br/pybr2020/) em que eu apresentava o conceito de “Documento do Orgulho”. Esse é um documento que eu escrevo por semestre, anotando sempre o que eu quero alcançar no próximo semestre e tudo o que eu fiz nesse semestre. Eu compartilho esse documento com o meu gerente e meus colegas, para que todos se lembrem de tudo o que eu fiz quando chega a hora de avaliar minha performance.

O que é isso se não sou eu tendo empatia com o meu futuro e a minha carreira? De que adianta me esforçar se eu não lembro o que eu fiz ou se eu não sei pra onde eu vou?

Por muitos anos a tecnologia foi um campo essencialmente lógico, técnico, masculino. O “hard skills” era o que importava e qualquer coisa “soft” só poderia ser fraca, desnecessária e até desprezível. Mas a realidade é muito diferente.

Está mais do que na hora de percebermos que o desenvolvimento de software, é um esporte de equipe tanto quanto remo. O Google fez uma pesquisa para tentar entender o que torna um time eficaz. A resposta? Como um time se comporta é muito mais relevante do quem que está no time. Times precisa estar em sintonia para poder chegar à melhor performance e o único jeito de conseguir isso é cultivando habilidades que vão muito além de código. É cultivando empatia.

{{<figure src="/assets/img/posts/o_que_raios/76.jpg#center" alt="Uma tela onde está escrito 'desenvolvimento de software é como remo. é um esporte de equipe que requer habilidades e sincronização'">}}


É com empatia que podemos construir times eficazes. É com empatia que podemos construir produtos verdadeiramente encantadores. É apenas com empatia que nós podemos quem nós somos, porque sabemos que seremos bem acolhidas.

O mundo moderno é complexo, é lindo, é diverso, é dinâmico. As verdades de hoje são completamente transformadas amanhã. Nada puramente técnico e frio consegue resolver os problemas que estamos tentando resolver hoje.

O código é o que nos move. É nossa paixão e é o que nos traz aqui hoje, nessa sala. Programar é o que nos faz nos apaixonar e querer construir nossa carreira. Mas é a empatia que nos transforma em algo maior. É a empatia que nos faz evoluir e chegar mais longe. É a empatia que nos faz, de fato, sermos desenvolvedoras excepcionais.

{{<figure src="/assets/img/posts/o_que_raios/78.jpg#center" alt="Uma tela onde está escrito 'Código é o que nos move. Empatia é o que nos torna excepcionais.'">}}
