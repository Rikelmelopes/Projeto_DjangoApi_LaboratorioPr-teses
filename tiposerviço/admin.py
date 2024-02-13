from django.contrib import admin
from tiposerviço.models import TipoServico

@admin.register(TipoServico)
class TipoServicoAdmin(admin.ModelAdmin):
    list_display = ('id','tipo')
    
