# Generated by Django 5.0.2 on 2024-02-13 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviços', '0005_remove_servico_tipo_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='tipo_cliente',
            field=models.CharField(blank=True, choices=[('Dentista', 'Dentista'), ('Protetico', 'Protetico'), ('Particular', 'Particular')], max_length=20, null=True),
        ),
    ]
