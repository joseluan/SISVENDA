# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, logout, login
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from fornecedor.models import *
from fornecedor.forms import *


def entrar(request):
	if request.method=='POST':
		cusuario = request.POST.get("usuario")
		csenha = request.POST.get("senha")

		user = authenticate(username=cusuario, password=csenha)
		if user is not None:
			if user.is_active:
				login(request, user)
				request.session['usuario'] = cusuario
				return HttpResponseRedirect('/') 
			else:
				return HttpResponseRedirect('/') 
		else:
			
			return HttpResponseRedirect('/')   

	return render(request,'entrar.html',{
		'usuario': True,
		})


def index(request):
	if request.method=='POST':
		produtos = Produto.objects.filter(nome__contains=request.POST.get("pesquisa"))
		paginator = Paginator(produtos, 20) 
	    
		page = request.GET.get('page')
		lista_produtos = []
		try:
			lista_produtos = paginator.page(page)
		except PageNotAnInteger:
			lista_produtos = paginator.page(1)
		except EmptyPage:
			lista_produtos = paginator.page(paginator.num_pages)

		return render(request,'index.html',{'produtos': lista_produtos})

	else:
		produtos = Produto.objects.all()
		paginator = Paginator(produtos, 20) 
	    
		page = request.GET.get('page')
		lista_produtos = []
		try:
			lista_produtos = paginator.page(page)
		except PageNotAnInteger:
			lista_produtos = paginator.page(1)
		except EmptyPage:
			lista_produtos = paginator.page(paginator.num_pages)

		return render(request,'index.html',{'produtos': lista_produtos})


@login_required(login_url='/entrar/')
def fornecedores(request):
	if request.method == 'POST':
		
		fornecedores = Fornecedor.objects.filter(nome__contains=request.POST.get("pesquisa"))
		paginator = Paginator(fornecedores, 15) 
	    
		page = request.GET.get('page')
		lista_fornecedores = []
		try:
			lista_fornecedores = paginator.page(page)
		except PageNotAnInteger:
			lista_fornecedores = paginator.page(1)
		except EmptyPage:
			lista_fornecedores = paginator.page(paginator.num_pages)

		return render(request,'fornecedores.html',{'fornecedores': lista_fornecedores})
	else:
		fornecedores = Fornecedor.objects.all()
		paginator = Paginator(fornecedores, 15) 
	    
		page = request.GET.get('page')
		lista_fornecedores = []
		try:
			lista_fornecedores = paginator.page(page)
		except PageNotAnInteger:
			lista_fornecedores = paginator.page(1)
		except EmptyPage:
			lista_fornecedores = paginator.page(paginator.num_pages)

		return render(request,'fornecedores.html',{'fornecedores': lista_fornecedores})


@login_required(login_url='/entrar/')
def adicionaremail(request):
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		criar = True
		for user in Email.objects.all():
			if user.username == request.POST.get("email"):
				criar = False
		if criar:	
			try:
				user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))
				user.is_admin = True
				user.is_staff = True
				user.is_superuser = True
				user.save(using=self._db)
				fornecedor = Fornecedor.objects.create(username=request.POST.get("username"),nome=request.POST.get("nome"), emailfornecedor= request.POST.get("email"))
				fornecedor.save()
				return HttpResponseRedirect('/') 
			except Exception, e:
				return render(request,'adicionarfornecedor.html',{})
	return render(request,'adicionarfornecedor.html',{})	



@login_required(login_url='/entrar/')
def adicionarfornecedor(request):
	if request.method == 'POST':
		criar = True
		for user in Img.objects.all():
			if user.username == request.POST.get("username"):
				criar = False
		if criar:	
			try:
				user = User.objects.create_user(request.POST.get("username"), request.POST.get("email"), request.POST.get("password"))
				user.save()
				fornecedor = Fornecedor.objects.create(username=request.POST.get("username"),nome=request.POST.get("nome"), emailfornecedor= request.POST.get("email"))
				fornecedor.save()
				return HttpResponseRedirect('/') 
			except Exception, e:
				return render(request,'adicionarfornecedor.html',{})
	return render(request,'adicionarfornecedor.html',{})	


