from datetime import datetime
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import RegistroForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView
from django.http import HttpResponse


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


def sesion(request):
    if request.method == "POST":
        # Obtener los datos del formulario
        email = request.POST.get("email")
        password = request.POST.get("password")

        # Autenticar al usuario utilizando el correo electrónico
        user = authenticate(request, email=email, password=password)

        if user is not None:
            # Iniciar sesión del usuario
            login(request, user)
            return redirect("inicio")  # Redirigir a la página principal después del inicio de sesión exitoso
        else:
            # El usuario no es válido
            mensaje_error = "Credenciales inválidas. Inténtalo de nuevo."
            return render(request, "publicaciones/iniciar_sesion.html", {"error_message": mensaje_error})

    # Si el método no es POST, renderizar el formulario de inicio de sesión
    return render(request, "publicaciones/iniciar_sesion.html")




def detalles(request):
    return render(request, "publicaciones/detalle_foto.hmtl")


def modificarContraseña(request):
    return render(request, "publicaciones/modificar_contraseña.html")


def perfil(request):
    return render(request, "publicaciones/perfil.html")


def olvidarContraseña(request):
    return render(request, "publicaciones/olvidar_contraseña.html")


def subirFoto(request):
    return render(request, "publicaciones/subir_foto.html")


def registro(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("registro_exitoso")
    else:
        form = RegistroForm()
    return render(request, "publicaciones/registrarse.html", {"form": form})


def registro_exitoso(request):
    return render(request, "publicaciones/registro_exitoso.html")
