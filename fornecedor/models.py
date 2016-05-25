# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Documento(models.Model):
	class Meta:
		verbose_name_plural = 'Documentos'
		verbose_name = 'Documento'

	tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, default="nulo")
	numero = models.DecimalField(verbose_name = 'Numero', max_digits = 25, decimal_places = 0, default=0 ) 
	emissao = models.DateTimeField(verbose_name = 'Emissao',auto_now = False, auto_now_add = True)
	vencimento = models.DateTimeField(verbose_name = 'Vencimento',auto_now = False, auto_now_add = True)
	ativo = models.BooleanField(verbose_name='Ativo')

	def __unicode__(self):
		return self.tipo

class Endereco(models.Model):
	class Meta:
		verbose_name_plural = 'Enderecos'
		verbose_name = 'Endereco'

	cep = models.DecimalField(verbose_name = 'Cep', max_digits = 15, decimal_places = 0, default=0 ) 
	tipo = models.CharField(verbose_name = 'Tipo', max_length = 100, default="nulo")
	descricao = models.CharField(verbose_name = 'Descricao', max_length = 2048, default="nulo")
	complemento = models.CharField(verbose_name = 'Complemento', max_length = 2048, default="nulo")
	numero = models.DecimalField(verbose_name = 'Numero', max_digits = 10, decimal_places = 0, default=0 ) 
	ativo = models.BooleanField(verbose_name='Ativo')

	def __unicode__(self):
		return self.tipo


class Email(models.Model):
	class Meta:
		verbose_name_plural = 'Emails'
		verbose_name = 'Email'

	descricao = models.CharField(verbose_name = 'Descricao', max_length = 2048, default="nulo")
	ativo = models.BooleanField(verbose_name='Ativo')

	def __unicode__(self):
		return self.descricao


	def __unicode__(self):
		return self.descricao

class Financeiro(models.Model):
	class Meta:
		verbose_name_plural = 'Finaceiros'
		verbose_name = 'Financeiro'

	parcela = models.DecimalField(verbose_name = 'Parcela', max_digits = 3, decimal_places = 0, default=1 ) 
	valor = models.DecimalField(verbose_name = 'Valor', max_digits = 10, decimal_places = 0, default=0 ) 
	desconto = models.DecimalField(verbose_name = 'Desconto', max_digits = 10, decimal_places = 0, default=0 ) 
	valor_pago = models.DecimalField(verbose_name = 'Valor_pago', max_digits = 10, decimal_places = 0, default=0 ) 
	

class Fornecedor(models.Model):
	class Meta:
		verbose_name_plural = 'Fornecedores'
		verbose_name = 'Fornecedor'

	nome = models.CharField(verbose_name = 'Nome', max_length = 100, default="nome")
	documento = models.ForeignKey(Documento)
	endereco = models.ForeignKey(Endereco)	
	email = models.ForeignKey(Email)

	def __unicode__(self):
		return self.nome

class Cliente(models.Model):
	class Meta:
		verbose_name_plural = 'Clintes'
		verbose_name = 'Cliente'

	nome = models.CharField(verbose_name = 'Nome', max_length = 100, default="nome")
	documento = models.ForeignKey(Documento)
	endereco = models.ForeignKey(Endereco)	
	email = models.ForeignKey(Email)

	def __unicode__(self):
		return self.nome

class Produto(models.Model):
	class Meta:
		verbose_name_plural = 'Produtos'
		verbose_name = 'Produto'

	nome = models.CharField(verbose_name = 'Nome', max_length = 100, default="nome")
	fornecedor = models.ForeignKey(Fornecedor)
	foto = models.ImageField(upload_to='produto/', height_field=None, width_field=None, max_length=100,blank=True,null=True, default = "fornecedor/static/imagens/default.jpg")
	descricao = models.CharField(verbose_name = 'Descricao', max_length = 500, default="nulo") 
	estoque = models.DecimalField(verbose_name = 'Estoque', max_digits = 10, decimal_places = 0, default=0 ) 

class Venda(models.Model):
	class Meta:
		verbose_name_plural = 'Vendas'
		verbose_name = 'Venda'

	produto = models.ForeignKey(Produto)
	cliente = models.ForeignKey(Cliente)
	financeiro = models.ForeignKey(Financeiro)

class Img(models.Model):
	imagens = models.ImageField(upload_to='imagens/')
