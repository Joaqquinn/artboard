from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User



# Create your models here.


class Rol(models.Model):
    idRol = models.AutoField(primary_key=True, verbose_name="Codigo Rol")
    nombre = models.CharField(max_length=50)


class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    foto_perfil = models.ImageField(upload_to="perfil", null=True, blank=True)
    def __str__(self):
        return f"{self.usuario.username}"


class Publicacion(models.Model):
    idPublicacion = models.AutoField(primary_key=True, verbose_name="Codigo Publicacion")
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    fechaPublicacion = models.DateField(auto_now_add=True)
    estatus = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="Usuario")
    Imagen = models.ImageField(upload_to="publicaciones", null=True, blank=True)
    
    def __str__(self):
        return f"{self.titulo}"

class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True, verbose_name="Codigo Imagen")
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, verbose_name="Id publicacion")
    nombre = models.TextField(max_length=20)
    archivo = models.CharField(max_length=20)


class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True, verbose_name="Codigo Comentario")
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, verbose_name="Id publicacion")
    comentario = models.TextField(max_length=500)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="Usuario")




#class Like(models.Model):
  #  idLike = models.AutoField(primary_key=True, verbose_name="Codigo Like")
   # idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, verbose_name="Id publicacion")
    #usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE, verbose_name="Usuario")