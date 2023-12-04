from typing import Any
from django.db import models
from appejemplares.models import Libro
from appusuarios.models import Usuario

class Prestamo(models.Model):

    id = models.AutoField(primary_key=True)
    rut_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null='False')
    fecha_prestamo = models.DateTimeField(auto_now=True, null='False')
    libros = models.ForeignKey(Libro,on_delete=models.CASCADE, null='False')

    def __str__(self):
        fila = "ID Préstamo: "+ self.id + " - " + "Usuario: " + self.usuario + " - " + "Fecha Préstamo: " + " " + self.fecha_prestamo + " - " + "Libro : " + self.libro
        return fila

    class Meta:
        verbose_name = "Datos_Prestamos"
