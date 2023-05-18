from django.db import models

# Create your models here.
class Pregunta(models.Model):
    idPregunta = models.AutoField(primary_key=True,verbose_name='Codigo Pregunta')
    descripcion = models.TextField()


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
    pregunta = models.ForeignKey(Pregunta,on_delete=models.CASCADE,verbose_name='Pregunta')


class Comentario (models.Model):
    idComentario = models.AutoField(primary_key=True,verbose_name='Codigo Comentario')
    
    
