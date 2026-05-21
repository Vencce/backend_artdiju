# Artdiju - Backend

Este repositório contém a API robusta da plataforma Artdiju, desenvolvida com **Python** e o framework **Django**. A API é responsável pela gestão de dados, autenticação de utilizadores, processamento de subscrições e servir de ponte para o catálogo de produtos apresentado no frontend.

## 🛠️ Tecnologias Utilizadas

* **Python (3.x)**: Linguagem de programação base.
* **Django**: Framework web de alto nível.
* **Django Rest Framework (DRF)**: Para a construção de uma API RESTful flexível.
* **SQLite**: Base de dados leve utilizada para persistência de dados.
* **Django Cors Headers**: Para permitir o consumo da API pelo frontend em domínios diferentes.
* **Pillow**: Para processamento e gestão de imagens de produtos.

## 📁 Estrutura do Projeto

* **`config/`**: Definições principais do projeto, incluindo configurações de segurança, base de dados e rotas globais.
* **`core/`**: Aplicação principal que contém a lógica de negócio:
    * **`models.py`**: Definição das tabelas de `Product` (Produtos), `Subscriber` (Subscritores) e categorias.
    * **`serializers.py`**: Transformação de objetos complexos em dados JSON.
    * **`views.py`**: Lógica de processamento das requisições para a vitrine e painel administrativo.
    * **`urls.py`**: Endpoints específicos da aplicação core.
* **`media/`**: Armazenamento local das imagens carregadas para os produtos.

## ✨ Funcionalidades da API

1.  **Gestão de Produtos**: CRUD completo (Criar, Ler, Atualizar, Eliminar) para o catálogo de arte.
2.  **Sistema de Destaques**: Filtro para produtos marcados como "Featured" na vitrine principal.
3.  **Controlo de Inventário**: Identificação de produtos já vendidos (`is_sold`).
4.  **Newsletter**: Endpoint para registo de e-mails de utilizadores interessados em atualizações.
5.  **Área Administrativa**: Interface integrada do Django para gestão rápida de dados por administradores.
6.  **CORS Configurado**: Preparado para comunicar de forma segura com o frontend Vue.js.

## 🛠️ Instalação e Execução

1.  **Pré-requisitos**: Ter o Python e o `pip` instalados.
2.  **Criar ambiente virtual**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate     # Windows
    ```
3.  **Instalar dependências**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Executar Migrações**:
    ```bash
    python manage.py migrate
    ```
5.  **Iniciar o servidor**:
    ```bash
    python manage.py runserver
    ```

## 🚀 Deploy

O projeto inclui um script `build.sh` para facilitar o processo de build em ambientes de produção ou plataformas de hospedagem.

---
Desenvolvido por **Vitor Ferreira**.
