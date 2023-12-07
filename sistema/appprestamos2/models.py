from typing import Any
from django.db import models
from appejemplares.models import Libro
from appusuarios.models import Usuario

class Prestamo(models.Model):

    id_prestamo = models.AutoField(primary_key=True)
    fecha_prestamo = models.DateTimeField(auto_now=True)
    id_libro = models.ForeignKey(Libro, on_delete=models.CASCADE,null=False,blank=False)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=False,blank=False)


    #rut_usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null='False')

    def __str__(self):
        fila = "ID Préstamo: "+ self.id_prestamo  
        return fila

    class Meta:
        verbose_name = "Datos_Prestamos"
