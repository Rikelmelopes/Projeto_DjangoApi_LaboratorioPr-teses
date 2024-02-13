
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
import as generics e os serializers

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

## 5_ Criar Urls

```
from django.contrib import admin
from django.urls import path

Sempre importe as Views criadas 

from clientes.views import ClienteCreateListView, ClienteRetrieveUpdateDestroyView 

path('clientes/',ClienteCreateListView.as_view(), name = 'cliente-create-list'),
path('clientes/<int:pk>/', ClienteRetrieveUpdateDestroyView.as_view() , name = 'cliente-detail-view')
```

