from django.contrib import admin
from publicaciones.models import Rol,Publicacion,Imagen,Comentario,Perfil

# Register your models here.
admin.site.register(Rol)
admin.site.register(Publicacion)
admin.site.register(Imagen)
admin.site.register(Comentario)
admin.site.register(Perfil)