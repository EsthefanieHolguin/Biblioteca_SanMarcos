from django.db import models

# Create your models here.
class Catalogocompleto(models.Model):
    isbn=models.CharField(max_length=50)
    titulo=models.CharField(max_length=50)
    autor=models.CharField(max_length=50)
    categoria=models.CharField(max_length=50)
    ubicacion=models.CharField(max_length=50)

    class Meta:
        db_table='catalogocompleto'