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
