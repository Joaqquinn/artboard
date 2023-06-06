from django.contrib import admin
from publicaciones.models import Rol,Publicacion,Imagen,Comentario

# Register your models here.
admin.site.register(Rol)
admin.site.register(Publicacion)
admin.site.register(Imagen)
admin.site.register(Comentario)