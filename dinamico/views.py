from django.shortcuts import render
from .models import Publicacion, Contenido
# Create your views here.

def publicaciones(request):
    publicaciones = Publicacion.objects.all()
    return render(request,"dinamico/publi.html", {'publicacion':publicaciones})

def tutoriales(request):
    tuto = Contenido.objects.all()
    return render(request,"dinamico/tutorial.html",{'tuto':tuto})
