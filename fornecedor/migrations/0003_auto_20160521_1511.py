# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-21 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedor', '0002_auto_20160521_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.AlterModelOptions(
            name='documento',
            options={'verbose_name': 'Documento', 'verbose_name_plural': 'Documentos'},
        ),
        migrations.AlterModelOptions(
            name='email',
            options={'verbose_name': 'Email', 'verbose_name_plural': 'Emails'},
        ),
        migrations.AlterModelOptions(
            name='endereco',
            options={'verbose_name': 'Endereco', 'verbose_name_plural': 'Enderecos'},
        ),
        migrations.AlterModelOptions(
            name='finaceiro',
            options={'verbose_name': 'Financeiro', 'verbose_name_plural': 'Finaceiros'},
        ),
        migrations.AlterModelOptions(
            name='fornecedor',
            options={'verbose_name': 'Fornecedor', 'verbose_name_plural': 'Fornecedores'},
        ),
        migrations.AlterModelOptions(
            name='produto',
            options={'verbose_name': 'Produto', 'verbose_name_plural': 'Produtos'},
        ),
        migrations.AlterModelOptions(
            name='unidade',
            options={'verbose_name': 'Unidade', 'verbose_name_plural': 'Unidades'},
        ),
        migrations.AlterField(
            model_name='produto',
            name='descricao',
            field=models.CharField(default='nulo', max_length=500, verbose_name='Descricao'),
        ),
        migrations.AlterField(
            model_name='unidade',
            name='fator',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Fator'),
        ),
        migrations.AddField(
            model_name='venda',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fornecedor.Produto'),
        ),
    ]
