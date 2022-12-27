from django.db import models
from estudiante.models import Estudiante 

# Create your models here.

class Sesion(models.Model):
    id       = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante", on_delete=models.CASCADE)
    fecha    = models.DateTimeField(auto_now=True, verbose_name="Fecha de Sesion")
    
    PelucheMoFi = 'Peluche MoFi'
    JuegosSerios= 'Juegos Serios'
    TableroMoFi = 'Tablero Mofi'
    TableroMoPe = 'Tablero MoPe'
    Varita      = 'Varita'
    Herramienta_Sesion = [
        (PelucheMoFi, 'Peluche MoFi'),
        (JuegosSerios,'Juegos Serios'),
        (TableroMoFi, 'Tablero Mofi'),
        (TableroMoPe, 'Tablero MoPe'),
        (Varita, 'Varita'),
    ]
    Herramienta = models.CharField(max_length=60,choices=Herramienta_Sesion, default=PelucheMoFi, verbose_name="Herramienta usada")

    class Meta:
        verbose_name = "sesion"
        verbose_name_plural = "sesiones"
        ordering = ['-id']

    def __str__(self):
        return "Estudiante: "+self.Estudiante.nombre + " ID-Ses: "+str(self.id)

class Peluche(models.Model):
    id   = models.AutoField(primary_key=True)
    Tipo = models.CharField(max_length=100, verbose_name="Tipo Acividad")
    Tiempo  = models.CharField(max_length=20, verbose_name="Tiempo de Acividad")

    SI = 'SI'
    NO  = 'NO'
    Necesita_Ayuda = [
        (SI, 'SI'),
        (NO, 'NO'),
    ]
    Ayuda = models.CharField(max_length=2,choices=Necesita_Ayuda, default=NO, verbose_name="Necesita Ayuda")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Peluche"
        verbose_name_plural = "Actividades Peluche"
        ordering = ['-id']

    def __str__(self):
        return self.Tipo 

class Tablero(models.Model):
    id   = models.AutoField(primary_key=True)
    Actividad = models.CharField(max_length=100, verbose_name="Tipo Acividad")
    Tiempo  = models.CharField(max_length=20, verbose_name="Tiempo de Acividad")
    Errores = models.PositiveIntegerField(verbose_name="Numero de Errores")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Tablero"
        verbose_name_plural = "Actividades Tablero"
        ordering = ['-id']



class Varita(models.Model):
    id   = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=100, verbose_name="Tipo Acividad")
    Tiempo  = models.CharField(max_length=20, verbose_name="Tiempo de Acividad")
    Intentos = models.PositiveIntegerField(verbose_name="Numero de Intentos")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Varita"
        verbose_name_plural = "Actividades Varita"
        ordering = ['-id']

    def __str__(self):
        return self.Nivel

class JuegoTopos(models.Model):
    id   = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=100, verbose_name="Nivel")
    Cant_Agujeros = models.PositiveIntegerField(verbose_name="Cantidad Agujeros")
    Tiem_Juego = models.PositiveIntegerField(verbose_name="Tiempo de Juego")
    Tiem_Arriba = models.PositiveIntegerField(verbose_name="Tiempo topos superficie")
    Tiem_Salida = models.PositiveIntegerField(verbose_name="Tiempo de salida de Topos")
    Porce_Gana = models.PositiveIntegerField(verbose_name="Porcentaje necesario")
    Num_Aciertos = models.PositiveIntegerField(verbose_name="Numero de Aciertos")
    Num_Perdidos = models.PositiveIntegerField(verbose_name="Numero de Perdidos")
    Num_Errores = models.PositiveIntegerField(verbose_name="Numero de Errores")
    Porce_Logrado = models.PositiveIntegerField(verbose_name="Porcentaje Logrado")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Juego Topos"
        verbose_name_plural = "Actividades Juego Topos"
        ordering = ['-id']

    def __str__(self):
        return self.Nivel

class JuegoRompeC(models.Model):
    id   = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=100, verbose_name="Nivel")
    Tiem_Necesario = models.PositiveIntegerField(verbose_name="Tiempo Necesario")
    Tiem_Logrado = models.PositiveIntegerField(verbose_name="Tiempo Logrado")
    Precision = models.CharField(max_length=100, verbose_name="Precision")
    Num_Piezas = models.PositiveIntegerField(verbose_name="Numero de Piezas")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Juego Rompecabezas"
        verbose_name_plural = "Actividades Juego Rompecabezas"
        ordering = ['-id']

    def __str__(self):
        return self.Nivel

class JuegoLaberinto(models.Model):
    id   = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=100, verbose_name="Nivel")
    Tiem_Necesario = models.PositiveIntegerField(verbose_name="Tiempo Necesario")
    Tiem_Logrado = models.PositiveIntegerField(verbose_name="Tiempo Logrado")
    Intentos = models.PositiveIntegerField(verbose_name="Numero de Intentos")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Laberinto"
        verbose_name_plural = "Actividades Laberinto"
        ordering = ['-id']

    def __str__(self):
        return self.Nivel

class JuegoLetras(models.Model):
    id   = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=100, verbose_name="Nivel")
    Tiem_Necesario = models.PositiveIntegerField(verbose_name="Tiempo Necesario")
    Tiem_Logrado = models.PositiveIntegerField(verbose_name="Tiempo Logrado")
    Intentos = models.PositiveIntegerField(verbose_name="Numero de Intentos")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Letra"
        verbose_name_plural = "Actividades Letras"
        ordering = ['-id']

    def __str__(self):
        return self.Nivel

class JuegoColorear(models.Model):
    id   = models.AutoField(primary_key=True)
    Nivel = models.CharField(max_length=100, verbose_name="Nivel")
    Tiem_Necesario = models.CharField(max_length=100, verbose_name="Tiempo Jugado")
    Colores = models.CharField(max_length=100, verbose_name="Colores Usados")
    Sesion   = models.ForeignKey(Sesion, verbose_name="Sesion de Intervencion", on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Actividad Colorear"
        verbose_name_plural = "Actividades Colorear"
        ordering = ['-id']

    def __str__(self):
        return self.Nivel