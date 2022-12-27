from rest_framework import viewsets
from .models import RecoPeluche, RecoJuegosS, RecoTablero, RecoVarita
from .serializer import RecoPelucheSerializer, RecoJuegosSSerializer, RecoTableroSerializer, RecoVaritaSerializer

class RecoPelucheViewSet(viewsets.ModelViewSet):
    queryset = RecoPeluche.objects.all()
    serializer_class = RecoPelucheSerializer

class RecoJuegosSViewSet(viewsets.ModelViewSet):
    queryset = RecoJuegosS.objects.all()
    serializer_class = RecoJuegosSSerializer

class RecoTableroViewSet(viewsets.ModelViewSet):
    queryset = RecoTablero.objects.all()
    serializer_class = RecoTableroSerializer

class RecoVaritaViewSet(viewsets.ModelViewSet):
    queryset = RecoVarita.objects.all()
    serializer_class = RecoVaritaSerializer