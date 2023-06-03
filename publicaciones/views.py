from datetime import datetime
from django.shortcuts import render,get_object_or_404
from .models import Imagen

# Create your views here.
def detalle_imagen(request,imagen_id):
    # obtener la imagen correspondiente al id proporcionado
    #imagen = get_object_or_404(Imagen,idImagen=imagen_id)
    
    #contexto = {
        #'imagen':imagen,
        #'descripcion':imagen.descripcion,   
        #'autor':imagen.autor,
        #'fecha': imagen.fecha
    #}
    contexto ={
        'imagen':'linkde la imagen',
        'descripcion':'descripcion de la imagen',
        'autor':'joaqin',
        'fecha': datetime.today(),
    }
    return render(request, 'publicaciones/detalle_imagen.html', contexto)


def inicio(request):
    return render(request,'publicaciones/inicio.html')

def sesion(request):
    return render(request,'publicaciones/iniciar_sesion.html')


def registro(request):
    return render(request,'publicaciones/registrarse.html')

def  detalles(request):
    return render(request,'publicaciones/detalle_foto.hmtl')

def  modificarContraseña(request):
    return render(request,'publicaciones/modificar_contraseña.html')

def  perfil(request):
    return render(request,'publicaciones/perfil.html')

def  olvidarContraseña(request):
    return render(request,'publicaciones/olvidar_contraseña.html')

def  subirFoto(request):
    return render(request,'publicaciones/subir_foto.html')








