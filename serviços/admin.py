from django.contrib import admin
from serviços.models import Servico

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('numero','nome_do_paciente' ,'cliente', 'tipo_do_cliente', 'tipo', 'data_de_entrada')
