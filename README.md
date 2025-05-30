# 🐳 Infraestrutura com Containers (Flask + PostgreSQL + Docker Compose)

Este projeto implementa uma aplicação Python (Flask) containerizada, que se conecta a um banco de dados PostgreSQL, também em container. Toda a infraestrutura é orquestrada com Docker Compose, com ambientes separados para desenvolvimento e produção, seguindo boas práticas de segurança, versionamento e organização.

---

## ✅ Funcionalidades

- Aplicação web em Flask para cadastro de usuários.
- Banco de dados PostgreSQL containerizado.
- Ambientes isolados para **desenvolvimento** e **produção**.
- Uso de variáveis de ambiente com `.env`.
- Imagem da aplicação publicada no Docker Hub.
- Segurança com Dockerfile multistage e execução sem root.
- Análise de imagem com Docker Scout ou Trivy.
- Gerenciamento visual do banco com **DBeaver**.

---

## 📁 Estrutura do Projeto

infra/
├── app/
│ ├── app.py
│ ├── requirements.txt
│ └── Dockerfile
├── docker-compose.dev.yml
├── docker-compose.prod.yml
├── .env.dev
└── .env.prod

yaml
Copy
Edit



2. .env.dev

# .env.dev
POSTGRES_USER=devuser
POSTGRES_PASSWORD=devpass
POSTGRES_DB=usuarios_dev

.env.prod:

# .env.prod
POSTGRES_USER=produser
POSTGRES_PASSWORD=prodpass
POSTGRES_DB=usuarios_prod

3. Ambiente de desenvolvimento

docker compose -f docker-compose.dev.yml up -d
📌 Isso criará:

A aplicação Flask em localhost:8080

O banco PostgreSQL escutando na porta 5432

4. Acessar:

http://localhost:8080: Formulário de cadastro

http://localhost:8080/status: Status da API

5. utilização do DBeaver

Campo	Valor
Host	localhost
Port	5432
Database	usuarios_dev
Username	devuser
Password	devpass

6. Publicação da imagem no Docker Hub

docker build -t renanafs/flaskapp:1.0 ./app
docker push renanafs/flaskapp:1.0

7. Ambiente de produção

docker compose -f docker-compose.prod.yml up -d
O ambiente de produção expõe a aplicação em localhost:80

8. Análise de segurança da imagem

Com Docker Scout:
docker scout quickview renanafs/flaskapp:1.0

Dockerfile otimizado

Multistage build

Imagem base leve (python:3.11-alpine)

Remoção de dependências desnecessárias

Usuário não-root

🔒 Segurança e boas práticas aplicadas

Execução com usuário não-root dentro do container.

Separação de ambientes com redes dedicadas (dev_net, prod_net).

Uso de .env para não expor senhas.

Dockerfile com imagem leve e sem dependências desnecessárias.

Versionamento da imagem no Docker Hub.

🔍 Boas práticas aplicadas

Estrutura de diretórios clara

Volumes nomeados para persistência

Uso de DBeaver como GUI segura

Versionamento da imagem Docker

📸 Evidência no Docker Hub
Imagem disponível em: https://hub.docker.com/r/renanafs/flaskapp/tags

