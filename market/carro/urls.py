from django.urls import path

from . import views

app_name = "carro"
# /carro/agregar/14?unidades=5
urlpatterns = [
    path('agregar/<int:id_producto>', views.agregar_producto, name='agregar'),
    path('eliminar/<int:id_producto>/', views.eliminar_producto, name='eliminar'),
    path('restar/<int:id_producto>/', views.restar_producto, name='restar'),
    path('limpiar/', views.limpiar_carro, name='limpiar'),
]
