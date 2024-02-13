from rest_framework import serializers
from tiposerviço.models import TipoServico

class TipoServicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoServico
        fields = '__all__'