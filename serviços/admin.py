from django.contrib import admin
from serviços.models import Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('id','numero','data_entrada','cliente')
