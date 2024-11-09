import os
from django.core.management.base import BaseCommand
from django.db import connection
from django.conf import settings


class Command(BaseCommand):
    help = "Importa dados de livros, autores e categorias a partir de um arquivo SQL"

    def handle(self, *args, **kwargs):
        # Definir o caminho do arquivo SQL
        sql_file_path = os.path.join(settings.BASE_DIR, "data", "import_books.sql")

        # Verificar se o arquivo existe
        if not os.path.exists(sql_file_path):
            self.stdout.write(
                self.style.ERROR(f"Arquivo SQL não encontrado: {sql_file_path}")
            )
            return

        # Ler e executar o conteúdo do arquivo SQL
        with open(sql_file_path, "r") as sql_file:
            sql_script = sql_file.read()

        with connection.cursor() as cursor:
            cursor.executescript(sql_script)

        self.stdout.write(self.style.SUCCESS("Dados importados com sucesso"))
