from django.db import models
from typing import Any


class Usuario(models.Model):
    """
    Modelo que representa a un usuario en el sistema.

    Attributes:
    - rut_usuario (str): Rut del usuario, clave primaria.
    - nombre_usuario (str): Nombre del usuario.
    - email (EmailField): Dirección de correo electrónico del usuario.
    - curso (str): Curso al que pertenece el usuario.

    Methods:
    - __str__(): Devuelve una representación en cadena del usuario.

    Meta:
    - verbose_name (str): Nombre amigable para el modelo en singular.

    """

    # Definición de campos del modelo
    rut_usuario = models.CharField(primary_key=True,max_length=9,)
    nombre_usuario = models.CharField(max_length=100, verbose_name='Nombre', null=False, blank=False)
    email = models.EmailField(max_length=120, verbose_name='Email', null=False, blank=False)
    curso = models.CharField(max_length=20, verbose_name='Curso', null=False, blank=False)

    def __str__(self):
        """
        Método que devuelve una representación en cadena del usuario.

        Returns:
        - str: Representación en cadena del usuario.

        """

        fila = self.rut_usuario 
        return fila

    class Meta:
        """
        Clase Meta para configuración adicional del modelo.

        Attributes:
        - verbose_name (str): Nombre amigable para el modelo en singular.

        """
        
        verbose_name = "Datos_Usuarios"