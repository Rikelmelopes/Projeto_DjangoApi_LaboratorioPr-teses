from django.urls import path
from . import views

urlpatterns = [
    
    path('tiposervicos/',views.TipoServicoCreateListView.as_view(), name = 'tiposerviço-create-list'),
    path('tiposervicos/<int:pk>/', views.TipoServicoRetrieveUpdateDestroyView.as_view() , name = 'tiposerviço-detail-view'),
    
]