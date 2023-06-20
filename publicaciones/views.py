from http.client import HTTPResponse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from django.contrib import messages
from .forms import ComentarioForm, CustomUserCreationForm, PublicacionForm,ProfileForm
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse



# Create your views here.

def inicio(request):
    publicaciones = Publicacion.objects.order_by("-fechaPublicacion")
    return render(request, 'publicaciones/inicio.html', {'publicaciones': publicaciones})

    publicacion = Publicacion.objects.get(idPublicacion=pk)

    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.idPublicacion = publicacion
            comentario.save()
            return redirect('detalle_publicacion', pk=pk)
    else:
        form = ComentarioForm()

    return render(request, "publicaciones/detalle_publicacion.html", {'publicacion': publicacion, 'form': form})


def detalle_publicacion(request, pk):
    publicacion = get_object_or_404(Publicacion, idPublicacion=pk)

    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user in publicacion.likes.all():
                # El usuario ya dio like, lo quitamos
                publicacion.likes.remove(request.user)
            else:
                # El usuario no ha dado like, lo agregamos
                publicacion.likes.add(request.user)
        else:
            # El usuario no está autenticado, redirigir a la página de inicio de sesión
            return redirect('inicioSesion')

    comentarios = Comentario.objects.filter(idPublicacion=publicacion)

    return render(request, "publicaciones/detalle_publicacion.html", {
        'publicacion': publicacion,
        'comentarios': comentarios,
    })


def like_publicacion(request, publicacion_id):
    publicacion = get_object_or_404(Publicacion, idPublicacion=publicacion_id)

    if request.method == 'POST':
        if request.user.is_authenticated:
            if request.user in publicacion.likes.all():
                # El usuario ya dio like, lo quitamos
                publicacion.likes.remove(request.user)
            else:
                # El usuario no ha dado like, lo agregamos
                publicacion.likes.add(request.user)
        else:
            # El usuario no está autenticado, redirigir a la página de inicio de sesión
            return redirect('inicioSesion')

    return redirect('detalle_publicacion', pk=publicacion_id)




def crear_comentario(request, pk):
    publicacion = get_object_or_404(Publicacion, idPublicacion=pk)

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.usuario = request.user
            comentario.idPublicacion = publicacion
            comentario.save()
    return redirect('detalle_publicacion', pk=publicacion.idPublicacion)

def modificar_contraseña(request):
    return render(request, "publicaciones/modificar_contraseña.html")


def editar_perfil(request):
    if request.method =='POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.perfil)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = ProfileForm(instance=request.user.perfil)
    return render(request, "publicaciones/editar_perfil.html", {'form': form})
    

    


def perfil(request):
    return render(request, "publicaciones/perfil.html")



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


def eliminar_publicacion(request, pk):
    if not request.user.is_superuser:
        # Si el usuario no es un superusuario, redirigir a otra página o mostrar un mensaje de error
        return HttpResponse("Acceso denegado")

    publicacion = get_object_or_404(Publicacion, idPublicacion=pk)
    
    if request.method == 'POST':
        publicacion.delete()
        return redirect('inicio')  # Redirige a la página de inicio después de eliminar la publicación
    
    return render(request, 'publicaciones/eliminar_publicacion.html', {'publicacion': publicacion})


#def eliminar_comentario(request, pk):
    # Obtener el comentario que se desea eliminar
    comentario = get_object_or_404(Comentario, id=pk)
    
    # Verificar si el usuario tiene permisos para eliminar el comentario
    if request.user.is_superuser:
        # Eliminar el comentario
        comentario.delete()
    
    # Redireccionar a la página de detalle de la publicación o a otra página según tus necesidades
    return redirect('detalle-publicacion', publicacion_id=comentario.publicacion.idPublicacion)


#def modificar_contraseña(request):
    if request.method == 'POST':
        contraseña_actual = request.POST.get('current-password')
        nueva_contraseña = request.POST.get('new-password')
        confirmar_contraseña = request.POST.get('confirm-password')

        # Verificar si la contraseña actual coincide con la del usuario autenticado
        if request.user.check_password(contraseña_actual):
            # Verificar si la nueva contraseña y la confirmación coinciden
            if nueva_contraseña == confirmar_contraseña:
                # Cambiar la contraseña del usuario
                request.user.set_password(nueva_contraseña)
                request.user.save()

                messages.success(request, 'Contraseña modificada exitosamente.')
                return redirect('modificar_contraseña')
            else:
                messages.error(request, 'La nueva contraseña y la confirmación no coinciden.')
        else:
            messages.error(request, 'La contraseña actual es incorrecta.')

    return render(request, 'publicaciones/modificar_contraseña.html')



    


