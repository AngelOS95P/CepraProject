
from rest_framework import viewsets
from .models import Sesion, Peluche, Tablero, Varita, JuegoTopos, JuegoRompeC, JuegoLaberinto, JuegoLetras,JuegoColorear
from .serializer import SesionSerializer, PelucheSerializer, TableroSerializer, VaritaSerializer, JuegoToposSerializer, JuegoRompeCSerializer, JuegoLaberintoSerializer, JuegoLetrasSerializer, JuegoColorearSerializer

class SesionViewSet(viewsets.ModelViewSet):
    queryset = Sesion.objects.all()
    serializer_class = SesionSerializer

class PelucheViewSet(viewsets.ModelViewSet):
    queryset = Peluche.objects.all()
    serializer_class = PelucheSerializer

class TableroViewSet(viewsets.ModelViewSet):
    queryset = Tablero.objects.all()
    serializer_class = TableroSerializer

class VaritaViewSet(viewsets.ModelViewSet):
    queryset = Varita.objects.all()
    serializer_class = VaritaSerializer

class JuegoToposViewSet(viewsets.ModelViewSet):
    queryset = JuegoTopos.objects.all()
    serializer_class = JuegoToposSerializer

class JuegoRompeCViewSet(viewsets.ModelViewSet):
    queryset = JuegoRompeC.objects.all()
    serializer_class = JuegoRompeCSerializer

class JuegoLaberintoViewSet(viewsets.ModelViewSet):
    queryset = JuegoLaberinto.objects.all()
    serializer_class = JuegoLaberintoSerializer


class JuegoLetrasCViewSet(viewsets.ModelViewSet):
    queryset = JuegoLetras.objects.all()
    serializer_class = JuegoLetrasSerializer


class JuegoColorearViewSet(viewsets.ModelViewSet):
    queryset = JuegoColorear.objects.all()
    serializer_class = JuegoColorearSerializer