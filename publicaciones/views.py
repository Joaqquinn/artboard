from django.shortcuts import render

# Create your views here.
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








