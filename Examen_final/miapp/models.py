from django.db import models

class Pais(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=40)
    poblacion = models.IntegerField()
    estado = models.BooleanField()

class Editorial(models.Model):
    nombre = models.CharField(max_length=40)
    url = models.URLField()
    imagen = models.ImageField(upload_to='editoriales/', null=True, blank=True)
    estado = models.BooleanField()

    def __str__(self):
        return self.nombre
