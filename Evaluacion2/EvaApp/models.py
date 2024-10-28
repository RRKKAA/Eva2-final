from django.db import models

# Create your models here.

class videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    publicador = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tamanio = models.IntegerField()
    costo = models.IntegerField()