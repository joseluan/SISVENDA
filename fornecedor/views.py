# -*- coding: utf-8 -*-
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
	produtos = Produto.objects.all()
	paginator = Paginator(produtos, 15) 
    
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
	fornecedores = Produto.objects.all()
	paginator = Paginator(produtos, 15) 
    
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
def adicionarProduto(request):
	if request.method == 'POST':
		form = ImageUploadForm(request.POST, request.FILES)
		cd = Img.objects.create(imagens = form.cleaned_data['image']).save()
	return render(request,'adicionarproduto.html',{})


@login_required(login_url='/entrar/')
def Vendas(request):
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
def VendasPagar(request,pk):
	venda = Venda.objects.get(id=pk)
	if request.method == 'POST':
		venda.financeiro.valor_pago += 10
		venda.financeiro.parcela -= 1
		venda.save()
		return render(request,'pagarvenda.html',{'venda': venda})
	return render(request,'pagarvenda.html',{'venda': venda})
