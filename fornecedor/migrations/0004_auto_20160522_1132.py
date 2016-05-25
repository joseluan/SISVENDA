# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-22 14:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0003_auto_20160521_1511'),
    ]

    operations = [
        migrations.RenameField(
            model_name='venda',
            old_name='item',
            new_name='produto',
        ),
        migrations.AddField(
            model_name='produto',
            name='fornecedor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fornecedor.Fornecedor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='produto',
            name='nome',
            field=models.CharField(default='nome', max_length=100, verbose_name='Nome'),
        ),
    ]