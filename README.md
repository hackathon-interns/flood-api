# Django Setup Template

Este é um template básico para projetos Django, contendo uma configuração inicial que eu considero a melhor prática. Ele inclui todas as bibliotecas e configurações que frequentemente utilizo em meus projetos.

## Sumário

- [Funcionalidades](#funcionalidades)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Uso](#uso)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Contribuição](#contribuição)
- [Licença](#licença)

## Funcionalidades

- Configuração inicial do Django
- Suporte para ambiente virtual
- Configurações de banco de dados
- Autenticação de usuários
- Configurações de segurança
- Ferramentas para desenvolvimento e depuração
- Suporte para testes automatizados

## Pré-requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados:

- Python 3.8+
- pip
- virtualenv

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/pedroandrade03/django-setup-template.git
    cd django-setup-template
    ```

2. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate   # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

4. Configure as variáveis de ambiente:

    Crie um arquivo `.env` na raiz do projeto e adicione as seguintes variáveis:

    ```env
    DEBUG=True
    SECRET_KEY=your-secret-key
    DATABASE_URL=sqlite:///db.sqlite3
    ```

5. Execute as migrações do banco de dados:

    ```bash
    python manage.py migrate
    ```

6. Crie um superusuário:

    ```bash
    python manage.py createsuperuser
    ```

7. Inicie o servidor de desenvolvimento:

    ```bash
    python manage.py runserver
    ```

## Configuração

Para personalizar o template para o seu projeto, você pode modificar os seguintes arquivos ou criar novos:

- `app/`: Aplicação principal do projeto.
- `core/`: Módulo principal do projeto.
- `user/`: Aplicação de autenticação de usuários.

## Uso

Para iniciar o servidor de desenvolvimento, use:

```bash
python manage.py runserver
```
