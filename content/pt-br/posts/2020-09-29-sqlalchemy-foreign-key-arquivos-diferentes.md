---
layout: post
title: "Adicionando relacionamento em tabelas pré-existentes no SQLAlchemy"
categories:
  - banco de dados
tags:
  - python
  - outreachy
  - sqlalchemy
  - orm
  - banco de dados
  - SQL
  - Project Jupyter
featured-img: alone-anime
slug: sqlalchemy-relacionamento
translationKey: sqlalchemy-relationship
date: 2020-09-29T11:21:52-05:00
---

[Neste texto](https://leportella.com/tutorial-basico-sqlalchemy.html) você consegue ter uma ideia pequena de como o SQLAlchemy funciona. No entanto, todo o meu estudo dessa biblioteca aconteceu por causa de um problema que eu demorei muito tempo pra conseguir solucionar. 

Como o problema era muito complexo e eu não achei que cabia no outro texto, decidi escrever esse aqui dedicado a ele. Aqui vai :)
<!--more-->

Enquanto eu estava criando o [Native Authenticator](https://github.com/jupyterhub/nativeauthenticator/) eu percebi que eu ia precisar guardar uma informação sobre o meu usuário que não estava disponível na tabela padrão `User`. Informações tipo email e senha, por exemplo. O [JupyterHu](https://github.com/jupyterhub/jupyterhub/blob/master/jupyterhub/orm.py#L111) ja tinha uma classe `User` que era mais ou menos assim: 

While I was creating the [Native Authenticator](https://github.com/jupyterhub/nativeauthenticator/) I realized that I needed to store some information about my user that wasn't available in the default `User` table. Informations such as email or password, for instance. The [JupuyterHub `User` class](https://github.com/jupyterhub/jupyterhub/blob/master/jupyterhub/orm.py#L111) was like this:

```python
# jupyterhub/orm.py

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(Unicode(255), unique=True)

```

Eu decidi, então, criar uma classe chamada  `UserInfo` que iria guardar todas as informações adicionais que eu queria. Minha classe ficou assim:

```python
# nativeauthenticator/orm.py 

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class UserInfo(Base):
    __tablename__ = 'users_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

```

Uma vez que essa classe estava pronta, tudo o que eu precisava era adicionar essa tabela ao meu banco de dados. Então eu adicionei a criação dela no método `__init__` do meu authenticador. Dessa forma:

```python
# nativeauthenticator/nativeauthenticator.py

class NativeAuthenticator(Authenticator):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        inspector = inspect(self.db.bind)
        if 'users_info' not in inspector.get_table_names():
            UserInfo.__table__.create(self.db.bind)

```

Obs: *self.db.bind* é o SQLAlchemy *engine*.

Primeiro verifiquei se minha tabela já não estava lá (caso contrário, receberia um erro) e, se não estiver, ai sim o comando pra criar a tabela. Tudo estava funcionando até agora :)

O problema começou quando decidi adicionar um relacionamento entre `UserInfo` e `User`.

Por algum motivo, não consegui fazer funcionar. A tabela `UserInfo` nunca encontrava a tabela `User` e recebia este erro:

> NoReferencedTableError: Foreign key associated with column 'product.user_id' could not find table 'user' with which to generate a foreign key to target column 'id'.

*Tradução*: NoReferencedTableError: A chave estrangeira associada à coluna 'product.user_id' não pôde encontrar a tabela 'user' com a qual gerar uma chave estrangeira para a coluna de destino 'id'.

Eu passei um bom tempo no [Stack Overflow](https://stackoverflow.com/) e depois de muito tempo [eu escrevi uma issue pedindo ajuda](https://github.com/jupyterhub/nativeauthenticator/issues/26). Foi quando o [André](https://github.com/dedeco) me perguntou se eu estava usando a mesma instância de `Base` pra criar os dois modelos. Adivinha? Não estava. 

Portanto, a primeira coisa que você deve fazer ao criar duas classes para o mesmo `engine` do `SQLAlchemy` é  **usar o mesmo`Base` em todos os modelos**. Parece trivial, mas não é. Aqui está a solução:

```
# nativeauthenticator/orm.py 

from jupyterhub.orm import Base
from sqlalchemy import Column, Integer, String

class UserInfo(Base):
    __tablename__ = 'users_info'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

```

Depois disso, você pode adicionar os atributos para o relacionamento em sua classe:

```
class UserInfo(Base):
    ...
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

```

Agora você pode simplesmente adicionar a tabela e ela funcionará!

No entanto, desta forma você não será capaz de ver quais instâncias de `UserInfo` estão conectadas ao seu `User`, porque apenas `UserInfo` conhece `User`. Portanto, você deve adicionar um relacionamento à classe `User`. Como não estamos adicionando na criação da classe `User` (porque eu não queria alterar o arquivo original), nós o adicionamos à classe no momento em que você define o relacionamento:

```
User.info = relationship(UserInfo, backref='users')

```

Veja um exemplo completo com as duas classes:

{{<figure src="https://raw.githubusercontent.com/leportella/sqlalchemy-basics-post/master/gifs/jupyterhub_example.gif#center">}}

Pronto! Tudo funciona!

Agradecimentos especiais ao [André](https://github.com/dedeco), [Yuvi](https://github.com/yuvipanda) e [Pastore](https://github.com/apast) por toda a ajuda ❤️!