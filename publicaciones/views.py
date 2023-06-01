from django.shortcuts import render

# Create your views here.
def seleccionar_foto(request, caso):
    fotos = {
        'caso1': 'ruta_de_la_foto1.jpg',
        'caso2': 'ruta_de_la_foto2.jpg',
        'caso3': 'ruta_de_la_foto3.jpg',
        # Agrega más casos si es necesario
    }
    foto = fotos.get(caso)
    return render(request, 'foto.html', {'foto': foto})


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








