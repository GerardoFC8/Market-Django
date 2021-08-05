from django.shortcuts import render, redirect
from .models import Usuario, Producto
from .forms import UsuarioForm, ProductoForm
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def index(request):
    prod = Producto.objects.all()
    return render(request, "mainCRUD/index.html", {"list_producto": prod})

def usuario(request):
    us = Usuario.objects.filter(usuario_estado = True)
    context = {"list_usuario": us}
    return render(request, "mainCRUD/usuario.html", context)

def producto(request):
    prod = Producto.objects.all()
    context = {"list_producto": prod}
    return render(request, "mainCRUD/producto.html", context)

def agregar_usu(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = UsuarioForm()
        
    context = {'form' : form}
    return render(request, 'mainCRUD/agregar_usu.html', context)

def agregar_prod(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()
        
    context = {'form' : form}
    return render(request, 'mainCRUD/agregar_prod.html', context)

def editar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = UsuarioForm(instance = usuario)

    context = {'form' : form}
    return render(request, 'mainCRUD/editar_usu.html', context)

def eliminar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id = id_usuario)
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance = usuario)
        if form.is_valid():
            form.save()
            return redirect('usuario')
    else:
        form = UsuarioForm(instance = usuario)

    context = {'form' : form}
    return render(request, 'mainCRUD/agregar_usu.html', context)


def editar_producto(request, id_producto):
    producto = Producto.objects.get(id = id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance = producto)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm(instance = producto)

    context = {'form' : form}
    return render(request, 'mainCRUD/agregar_prod.html', context)

def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id = id_producto)
    producto.delete()
    return redirect('producto')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            messages.success(request, f'El usuario {username} fue creado correctamente.')
            form.save()
    else:
        form = UserRegisterForm()

    context = {'form' : form}
    return render(request, 'mainCRUD/admin/register.html', context)

