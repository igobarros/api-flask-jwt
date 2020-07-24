## API COM FLASKRESTFULL E JWT


### Esse projeto trata-se de uma simples API desenvolvida usando as bibliotecas flask_restfull, flask_sqlalchemy e JWT (JSON Web Token).


### Dependências
##### Vamos executar os comandos a baixo para configurar o ambiente

```bash
$ python3 -m pip install pipenv
$ pipenv sync --dev
$ pipenv shell
$ export FLASK_APP=main
```

	1 - A segundo linha de comando instala todas as dependências do projeto que contém no arquivo ```Pipfile.lock``` .
	2 - A terceiro linha de comando ativa o ambiente virtual do pipenv.
	3 - Por último, a próxima linha de comando informa ao flask qual arquivo(script) será usado quando o flask for executado, então estamos passando por variável de ambiente ```FLASK_APP``` qual arquivo será executado quando o flask for carregado.

##### Configurações do banco de dados
Nesse projeto vamos trabalhar com o SGBD postgresql. Mas nada impede que você use qualquer outro SGBD de sua escolha. Isso porque estamos usando a biblioteca flask_sqlalchemy para se conectar ao banco de dados, o sqlalchemy performance como uma ORM (Object Relational Mapper) que é uma forma de usar orientação a objetos para manipulação dos bancos relacionais. Outra vantagem é que essa biblioteca trabalha com drivers, dando a possibilidade de usar o mesmo código para qualquer banco de dados relacionais, que suporte,  sem ter que fazer grande modificações.

Então vamos lá:

1 - Se já tem o postgresql instalado e configurado na sua máquina execute os comandos abaixo:
```bash
$ sudo -u postgres psql
=# CREATE DATABASE flask_contacts;
=# \connect flask_contacts;
```

2 - O próximo passo é configurar o URL de conexão com o banco:
No arquivo ```config.py``` altere as credenciais de acordo com as do seu banco

```py
SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/name_db'
```

3 - Agora iremos configurar as migrações da modelagem do banco desenvolvida no projeto para o postgresql.
Se todos os passos acima foram executados com êxito a criação do banco <flask_contacts> e as credenciais:

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```

	4 - Execute o projeto

```bash
$ flask run
```

### Docker
Podemos isolar nossa aplicação em um container docker com o comando:

```bash
$ docker run --name pglocal -e "POSTGRES_PASSWORD=admin" -p 5432:5432 -d postgres
```

Configurando o banco:

```bash
$ docker exec -it pglocal bash
=# psql -U postgres
=# \l
=# CREATE DATABASE flask_contacts;
=# \connect flask_contacts;
```

No arquivo ```config.py``` use essas configurações

```py
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin123@localhost/flask_contacts'
```

Rodando as migrações

```bash
$ flask db init
$ flask db migrate
$ flask db upgrade
```

Ativar o container
```
$ docker start pglocal
```

### Testando a API

**USERS**

POST
Criando um novo usuário
```bash
$ curl -v -d '{"username":"admin", "password": "12345"}' -H "content-type: application/json"  http://localhost:5000/api/v1/register
```

POST
Realizando o login para retornar o ACESS_TOKEN
```
curl -v -d '{"username":"admin", "password": "12345"}' -H "content-type: application/json"  http://localhost:5000/api/v1/login
```

**CONTATOS**

POST
Criando um novo contato
```bash
$ curl -X POST -d '{"name":"Geovana", "cellphone": "11993447755"}' -H "content-type: application/json" -H "authorization: Bearer {ACCESS_TOKEN}" http://localhost:5000/api/v1/contacts
```

GET
Retornando os contatos cadastrados
```bash
$ curl -X GET -H "Accept: application/json" -H "Authorization: Bearer {ACCESS_TOKEN}" "http://localhost:5000/api/v1/contacts"
```

PUT
Alterando um contato
```bash
$ curl -X PUT -d '{"id": 1, "Nome": "Geovana", "cellphone": "129843274"}' -H "content-type: application/json" -H "authorization: Bearer {ACCESS_TOKEN}" http://localhost:5000/api/v1/contacts
```

DELETE
Deletando um contato
```bash
$ curl -X DELETE -d '{"id": 1}' -H "content-type: application/json" -H "authorization: Bearer {ACCESS_TOKEN}" http://localhost:5000/api/v1/contacts
```

### Contato
E-mail: igopbarros@gmail.com