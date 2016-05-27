# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': './static/',}),
    url(r'^$', 'fornecedor.views.index', name='index'),
    url(r'^entrar/','fornecedor.views.entrar',name='entrar'),
    url(r'^adicionar_fornecedor/', 'fornecedor.views.adicionarfornecedor', name='adicionar_fornecedor'),
    url(r'^fornecedores/', 'fornecedor.views.fornecedores', name='fornecedores'),
    url(r'^adicionar_produto/', 'fornecedor.views.adicionarproduto', name='adicionar_produto'),
    url(r'^editarproduto/(?P<pk>[0-9]+)/$', 'fornecedor.views.editarproduto', name='editar_produto'),
    url(r'^vendas/', 'fornecedor.views.vendas', name='vendas'),
    url(r'^vendasexcluir/(?P<pk>[0-9]+)/$', 'fornecedor.views.vendasexcluir', name='vendas_excluir'),
    url(r'^comprar/(?P<pk>[0-9]+)/$', 'fornecedor.views.comprar', name='comprar'),
    url(r'^vendaspagar/(?P<pk>[0-9]+)/$', 'fornecedor.views.vendaspagar',name='vendas_pagar'),
]

