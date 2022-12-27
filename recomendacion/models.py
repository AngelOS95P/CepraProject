from django.db import models
from estudiante.models import Estudiante 

# Create your models here.
class RecoPeluche(models.Model):
    id           = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Sombrero     = models.PositiveIntegerField(verbose_name="Sombrero")
    Broches      = models.PositiveIntegerField(verbose_name="Broches")
    Cierre       = models.PositiveIntegerField(verbose_name="Cierre")
    Velcro       = models.PositiveIntegerField(verbose_name="Velcro")
    Cordon       = models.PositiveIntegerField(verbose_name="Cordon")
    Semanas       = models.PositiveIntegerField(default=3, verbose_name="Numero semanas")

    class Meta:
        verbose_name = "Recomendacion Peluche"
        verbose_name_plural = "Recomendaciones Peluche"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre

class RecoJuegosS(models.Model):
    id          = models.AutoField(primary_key=True)
    Estudiante  = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    FrecuenciaS = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Topos       = models.PositiveIntegerField(verbose_name="Topos")
    Laberinto   = models.PositiveIntegerField(verbose_name="Laberinto")
    RompeC      = models.PositiveIntegerField(verbose_name="RompeC")
    Colorear    = models.PositiveIntegerField(verbose_name="Colorear")
    Letras      = models.PositiveIntegerField(verbose_name="Letras")
    Semanas       = models.PositiveIntegerField(default=3, verbose_name="Numero semanas")

    class Meta:
        verbose_name = "Recomendacion Juegos Serios"
        verbose_name_plural = "Recomendaciones Juegos Serios"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre

class RecoTablero(models.Model):
    id          = models.AutoField(primary_key=True)
    Estudiante  = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    FrecuenciaS = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Trazos      = models.PositiveIntegerField(verbose_name="Trazos")
    Pinzas      = models.PositiveIntegerField(verbose_name="Pinzas")
    Precision   = models.PositiveIntegerField(verbose_name="Precision")
    Semanas     = models.PositiveIntegerField(default=3, verbose_name="Numero semanas")

    class Meta:
        verbose_name = "Recomendacion Tablero"
        verbose_name_plural = "Recomendaciones Tablero"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre

class RecoVarita(models.Model):
    id           = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    FrecuenciaS  = models.PositiveIntegerField(verbose_name="Frecuencia Semanal")
    Horizontal   = models.PositiveIntegerField(verbose_name="Horizontal")
    Vertical     = models.PositiveIntegerField(verbose_name="Vertical")
    Oblicuas     = models.PositiveIntegerField(verbose_name="Oblicuas")
    Semanas      = models.PositiveIntegerField(default=3, verbose_name="Numero semanas")

    class Meta:
        verbose_name = "Recomendacion Varita"
        verbose_name_plural = "Recomendaciones Varita"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre