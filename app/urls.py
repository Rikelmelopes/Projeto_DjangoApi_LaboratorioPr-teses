
from django.contrib import admin
from django.urls import path

from clientes.views import ClienteCreateListView, ClienteRetrieveUpdateDestroyView
from serviços.views import ServicoCreateListView ,ServicoRetrieveUpdateDestroyView
from tiposerviço.views import TipoServicoCreateListView ,TipoServicoRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('clientes/',ClienteCreateListView.as_view(), name = 'cliente-create-list'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view() , name = 'cliente-detail-view'),
    
    path('serviços/',ServicoCreateListView.as_view(), name = 'serviço-create-list'),
    path('serviços/<int:pk>/', ServicoRetrieveUpdateDestroyView.as_view() , name = 'serviço-detail-view'),
    
    path('tiposerviços/',TipoServicoCreateListView.as_view(), name = 'tiposerviço-create-list'),
    path('tiposerviços/<int:pk>/', TipoServicoRetrieveUpdateDestroyView.as_view() , name = 'tiposerviço-detail-view'),
    
    
]
