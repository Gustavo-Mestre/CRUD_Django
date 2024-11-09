# CRUD_Django


# Projeto Django - Aplicação de Gerenciamento de Livros

Este projeto é uma aplicação Django para gerenciar livros, incluindo funcionalidades de criação, listagem, edição e exclusão. 
O projeto utiliza Class-Based Views (CBVs) e o Django Admin para gerenciar dados.

## Estrutura do Projeto

### Modelos

- **Category**: Representa a categoria de um livro.
- **Author**: Representa o autor de um livro.
- **Book**: Representa o livro em si, com relações de chave estrangeira para `Author` e `Category`.

### Views

- **BookListView**: Lista todos os livros.
- **BookCreateView**: Exibe o formulário para adicionar um novo livro.
- **BookUpdateView**: Exibe o formulário para editar um livro existente.
- **BookDeleteView**: Exibe uma página de confirmação para excluir um livro.

## Configuração do Ambiente

### 1. Pré-requisitos

Certifique-se de que você tem o [Python](https://www.python.org/downloads/) instalado. Este projeto requer Python 3.x.

### 2. Criar e Ativar um Ambiente Virtual

Para manter as dependências isoladas, crie um ambiente virtual:

```bash
python -m venv myenv
```

Ative o ambiente virtual:

- **Windows**:
  ```bash
  myenv\Scripts\activate
  ```
- **Mac/Linux**:
  ```bash
  source myenv/bin/activate
  ```

### 3. Instalar Dependências

Instale o Django e outras dependências listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

Se o arquivo `requirements.txt` ainda não existir, crie-o com o seguinte conteúdo:

```text
Django>=3.2,<4.0
django-crispy-forms
```

## Configuração do Projeto Django

### 1. `settings.py`

Certifique-se de que seu `setup/settings.py` contém as seguintes configurações:

```python
from pathlib import Path
from decouple import config, Csv
from dj_database_url import parse as db_url


BASE_DIR = Path(__file__).resolve().parent.parent




SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", cast=bool, default=False)


ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

# Application definition

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

THIRD_PARTY_APPS = [
    "crispy_forms",
    "crispy_bootstrap5",
]

MY_APPS = [
    "books.apps.BooksConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + MY_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "setup.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "setup.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": config(
        "DATABASE_URL",
        default=f'sqlite:///{BASE_DIR / "db.sqlite3"}',
        cast=db_url,
    )
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "pt-br"

TIME_ZONE = "America/Sao_Paulo"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

```

### 2. Criar e Aplicar as Migrações

```bash
python manage.py makemigrations
python manage.py migrate
```

### 3. Criar um Superusuário para o Admin

```bash
python manage.py createsuperuser
```

### 4. Iniciar o Servidor de Desenvolvimento

```bash
python manage.py runserver
```

## Estrutura dos Arquivos

### `models.py`

```python
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Book(models.Model):
    title = models.CharField(verbose_name="título", max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Autor")
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, verbose_name="Categoria"
    )
    published_date = models.DateField(verbose_name="Data de Publicação")

    def __str__(self):
        return self.title
```

### `views.py`

```python
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "books/book_list.html"
    context_object_name = "books"

class BookCreateView(CreateView):
    model = Book
    fields = ["title", "author", "category", "published_date"]
    success_url = reverse_lazy("book_list")
    template_name = "books/book_form.html"

class BookUpdateView(UpdateView):
    model = Book
    fields = ["title", "author", "category", "published_date"]
    success_url = reverse_lazy("book_list")
    template_name = "books/book_form.html"

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy("book_list")
    template_name = "books/book_confirm_delete.html"
```

### URLs

```python
from django.contrib import admin
from django.urls import path
from books.views import BookListView, BookCreateView, BookUpdateView, BookDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", BookListView.as_view(), name="book_list"),
    path("create", BookCreateView.as_view(), name="book_create"),
    path("update/<int:pk>", BookUpdateView.as_view(), name="book_update"),
    path("delete/<int:pk>", BookDeleteView.as_view(), name="book_delete")
]
```

### Templates

#### `base.html`: 

```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    
    <title>{% block page_title %}{% endblock page_title %}</title>

    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" crossorigin="anonymous">
</head>
<body>
    <nav class="navbar navbar-dark bg-dark mb-5">
        <div class="container-fluid">
            <a class="navbar-brand" href="{% url 'book_list' %}">Livros</a>
        </div>
    </nav>

    <main class="container center">
      {% block content %}
      {% endblock content %}
    </main>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
</body>
</html>
```

#### `books/book_list.html`

```html
{% extends "base.html" %}

{% block page_title %}Lista de Livros{% endblock page_title %}

{% block content %}
    <h1>Lista de Livros</h1>
    <a href="{% url 'book_create' %}" class="btn btn-primary">Adicionar Novo Livro</a>
    <ul>
        {% for book in books %}
            <li>{{ book.title }} - {{ book.author }}
            <a href="{% url 'book_update' book.pk %}" class="btn btn-secondary btn-sm">Editar</a>
            <a href="{% url 'book_delete' book.pk %}" class="btn btn-danger btn-sm">Excluir</a>
            </li>
        {% endfor %}
    </ul>
{% endblock %}
```

#### `books/book_form.html`

```html
{% extends "base.html" %}
{% load crispy_forms_tags %}

{% block page_title %}
    {% if book.pk %}Editar Livro{% else %}Novo Livro{% endif %}
{% endblock page_title %}

{% block content %}
    <h1>{% if book.pk %}Editar Livro{% else %}Novo Livro{% endif %}</h1>
    <form method="POST">
        {% csrf_token %}
        {{ form|crispy }}
        <button type="submit" class="btn btn-primary">Salvar</button>
    </form>
{% endblock %}
```

#### `books/book_confirm_delete.html`

```html
{% extends 'base.html' %}

{% block page_title %}Exclusão de Livro{% endblock page_title %}

{% block content %}
    <h1>Excluir Livro?</h1>

    <p>Tem deseja que deseja excluir o livro <strong> {{ book.title}}</strong>?</p>

    <form method="POST">
        {% csrf_token %}

        <button type="submit" class="btn btn-danger">Excluir</button>
        <a href="{% url 'book_list' %}" class="btn btn-primary">Cancelar</a>
    </form>
{% endblock content %}
```

## Executar a Aplicação

1. Inicie o servidor Django:

   ```bash
   python manage.py runserver
   

2. Acesse a lista de livros: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
