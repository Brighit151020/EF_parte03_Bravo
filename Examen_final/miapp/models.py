from django.db import models

class Pais(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    poblacion = models.IntegerField()
    estado = models.BooleanField()

