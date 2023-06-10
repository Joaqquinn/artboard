from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import CustomUserCreationForm, PublicacionForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required



# Create your views here.

def inicio(request):
    publicaciones = Publicacion.objects.order_by("-fechaPublicacion")
    return render(request, 'publicaciones/inicio.html', {'publicaciones': publicaciones})

def detalle_publicacion(request, pk):
    publicacion= Publicacion.objects.get(idPublicacion=pk)
    return render(request, "publicaciones/detalle_publicacion.html", {'publicacion': publicacion})


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

@login_required
def subir_foto(request):
    if request.method == "POST":
        form = PublicacionForm(request.POST, request.FILES)
        if form.is_valid():
            publicacion = form.save(commit=False)
            publicacion.usuario = request.user
            publicacion.save()
            return redirect("inicio")
    else:
        form = PublicacionForm(initial={'usuario': request.user})

    contexto = {"form": form}
    return render(request, "publicaciones/subir_foto.html", contexto)


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
