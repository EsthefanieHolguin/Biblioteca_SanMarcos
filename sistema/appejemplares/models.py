from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _

class Libro(models.Model):
    CATEGORIAS_CHOICES = [
        ('novelas', 'Novelas'),
        ('suspenso', 'Suspenso'),
        ('historia', 'Historia'),
        ('test', 'Test'),
    ]

    isbn = models.CharField(primary_key=True, max_length=13)
    titulo = models.CharField(max_length=100, verbose_name='Título', null=False, blank=False)
    autor = models.CharField(max_length=100, verbose_name='Autor', null=False, blank=False)
    categoria = models.CharField(max_length=50, verbose_name='Categoría', choices=CATEGORIAS_CHOICES)
    ubicacion = models.CharField(max_length=20, verbose_name='Ubicación', null=False, blank=False)
    ejemplares_totales = models.IntegerField(default=0)
    ejemplares_disponibles = models.IntegerField(default=0)
    ejemplares_prestados = models.IntegerField(default=0)
    ejemplares_reservados = models.IntegerField(default=0)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)

    def __str__(self):
        return self.isbn

    def is_upperclass(self):
        return self.categoria in (choice[0] for choice in self.CATEGORIAS_CHOICES)

    def delete(self, using=None, keep_parents=False):
        super().delete()