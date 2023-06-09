from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .forms import PublicacionForm


# Create your views here.
def detalle_imagen(request, imagen_id):
    # obtener la imagen correspondiente al id proporcionado
    # imagen = get_object_or_404(Imagen,idImagen=imagen_id)

    # contexto = {
    #'imagen':imagen,
    #'descripcion':imagen.descripcion,
    #'autor':imagen.autor,
    #'fecha': imagen.fecha
    # }
    contexto = {
        "imagen": "linkde la imagen",
        "descripcion": "descripcion de la imagen",
        "autor": "joaqin",
        "fecha": datetime.today(),
    }
    return render(request, "publicaciones/detalle_imagen.html", contexto)


def inicio(request):
    return render(request, "publicaciones/inicio.html")


def detalles(request):
    return render(request, "publicaciones/detalle_foto.hmtl")


def modificarContraseña(request):
    return render(request, "publicaciones/modificar_contraseña.html")


def perfil(request):
    return render(request, "publicaciones/perfil.html")


def olvidarContraseña(request):
    return render(request, "publicaciones/olvidar_contraseña.html")


def vista_inicio(request):
    Publicaciones = Publicacion.objects.all().order_by("fechaPublicacion")
    contexto = {
        "publicaciones": Publicaciones,
    }
    return render(request, "publicaciones/inicio.html", contexto)


def registro(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")
            return redirect("inicio")
    else:
        form = CustomUserCreationForm()
    return render(request, "publicaciones/registro.html", {"form": form})


def registro_exitoso(request):
    return render(request, "publicaciones/registro_exitoso.html")


def subir_foto(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("inicio")
    else:
        form = PublicacionForm()

    contexto = {"form": form}
    return render(request, "subir_foto.html", contexto)


def cerrar_sesion(request):
    logout(request)
    return redirect("inicio")


@login_required
def ver_perfil(request):
    usuario = request.user
    contexto = {
        "usuario": usuario,
    }
    return (render(request, "publicaciones/perfil.html", contexto),)
