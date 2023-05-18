from django.db import models

# Create your models here.


class Rol(models.Model):
    idRol = models.AutoField(primary_key=True,verbose_name='Codigo Rol')
    nombre = models.CharField(max_length=50)


class Usuario(models.Model):
    idUsuario = models.AutoField(primary_key=True,verbose_name='Codigo Usuario')
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE,verbose_name='Rol')
    
    
class Publicacion(models.Model):
    idPublicacion = models.AutoField(primary_key=True,verbose_name='Codigo Publicacion')
    titulo = models.CharField(max_length=50)
    descripcion = models.TextField(max_length=500)
    fechaPublicacion = models.DateField(_(""), auto_now=False, auto_now_add=False)
    estatus = models.CharField(max_length=50)
    foto = models.ImageField()
    idusuario =models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Id usuario')
    
    
class Imagen(models.Model):
    idImagen = models.AutoField(primary_key=True,verbose_name='Codigo Imagen')
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, verbose_name='Id publicacion')
    nombre = models.TextField(max_length=20)
    archivo = models.CharField(max_length=20)
    
    
class Comentario(models.Model):
    idComentario = models.AutoField(primary_key=True,verbose_name='Codigo Comentario')
    idPublicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, verbose_name='Id publicacion')
    idUsuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name='Id usuario')
    comentario = models.TextField(max_length=500)
    fechaComentario = models.DateField(_(""), auto_now=False, auto_now_add=False)
    estatus = models.CharField(max_length=50)
    



    
    
    
