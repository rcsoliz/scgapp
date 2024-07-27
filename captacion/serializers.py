from rest_framework import serializers
from .models import Tipo, Ganado, Estancia, Zona

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields ='__all__'

class GanadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ganado
        fields ='__all__'

class EstanciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estancia
        fields ='__all__'

class ReporteGanadoSerializer(serializers.Serializer):
    cantidad =serializers.IntegerField()
    clases = GanadoSerializer(many=True)

