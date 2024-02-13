from rest_framework import generics
from tiposerviço.models import TipoServico
from tiposerviço.serializers import TipoServicoSerializer

class TipoServicoCreateListView(generics.ListCreateAPIView):
    queryset = TipoServico.objects.all()
    serializer_class = TipoServicoSerializer
    
class TipoServicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TipoServico.objects.all()
    serializer_class = TipoServicoSerializer