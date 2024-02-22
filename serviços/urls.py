from django.urls import path
from . import views

urlpatterns = [
    
    path('servicos/',views.ServicoCreateListView.as_view(), name = 'serviço-create-list'),
    path('servicos/<int:pk>/', views.ServicoRetrieveUpdateDestroyView.as_view() , name = 'serviço-detail-view'),
    
]

