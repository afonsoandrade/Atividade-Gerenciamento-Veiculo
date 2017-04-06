# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarcaDoVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('marca', models.CharField(max_length=20, help_text='Ex. Nissam, Honda,Fiat', verbose_name='Marca do Veiculo')),
            ],
            options={
                'ordering': ('marca',),
                'verbose_name_plural': 'Marca dos Veiculos',
                'verbose_name': 'Marca do Veiculo',
            },
        ),
        migrations.CreateModel(
            name='TipoDeVeiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, help_text='Ex. Carro ou Moto', verbose_name='Tipo de Veiculo')),
            ],
            options={
                'ordering': ('tipo',),
                'verbose_name_plural': 'Tpos de Veiculos',
                'verbose_name': 'Tipo de Veiculo',
            },
        ),
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50, verbose_name='Modelo')),
                ('placa', models.CharField(max_length=8, verbose_name='Placa')),
                ('cor', models.CharField(max_length=10, verbose_name='Modelo')),
                ('marca', models.ForeignKey(to='app_veiculos.MarcaDoVeiculo')),
                ('tipo', models.ForeignKey(to='app_veiculos.TipoDeVeiculo')),
            ],
            options={
                'ordering': ('tipo', 'marca', 'modelo'),
                'verbose_name_plural': 'Veiculos',
                'verbose_name': 'Veiculo',
            },
        ),
    ]
