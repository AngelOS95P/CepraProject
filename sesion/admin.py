from django.contrib import admin
from .models import Sesion, Peluche, Tablero, Varita, JuegoColorear, JuegoLaberinto, JuegoLetras, JuegoRompeC, JuegoTopos

# Register your models here.

class SesionAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Estudiante','fecha','Herramienta')

admin.site.register(Sesion, SesionAdmin)

class PelucheAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Tipo','Tiempo','Ayuda','Sesion')

admin.site.register(Peluche, PelucheAdmin)

class TableroAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Actividad','Tiempo','Errores','Sesion')

admin.site.register(Tablero, TableroAdmin)


class VaritaAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Nivel','Tiempo','Intentos','Sesion')

admin.site.register(Varita, VaritaAdmin)

class ToposAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Nivel','Cant_Agujeros','Tiem_Juego','Tiem_Arriba','Tiem_Salida','Porce_Gana','Num_Aciertos','Num_Perdidos','Porce_Logrado','Sesion')

admin.site.register(JuegoTopos, ToposAdmin)

class LaberintoAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Nivel','Tiem_Necesario','Tiem_Logrado','Intentos','Sesion')

admin.site.register(JuegoLaberinto, LaberintoAdmin)

class RompeCAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Nivel','Tiem_Necesario','Tiem_Logrado','Precision','Num_Piezas','Sesion')

admin.site.register(JuegoRompeC, RompeCAdmin)

class LetrasAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Nivel','Tiem_Necesario','Tiem_Logrado','Intentos','Sesion')

admin.site.register(JuegoLetras, LetrasAdmin)

class ColorearAdmin(admin.ModelAdmin):
    pass
    list_display=('id','Nivel','Tiem_Necesario','Colores','Sesion')

admin.site.register(JuegoColorear, ColorearAdmin)