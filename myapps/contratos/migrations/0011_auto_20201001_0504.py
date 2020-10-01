# Generated by Django 3.1.1 on 2020-10-01 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contratos', '0010_auto_20200928_0525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contrato',
            name='estado',
            field=models.CharField(choices=[('en espera', 'En espera'), ('aceptado', 'Aceptado'), ('rechazado', 'Rechazado'), ('finalizado', 'Finalizado'), ('cancelado', 'Cancelado'), ('borrador', 'Borrador')], default='borrador', max_length=15),
        ),
    ]