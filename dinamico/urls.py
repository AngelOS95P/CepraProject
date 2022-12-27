from django.urls import path
from . import views

urlpatterns = [
    path('publicaciones/articulos',views.publicaciones, name="dinamico"),
    path('publicaciones/tutoriales',views.tutoriales, name="tutoriales"),

]