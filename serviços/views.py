from rest_framework import generics
from serviços.models import Servico
from serviços.serializers import ServicoSerializer

class ServicoCreateListView(generics.ListCreateAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
    
class ServicoRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Servico.objects.all()
    serializer_class = ServicoSerializer
