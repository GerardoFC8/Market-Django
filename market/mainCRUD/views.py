from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario, Producto

# Create your views here.

def index(response):
    return HttpResponse("<style>body{background: #262626; color: #fff; font-size: 4rem;}</style><h1>INDEX</h1>")

def home(response):
    us = Usuario.objects.all()
    pr = Producto.objects.all()
    return HttpResponse("<style>body{background: #262626; color: #fff; font-size: 2rem;}</style>"
                        "<h1>USUARIOS</h1>"
                        "<h3>%s</h3>" 
                        "<h1>PRODUCTOS</h1>"
                        "<h3>%s</h3>" %(us[0], pr[0]))
