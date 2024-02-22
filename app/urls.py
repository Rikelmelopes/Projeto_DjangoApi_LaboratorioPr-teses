
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('clientes.urls')),
    path('api/v1/', include('serviços.urls')),  
    path('api/v1/', include('tiposerviço.urls')),  
]

