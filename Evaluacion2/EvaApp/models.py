from django.db import models

# Create your models here.

class videojuego(models.Model):
    nombre = models.CharField(max_length=50)
    publicador = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    tamanio = models.IntegerField()
    costo = models.IntegerField()
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)

class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.IntegerField()
    ciudad = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)

class computadora(models.Model):
    marca = models.CharField(max_length=50)
    disco = models.IntegerField()
    gpu = models.IntegerField()
    cpu = models.IntegerField()
    ram = models.IntegerField()
    usuario = models.ForeignKey(usuario, on_delete=models.CASCADE)
    