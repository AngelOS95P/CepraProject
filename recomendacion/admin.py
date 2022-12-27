from django.contrib import admin
from .models import RecoPeluche, RecoJuegosS, RecoTablero, RecoVarita
# Register your models here.

class RecoPelucheAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante','FrecuenciaS','Sombrero','Broches','Cierre','Velcro','Cordon')

admin.site.register(RecoPeluche, RecoPelucheAdmin)

class RecoJuegosSAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante','FrecuenciaS','Topos','Laberinto','RompeC','Colorear','Letras')

admin.site.register(RecoJuegosS, RecoJuegosSAdmin)

class RecoTableroAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante','FrecuenciaS','Trazos','Pinzas','Precision')

admin.site.register(RecoTablero, RecoTableroAdmin)

class RecoVaritaAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante','Horizontal','Vertical','Oblicuas')

admin.site.register(RecoVarita, RecoVaritaAdmin)
