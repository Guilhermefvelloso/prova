
PROVA - Sistema Django com Docker

Autor

Guilherme Ferreira Velloso

Descrição

Projeto desenvolvido utilizando Django, PostgreSQL e Docker.

Requisitos

- Docker Desktop instalado

Como executar

1. Baixar as imagens do Docker Hub:

docker pull guilhermefvelloso/prova-web:v1

2. Executar os containers:

docker compose up -d

3. Verificar os containers em execução:

docker compose ps

4. Executar as migrações do banco:

docker compose exec web python manage.py migrate

5. Criar o usuário administrador:

docker compose exec web python manage.py createsuperuser

6. Acessar o sistema:

http://localhost:8000/admin

Docker Hub

Imagem publicada:

guilhermefvelloso/prova-web:v1

Tecnologias Utilizadas

- Python
- Django
- PostgreSQL
- Docker
- Docker Compose
