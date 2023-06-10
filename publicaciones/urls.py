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
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path("inicio/", views.inicio, name="inicio"),
    path("sesion/",LoginView.as_view(template_name="publicaciones/iniciar_sesion.html"),name="inicioSesion",),
    path("modificarContraseña/", views.modificarContraseña, name="modificarContraseña"),
    path("perfil/", views.perfil, name="perfil"),
    path("olvidarContraseña/", views.olvidarContraseña, name="olvidarContraseña"),
    path("registro/", views.registro, name="registro"),
    path("registro_exitoso/", views.registro_exitoso, name="registro_exitoso"),
    path(
        "restablecer_contraseña/",
        auth_views.PasswordResetView.as_view(
            template_name="publicaciones/restablecer_contraseña.html",
        ),
        name="restablecer_contraseña",
    ),
    path(
        "restablecer_enviado/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="publicaciones/restablecer_enviado.html"
        ),
        name="password_reset_done",
    ),
    path(
        "restablecer_confirmar/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="publicaciones/restablecer_confirmar.html"
        ),
        name="password_reset_confirm",
    ),
    path(
        "restablecer_completo/",
        auth_views.PasswordResetCompleteView.as_view(),
        name="password_reset_complete",
    ),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
    path('perfil/', views.ver_perfil, name='perfil'),
    path('subir_foto/', views.subir_foto, name='subir_foto'),
    path('publicacion/<int:pk>/', views.detalle_publicacion, name='detalle_publicacion'),


]

