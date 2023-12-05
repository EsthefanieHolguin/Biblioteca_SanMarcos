from django.db import models
from typing import Any
from appejemplares.models import Libro
from appusuarios.models import Usuario

# Create your models here.
class Reserva(models.Model):

    id_reserva = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField(auto_now_add=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE,null=False,blank=False)
    isbn = Libro.isbn
    titulo = Libro.titulo
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=True,blank=False)
    rut_usuario = Usuario.rut
    usuario = Usuario.nombre_usuario
    curso = Usuario.curso

    def __str__(self):
        fila = "ID Reserva: " + self.id_reserva + " - " + "Libro: " + " " + self.titulo + " - " + "Usuario: " + " " + self.usuario
        return fila

    class Meta:
        verbose_name = "Datos_Reservas"