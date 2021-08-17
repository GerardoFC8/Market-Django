from django.db import models


# Create your models here.

class Producto(models.Model):
    prod_nombre = models.CharField(max_length=500)
    prod_categoria = models.CharField(max_length=250)
    prod_precio = models.FloatField(default=0.0)
    prod_descripcion = models.TextField(max_length=500)
    prod_imagen = models.ImageField()

    def __str__(self):
        return self.prod_nombre


class Correo(models.Model):
    nombre = models.CharField(max_length = 100)
    correo = models.EmailField()
    asunto = models.CharField(max_length = 200)
    mensaje = models.TextField()

    def __str__(self):
        return self.nombre