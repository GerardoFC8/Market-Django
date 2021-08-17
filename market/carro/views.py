from django.shortcuts import render
from .carro import Carro
from mainCRUD.models import Producto
from django.shortcuts import redirect


# Create your views here.
def index_carrito(request):
    return render(request, "carro/widget.html")


def agregar_producto(request, id_producto):
    cantidad = request.GET.get('unidades')
    carro = Carro(request)
    producto = Producto.objects.get(id=id_producto)
    carro.agregar(producto=producto, cantidad=cantidad)

    return redirect("/carro/")


def eliminar_producto(request, id_producto):
    carro = Carro(request)
    producto = Producto.objects.get(id=id_producto)
    carro.eliminar(producto=producto)

    return redirect("/carro/")


def restar_producto(request, id_producto):
    carro = Carro(request)
    producto = Producto.objects.get(id=id_producto)
    carro.restar_productos(producto=producto)

    return redirect("/carro/")


def limpiar_carro(request, id_producto):
    carro = Carro(request)
    carro.limpiar_carro()

    return redirect("/carro/")
