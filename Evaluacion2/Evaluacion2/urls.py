"""Evaluacion2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from EvaApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),

    path('usuarios/',views.listadoUsuarios),
    path('agregarUsuario/',views.agregarUsuario),
    path('actualizarUsuario/',views.actualizarUsuario),
    path('eliminarUsuario/',views.eliminarUsuario),
    path('usuario/',views.detalleUsuario),

    path('computadoras/',views.listadoComputadoras),
    path('agregarComputadora/',views.agregarComputadora),
    path('actualizarComputadora/',views.actualizarComputadora),
    path('eliminarComputadora/',views.eliminarComputadora),

    path('videojuegos/',views.listadoVideojuegos),
    path('agregarVideojuego/',views.agregarJuego),
    path('actualizarJuego/<int:id>',views.actualizarJuego),
    path('eliminarJuego/<int:id>',views.eliminarJuego)
]
