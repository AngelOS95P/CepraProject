from django.db import models

# Create your models here.
class Publicacion(models.Model):
    Titulo=models.CharField(max_length=160, verbose_name="Titulo")
    Resumen=models.TextField(verbose_name="Resumen")
    Enlace=models.CharField(max_length=500,verbose_name="Enlace")

    class Meta:
        verbose_name="publicación"
        verbose_name_plural="publicaciones"
        ordering = ['-Titulo']
    
    def _str_(self):
        return self.Titulo


class Contenido(models.Model):
    Titulo=models.CharField(max_length=160, verbose_name="Titulo")
    Descripcion=models.TextField(verbose_name="Descripción")
    Enlace=models.CharField(max_length=500,verbose_name="Enlace")

    class Meta:
        verbose_name="contenido"
        verbose_name_plural="contenidos"
        ordering = ['-Titulo']
    
    def _str_(self):
        return self.Titulo