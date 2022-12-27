from .models import Estudiante, Evaluacion
from rest_framework import serializers

class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estudiante
        fields = '__all__'
        
class EvaluacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Evaluacion
        fields = '__all__'