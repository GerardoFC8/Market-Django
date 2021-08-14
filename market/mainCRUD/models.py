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
    # Producto(prod_nombre="Platano", prod_categoria="viveres", prod_precio="3.60")

    # SHELL a 
# from mainCRUD.models import Usuario, Producto
