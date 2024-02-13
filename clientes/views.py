
from rest_framework import generics
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

class ClienteCreateListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

        
class ClienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
        


    