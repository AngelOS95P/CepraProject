from .models import RecoPeluche, RecoJuegosS, RecoTablero, RecoVarita
from rest_framework import serializers

class RecoPelucheSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecoPeluche
        fields = '__all__'

        
class RecoJuegosSSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecoJuegosS
        fields = '__all__'
        
class RecoTableroSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecoTablero
        fields = '__all__'
        
class RecoVaritaSerializer(serializers.ModelSerializer):
    class Meta:
        model=RecoVarita
        fields = '__all__'
        
