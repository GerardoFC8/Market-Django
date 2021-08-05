from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.index, name="home"),
    path("usuario/", views.usuario, name="usuario"),
    path("producto/", views.producto, name="producto"),
    path("agregar_usuario/", views.agregar_usu, name="agregar"),
    path("agregar_producto/", views.agregar_prod, name="agregar"),
    path("editar_usuario/<int:id_usuario>/", views.editar_usuario, name="editar_usuario"),
    path("eliminar_usuario/<int:id_usuario>/", views.eliminar_usuario, name="eliminar_usuario"),
    path("editar_producto/<int:id_producto>/", views.editar_producto, name="editar_producto"),
    path("eliminar_producto/<int:id_producto>/", views.eliminar_producto, name="eliminar_producto"),
    path("register/", views.register, name='register'),
    path("login/", LoginView.as_view(template_name='mainCRUD/admin/login.html'), name='login'),
    path("logout/", LoginView.as_view(template_name='mainCRUD/admin/logout.html'), name='logout'),
]
