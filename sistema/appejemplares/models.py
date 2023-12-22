from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import pre_save
from django.dispatch import receiver


class Libro(models.Model):
    """
    Modelo que representa un libro en la biblioteca.

    Attributes:
    - isbn (str): Número de identificación único del libro.
    - titulo (str): Título del libro.
    - autor (str): Autor del libro.
    - categoria (str): Categoría del libro (e.g., Novelas, Suspenso).
    - ubicacion (str): Ubicación física del libro en la biblioteca.
    - ejemplares_totales (int): Número total de ejemplares del libro.
    - ejemplares_disponibles (int): Número de ejemplares disponibles para préstamo.
    - ejemplares_prestados (int): Número de ejemplares actualmente prestados.
    - ejemplares_reservados (int): Número de ejemplares reservados.
    - descripcion (str): Descripción del libro (opcional).

    Methods:
    - __str__: Representación en cadena del libro (devuelve el ISBN como identificador).
    - is_upperclass: Verifica si la categoría del libro está en mayúsculas.
    - delete: Sobrescribe el método de eliminación para realizar acciones personalizadas.

    """

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
    ejemplares_disponibles = models.IntegerField(default=ejemplares_totales)
    ejemplares_prestados = models.IntegerField(default=0)
    ejemplares_reservados = models.IntegerField(default=0)
    descripcion = models.TextField(verbose_name='Descripción', null=True, blank=True)

    def __str__(self):
        """Representación en cadena del libro."""

        return self.isbn

    def is_upperclass(self):
        """Verifica si la categoría del libro está en mayúsculas."""

        return self.categoria in (choice[0] for choice in self.CATEGORIAS_CHOICES)

    def delete(self, using=None, keep_parents=False):
        """
        Sobrescribe el método de eliminación para realizar acciones personalizadas.

        En este caso, se podría agregar la eliminación de la imagen asociada al libro si se utiliza algún campo de imagen.

        Args:
        - using (str): Nombre de la base de datos.
        - keep_parents (bool): Indica si se deben mantener las relaciones de clave externa.

        """

        #self.imagen.storage.delete(self.imagen.name)
        super().delete()

from appprestamos.models import Prestamo 
@receiver(pre_save, sender=Prestamo)
def actualizar_ejemplares_libro(sender, instance, **kwargs):
    """
    Actualiza el número de ejemplares disponibles y prestados cuando se realiza un préstamo.

    Este método se conecta a la señal pre_save de Prestamo para actualizar automáticamente
    el número de ejemplares disponibles y prestados en el libro asociado cuando se realiza
    un préstamo o se finaliza un préstamo.

    Args:
    - sender: Clase que envía la señal (Prestamo en este caso).
    - instance: Instancia de Prestamo que activa la señal.
    - **kwargs: Argumentos adicionales.

    """
    
    # Obtener el libro asociado al préstamo
    libro = instance.isbn

    # Verificar si es un préstamo nuevo
    if instance._state.adding:
        # Restar 1 al número de ejemplares disponibles
        libro.ejemplares_disponibles -= 1
        # Sumar 1 al número de ejemplares prestados
        libro.ejemplares_prestados += 1
    else:
        # Verificar si se está finalizando un préstamo
        if instance.estado_prestamo == 'finalizado':
            # Sumar 1 al número de ejemplares disponibles
            libro.ejemplares_disponibles += 1
            # Restar 1 al número de ejemplares prestados
            libro.ejemplares_prestados -= 1

    # Guardar los cambios en el libro
    libro.save()
