from datetime import datetime
from django.shortcuts import render, redirect
from .models import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User




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
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect("inicio")
    else:
        form = UserCreationForm()
    return render(request, "publicaciones/registro.html", {"form": form})

def registro_exitoso(request):
    return render(request, "publicaciones/registro_exitoso.html")
    


    