@login_required(login_url='/entrar/')
def vendas(request):
	if request.method == 'POST':
		vendas = Venda.objects.filter(produto__nome__contains=request.POST.get("pesquisa"))
		paginator = Paginator(vendas,20) 
	    
		page = request.GET.get('page')
		lista_vendas = []
		try:
			lista_vendas = paginator.page(page)
		except PageNotAnInteger:
			lista_vendas = paginator.page(1)
		except EmptyPage:
			lista_vendas = paginator.page(paginator.num_pages)

		return render(request,'vendas.html',{'vendas': lista_vendas})
	else:
		vendas = Venda.objects.all()
		paginator = Paginator(vendas,20) 
	    
		page = request.GET.get('page')
		lista_vendas = []
		try:
			lista_vendas = paginator.page(page)
		except PageNotAnInteger:
			lista_vendas = paginator.page(1)
		except EmptyPage:
			lista_vendas = paginator.page(paginator.num_pages)

		return render(request,'vendas.html',{'vendas': lista_vendas})


@login_required(login_url='/entrar/')
def vendaspagar(request,pk):
	venda = Venda.objects.get(id=pk)
	venda.financeiro.valor_pago += 10
	venda.financeiro.parcela -= 1
	venda.save()
	if request.method == 'POST':
		venda = Venda.objects.get(id=pk)
		venda.financeiro.valor_pago += 10
		venda.financeiro.parcela -= 1
		venda.save()

		vendas = Venda.objects.all()
		paginator = Paginator(vendas,20) 
	    
		page = request.GET.get('page')
		lista_vendas = []
		try:
			lista_vendas = paginator.page(page)
		except PageNotAnInteger:
			lista_vendas = paginator.page(1)
		except EmptyPage:
			lista_vendas = paginator.page(paginator.num_pages)

		return render(request,'vendas.html',{'vendas': lista_vendas})
	return render(request,'pagarvenda.html',{'venda': venda})


@login_required(login_url='/entrar/')
def vendasexcluir(request,pk):
	Venda.objects.get(id=pk).delete()
	if request.method == 'POST':
		vendas = Venda.objects.filter(produto__nome__contains=request.POST.get("pesquisa"))
		paginator = Paginator(vendas,20) 
	    
		page = request.GET.get('page')
		lista_vendas = []
		try:
			lista_vendas = paginator.page(page)
		except PageNotAnInteger:
			lista_vendas = paginator.page(1)
		except EmptyPage:
			lista_vendas = paginator.page(paginator.num_pages)

		return render(request,'vendas.html',{'vendas': lista_vendas})
	else:
		vendas = Venda.objects.all()
		paginator = Paginator(vendas,20) 
	    
		page = request.GET.get('page')
		lista_vendas = []
		try:
			lista_vendas = paginator.page(page)
		except PageNotAnInteger:
			lista_vendas = paginator.page(1)
		except EmptyPage:
			lista_vendas = paginator.page(paginator.num_pages)

		return render(request,'vendas.html',{'vendas': lista_vendas})


@login_required(login_url='/entrar/')
def comprar(request,pk):

	if request.method == 'POST':
		venda = Venda.objects.create(produto=Produto.objects.get(id=pk),financeiro=Financeiro.objects.all()[0])
		return render(request,'comprar.html',{'produto': Produto.objects.get(id=pk)})	
	return render(request,'comprar.html',{'produto': Produto.objects.get(id=pk)})


def editarproduto(request,pk):
	
	if request.method == 'POST':
		p = Produto.objects.get(id=pk)
		p.valor = request.POST.get("valor")
		p.nome = request.POST.get("nome")
		p.descricao = request.POST.get("descricao")
		p.estoque = request.POST.get("estoque")
		p.save()
	else:
		produto = Produto.objects.get(id=pk)
		return render(request,'editarproduto.html',{'produto':produto})


@login_required(login_url='/entrar/')
def adicionarproduto(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
	    p = Produto.objects.create(foto=form.cleaned_data['image'])
	    p.valor = request.POST.get("valor")
	    p.nome = request.POST.get("nome")
	    p.descricao = request.POST.get("descricao")
	    p.estoque = request.POST.get("estoque")
	    p.save()
	    return HttpResponseRedirect('/') 	
    return render(request,'adicionarproduto.html',{})


