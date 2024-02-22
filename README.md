
## Criar repositorio virtual

```
python -m venv venv
```

## Ativar venv

```
venv/Scripts/activate
```

## Instalar django

```
pip install django
```

## Intalar DjangoRestFramework

```
pip install djangorestframework
```

## Adicione djangonrestframework em STALLED_APPS em settings

```
'rest_framework'
```

## Criar coração do projeto (app)

```
django-admin startproject app .
```

## Rodar migrate

```
python manage.py migrate
```

## Criar SuperUsuario

```
python manage.py createsuperuser
```

## Criar app inicial

```
python manage.py startapp clientes

Adicione a app criada em STALLED_APPS em settings
```

## 1_ Criar Models

```
from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nome

-Sempre apos modificar os models rode:
python manage.py makemigrations
python manage.py migrate
```

## 2_ Criar Admin do model criado

```
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id','nome')
```

## 3_ Criar Serializers

```
from rest_framework import serializers
from clientes.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

```

## 4_ Criar Views usando generics views

```
importar Generics/Serializers

from rest_framework import generics
from clientes.models import Cliente
from clientes.serializers import ClienteSerializer

class ClienteCreateListView(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class ClienteRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
```

## 5_ Criar Urls separadas para cada tabela

```
Exemplos:
Urls/Clientes:

from django.urls import path
from . import views

urlpatterns = [
    
    path('clientes/',views.ClienteCreateListView.as_view(), name = 'cliente-create-list'),
    path('clientes/<int:pk>/', views.ClienteRetrieveUpdateDestroyView.as_view() , name = 'cliente-detail-view'),
    
]

Urls/Apps:

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('authentication.urls')),
    path('api/v1/', include('clientes.urls')),
    path('api/v1/', include('serviços.urls')),  
    path('api/v1/', include('tiposerviço.urls')),  
]

```
## 6_ instalar JWT para autenticação

```
pip install djangorestframework-simplejwt

-Adicionar em INSTALLED_APPS

'rest_framework_simplejwt',
```

## Criar app da autenticação / adicione em installed_apps

```
python manage.py startapp authentication

```
## Crie Urls / importar rest_framework_simplejwt

```
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('authentication/token/',TokenObtainPairView,name = 'token_obtain_pair')
]

configure o projeto com JWT/Adicione em settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (       
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

```




