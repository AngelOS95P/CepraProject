from .models import Sesion, Peluche, Tablero, Varita, JuegoTopos, JuegoRompeC, JuegoLaberinto, JuegoLetras,JuegoColorear
from rest_framework import serializers

class SesionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sesion
        fields = '__all__'
        

class PelucheSerializer(serializers.ModelSerializer):
    class Meta:
        model=Peluche
        fields = '__all__'

class TableroSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tablero
        fields = '__all__'

class VaritaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Varita
        fields = '__all__'          


class JuegoToposSerializer(serializers.ModelSerializer):
    class Meta:
        model=JuegoTopos
        fields = '__all__'


class JuegoRompeCSerializer(serializers.ModelSerializer):
    class Meta:
        model=JuegoRompeC
        fields = '__all__'

class JuegoLaberintoSerializer(serializers.ModelSerializer):
    class Meta:
        model=JuegoLaberinto
        fields = '__all__'

class JuegoLetrasSerializer(serializers.ModelSerializer):
    class Meta:
        model=JuegoLetras
        fields = '__all__'


class JuegoColorearSerializer(serializers.ModelSerializer):
    class Meta:
        model=JuegoColorear
        fields = '__all__'
