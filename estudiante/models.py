from django.db import models

class Estudiante(models.Model):
    id      = models.AutoField(primary_key=True)
    nombre  = models.CharField(max_length=100, verbose_name="Nombre")
    edad_cron_mes = models.PositiveIntegerField(verbose_name="Edad Cronologica Meses")
    edad_eval_mes = models.PositiveIntegerField(verbose_name="Edad Evaluacion Meses")
    puntuacion    = models.FloatField(verbose_name="Total area Motora ")
    puntuacionMF  = models.FloatField(default=0, verbose_name="Puntuacion tipica motricidad fina ")
    puntuacionMP  = models.FloatField(default=0, verbose_name="Puntuacion tipica motricidad perceptiva")

    MASCULINO = 'Masculino'
    FEMENINO  = 'Femenino'
    SEXO_Option = [
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_Option, default=MASCULINO, verbose_name="Sexo")
    
    DIESTRO = 'Diestro'
    ZURDO  = 'Zurdo'
    LATERALIDAD_Option = [
        (DIESTRO, 'Diestro'),
        (ZURDO, 'Zurdo'),
    ]
    lateralidad = models.CharField(max_length=10, choices=LATERALIDAD_Option, default=DIESTRO, verbose_name="Lateralidad")

    unidad_edu  = models.CharField(max_length=100, verbose_name="Unidad Educativa")
    nivel   = models.CharField(max_length=100, verbose_name="Nivel")
    ciudad  = models.CharField(max_length=100, verbose_name="Ciudad") 


    class Meta:
        verbose_name = "estudiante"
        verbose_name_plural = "estudiantes"
        ordering = ['id']

    def __str__(self):   
        return self.nombre




class Evaluacion(models.Model):
    id           = models.AutoField(primary_key=True)
    Estudiante   = models.ForeignKey(Estudiante, verbose_name="Estudiante Evaluado", on_delete=models.CASCADE)
    ADQUIRIDO    = 'Adquirido'
    En_Proceso   = 'En proceso'
    No_Adquirido = 'No adquirido'
    No_Aplica    = 'No aplica'
    Calificacion = [
        (ADQUIRIDO, 'Adquirido'),
        (En_Proceso, 'En proceso'),
        (No_Adquirido, 'No adquirido'),
        (No_Aplica, 'No aplica'),
    ]
    M52  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Abre una puerta:")
    M53  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Ensarta 4 cuentas grandes:")
    M54  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Pasa páginas de un libro:")
    M55  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Sujeta el papel mientras dibuja:")
    M56  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Dobla una hoja de papel por la mitad:")
    M57  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Corta con tijeras:")
    M58  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Dobla dos veces el papel:")
    M59  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Abre un candado con llave:")
    M60  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Hace una pelota arrugando papel:")
    M61  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Hace un nudo:")
    M62  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Se toca con el pulgar las yemas de los dedos de la mano:")
    M66  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Mete anillas en un soporte:")
    M67  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Saca la pastilla de la botella:")
    M68  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia una línea vertical:")
    M69  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia un círculo:")
    M70  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia una cruz:")
    M71  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Corta con tijeras siguiendo una línea:")
    M72  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia las letras V, H, T:")
    M73  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia un triangulo:")
    M74  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Dibuja una persona (incluyendo 6 elementos):")
    M75  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia un cuadrado:")
    M76  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia palabras sencillas:")
    M77  = models.CharField(max_length=20, choices=Calificacion, default=ADQUIRIDO, verbose_name="Copia los números del 1 al 15:")
    
    class Meta:
        verbose_name = "evaluacion"
        verbose_name_plural = "evaluaciones"
        ordering = ['-id']

    def __str__(self):
        return self.Estudiante.nombre