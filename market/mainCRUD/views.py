from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Producto

# Create your views here.

def index(response):
    return render(response, "mainCRUD/index.html", {})

def usuario(response):
    us = Usuario.objects.filter(usuario_estado=True)
    return render(response, "mainCRUD/usuario.html", {"list_usuario": us})

def producto(response):
    prod = Producto.objects.all()
    return render(response, "mainCRUD/producto.html", {"list_producto": prod})
