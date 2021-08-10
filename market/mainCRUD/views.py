from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


# Create your views here.

def index(request):
    embutidos = Producto.objects.filter(prod_categoria = 'EMBUTIDOS Y LACTEOS')
    snacks = Producto.objects.filter(prod_categoria = 'SNACKS Y PIQUEOS')
    confiteria = Producto.objects.filter(prod_categoria = 'CONFITERIA')
    congelados = Producto.objects.filter(prod_categoria = 'CONGELADOS')
    alcohol = Producto.objects.filter(prod_categoria = 'BEBIDAS ALCOHOLICAS')
    productos = {"embutidos": embutidos, 
                "snacks": snacks,
                "confiteria": confiteria,
                "congelados": congelados,
                "alcohol": alcohol}
    return render(request, "mainCRUD/index.html", productos)

def producto(request):
    prod = Producto.objects.all()
    context = {"list_producto": prod}
    return render(request, "mainCRUD/producto.html", context)

@permission_required('mainCRUD.add_producto')
def agregar_prod(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm()

    context = {'form': form}
    return render(request, 'mainCRUD/agregar_prod.html', context)


@permission_required('mainCRUD.change_producto')
def editar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('producto')
    else:
        form = ProductoForm(instance=producto)

    context = {'form': form}
    return render(request, 'mainCRUD/agregar_prod.html', context)


@permission_required('mainCRUD.delete_producto')
def eliminar_producto(request, id_producto):
    producto = Producto.objects.get(id=id_producto)
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

    context = {'form': form}
    return render(request, 'mainCRUD/admin/register.html', context)
