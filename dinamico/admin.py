from django.contrib import admin
from .models import Publicacion, Contenido

class PubliAdmin(admin.ModelAdmin):
    pass
    list_display=('Titulo', 'Resumen' ,'Enlace')

admin.site.register(Publicacion, PubliAdmin)


class DinamicoAdmin(admin.ModelAdmin):
    pass
    list_display=('Titulo','Descripcion', 'Enlace')

admin.site.register(Contenido, DinamicoAdmin)


