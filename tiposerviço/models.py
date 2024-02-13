from django.db import models

class TipoServico(models.Model):
    tipo = models.CharField(max_length=200)

    def __str__(self):
        return self.tipo
