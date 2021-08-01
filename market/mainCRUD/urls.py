from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("usu/", views.home, name="usuarios"),
]
