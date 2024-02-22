from django.urls import path
from . import views

urlpatterns = [
    
    path('clientes/',views.ClienteCreateListView.as_view(), name = 'cliente-create-list'),
    path('clientes/<int:pk>/', views.ClienteRetrieveUpdateDestroyView.as_view() , name = 'cliente-detail-view'),
    
]
