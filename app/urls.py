
from django.contrib import admin
from django.urls import path
from clientes.views import ClienteCreateListView, ClienteRetrieveUpdateDestroyView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/',ClienteCreateListView.as_view(), name = 'cliente-create-list'),
    path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view() , name = 'cliente-detail-view')
]
