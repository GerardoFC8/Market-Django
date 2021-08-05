from django.db import models

# Create your models here.
class Usuario(models.Model):
    usuario_nombre = models.CharField(max_length=250)
    usuario_estado = models.BooleanField(default=True)
    usuario_correo = models.CharField(max_length=250)
    usuario_clave = models.CharField(max_length=250)
    usuario_fecha = models.DateField()

    def __str__(self):
        return self.usuario_nombre
# Usuario(usuario_nombre="Jamir", usuario_estado="1", usuario_correo="correo@gmail.com", usuario_clave="123", usuario_fecha="2021-08-01")

class Producto(models.Model):
    prod_nombre = models.CharField(max_length=500)
    prod_categoria = models.CharField(max_length=250)
    prod_precio = models.FloatField(default=0.0)

    def __str__(self):
        return self.prod_nombre
    # Producto(prod_nombre="Platano", prod_categoria="viveres", prod_precio="3.60")

    # SHELL a 
# from mainCRUD.models import Usuario, Producto
