from typing import Any
from django.db import models
from django.utils.translation import gettext_lazy as _
from appejemplares.models import Libro
from appusuarios.models import Usuario

class Prestamo(models.Model):
    
    class EstadoPrestamo(models.TextChoices):
        VIGENTE = '0', _('Vigente')
        FINALIZADO = '1', _('Finalizado')
        ATRASADO = '2', _('Devolución Atrasada')

    id_prestamo = models.AutoField(primary_key=True)
    isbn = models.ForeignKey(Libro, on_delete=models.CASCADE,null=False,blank=False)
    rut_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE,null=False,blank=False)
    fecha_prestamo = models.DateTimeField(auto_now=True)
    fecha_devolucion_calculada = models.DateTimeField(null=True,blank=True)
    fecha_devolucion_real = models.DateTimeField(null=True,blank=True)
    flg_estado_prestamo = models.CharField(
        max_length=10,
        choices=EstadoPrestamo.choices,
        default=EstadoPrestamo.VIGENTE,
    ) #0=Préstamo Vigente, 1=Préstamo Finalizado 2=Devolución Atrasada 

    def __str__(self):
        fila = "ID Préstamo: " + self.id_prestamo + "Isbn: " + self.isbn + "Rut Usuario: " + self.rut_usuario + "Fecha Préstamo: " + self.fecha_prestamo + "Fecha Devolución: " + self.fecha_prestamo + "Fecha Préstamo: " + self.fecha_prestamo 

        return fila

    def is_upperclass(self):
        return self.estado_prestamo in {
            self.EstadoPrestamo.VIGENTE,
            self.EstadoPrestamo.FINALIZADO,
            self.EstadoPrestamo.ATRASADO,
        }
    class Meta:
        verbose_name = "Datos_Prestamos"
