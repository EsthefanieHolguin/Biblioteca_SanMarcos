from django.db import models
from appejemplares.models import Libro
from appusuarios.models import Usuario

class Prestamo(models.Model):

    id_Prestamo = models.AutoField(primary_key=True)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE, null=True)
    fecha_prestamo = models.DateTimeField(auto_now=True, null=True)
    libro = models.ForeignKey(Libro,on_delete=models.CASCADE, null=True)

    def __str__(self):
        fila = "ID Préstamo: "+ self.id_Prestamo + " - " + "Usuario: " + self.usuario + " - " + "Fecha Préstamo: " + " " + self.fecha_prestamo + " - " + "Libro : " + self.libro
        return fila

    class Meta:
        verbose_name = "Datos_Prestamos"
