# Generated by Django 4.2.7 on 2023-11-30 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('autor', models.CharField(max_length=100, verbose_name='Autor')),
                ('categoria', models.CharField(choices=[('novelas', 'Novelas'), ('suspenso', 'Suspenso'), ('historia', 'Historia')], max_length=50, verbose_name='Categoría')),
                ('ubicacion', models.CharField(blank=True, max_length=20, null=True, verbose_name='Ubicación')),
                ('ejemplares_disponibles', models.IntegerField(default=0)),
                ('imagen', models.ImageField(null=True, upload_to='imagenes/', verbose_name='Imagen')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Descripción')),
            ],
        ),
    ]