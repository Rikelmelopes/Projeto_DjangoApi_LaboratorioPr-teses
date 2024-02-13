# Generated by Django 5.0.2 on 2024-02-13 16:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviços', '0002_alter_servico_tipo'),
        ('tiposerviço', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tiposerviço', to='tiposerviço.tiposervico'),
        ),
    ]
