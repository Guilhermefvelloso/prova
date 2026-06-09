API de Gerenciamento de Tarefas

Descrição

API desenvolvida em Django para gerenciamento de usuários e tarefas.

O sistema permite realizar operações de cadastro, consulta, alteração e exclusão de registros (CRUD), utilizando banco de dados PostgreSQL e execução via Docker.

Tecnologias Utilizadas

- Python
- Django
- PostgreSQL
- Docker
- Docker Compose

Estrutura do Projeto

backend/
├── config/
├── tarefas/
├── usuarios/
├── manage.py
├── requirements.txt
└── Dockerfile

docker-compose.yml
README.md

Como Executar

1. Clonar o repositório

git clone https://github.com/Guilhermefvelloso/prova.git
cd prova

2. Iniciar os containers

docker compose up -d

3. Executar as migrações

docker compose exec web python manage.py migrate

4. Criar um superusuário

docker compose exec web python manage.py createsuperuser

5. Acessar o sistema

Painel administrativo:

http://localhost:8000/admin

Docker Hub

Imagem publicada:

guilhermefvelloso/prova-web:v1

Download da imagem:

docker pull guilhermefvelloso/prova-web:v1

Funcionalidades

Usuários

- Criar usuário
- Consultar usuário
- Atualizar usuário
- Excluir usuário

Tarefas

- Criar tarefa
- Consultar tarefa
- Atualizar tarefa
- Excluir tarefa

Autor

Guilherme Ferreira Velloso

Disciplina: Laboratório de Programação Back-End

Professor: Alvaro Leiroz
