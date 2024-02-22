from django.db import models
from clientes.models import Cliente
from tiposerviço.models import TipoServico

TIPO_PAGAMENTO_CHOICES = [
    ('Pago','Pago'),
    ('Não pago','Não pago'),
]

TIPO_CLIENTE_CHOICES = [
        ('Dentista', 'Dentista'),
        ('Protetico', 'Protetico'), 
        ('Particular', 'Particular'), 
    ]

class Servico(models.Model):
    numero = models.IntegerField()
    nome_do_paciente = models.CharField(max_length=200)
    cliente = models.ForeignKey(
        Cliente,
        on_delete=models.PROTECT,
        related_name = 'serviços'
    )
    tipo_do_cliente = models.CharField(max_length=20, choices=TIPO_CLIENTE_CHOICES, null=True, blank=True)
    tipo = models.ForeignKey(
        TipoServico,
        on_delete=models.PROTECT,
        related_name = 'tiposerviço'
    )
    data_de_entrada = models.DateField()
    detalhes = models.TextField(max_length=200 ,null=True, blank=True )
    status = models.CharField(max_length=20, choices=TIPO_PAGAMENTO_CHOICES , null=True, blank=True)
    def __str__(self):
        return str(self.numero)