# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-26 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0014_financeiro_valorparcela'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financeiro',
            name='valor',
        ),
        migrations.AddField(
            model_name='produto',
            name='valor',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='Valor'),
        ),
    ]
