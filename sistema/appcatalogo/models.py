from django.db import models

# Create your models here.
class Catalogocompleto(models.Model):
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)

    class Meta:
        db_table='catalogocompleto'