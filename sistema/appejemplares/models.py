from typing import Any
from django.db import models

# Create your models here.

#python manage.py makemigrations  <---- lee el archivo models y crea un archivo de migracion
#python manage.py migrate  <---- toma las migraciones pendienes y las vuelca en la BBDD
class Libro(models.Model):

    CATEGORIAS_CHOICES = [
        ('novelas', 'Novelas'),
        ('suspenso', 'Suspenso'),
        ('historia', 'Historia'),
        ('test', 'Test'),
        # Agrega más opciones según sea necesario
    ]

    id = models.AutoField(primary_key=True)
    isbn = models.CharField(max_length=13, unique=True)
    titulo = models.CharField(max_length=100, verbose_name='Título', null=False, blank=False)
    autor = models.CharField(max_length=100, verbose_name='Autor', null=False, blank=False)
    categoria = models.CharField(max_length=50, verbose_name='Categoría', choices=CATEGORIAS_CHOICES)
    ubicacion = models.CharField(max_length=20, verbose_name='Ubicación', null=False, blank=False)
    ejemplares_disponibles = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='imagenes/', verbose_name='Imagen', null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)

    def __str__(self):
        fila = "Título: " + self.titulo + " - " + "Descripción: " + " " + self.descripcion
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()

    class Meta:
        verbose_name = "Datos_Libros"
