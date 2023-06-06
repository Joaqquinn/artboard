"""artboard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path("sesion/", views.sesion, name="inicioSesion"),
    path("detalles/", views.detalles, name="detalleFoto"),
    path("modificarContraseña/", views.modificarContraseña, name="modificarContraseña"),
    path("perfil/", views.perfil, name="perfil"),
    path("olvidarContraseña/", views.olvidarContraseña, name="olvidarContraseña"),
    path("subirFoto/", views.subirFoto, name="subirFoto"),
    path('imagen/<int:imagen_id>/', views.detalle_imagen, name='detalle_imagen'),
    path("registro/", views.registro, name='registro'), 
    path("registro_exitoso/", views.registro_exitoso, name="registro_exitoso"),
        
    
]
