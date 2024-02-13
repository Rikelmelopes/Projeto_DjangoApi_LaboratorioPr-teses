from django.db import models
from clientes.models import Cliente
from tiposerviço.models import TipoServico

class Servico(models.Model):
    numero = models.IntegerField()
    
    tipo = models.ForeignKey(
        TipoServico,
        on_delete=models.PROTECT,
        related_name = 'tiposerviço'
    )
    
    data_entrada = models.DateField()
    
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name = 'serviços'
    )
    
    def __str__(self):
        return self.numero