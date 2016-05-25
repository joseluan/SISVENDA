# -*- coding: utf-8 -*-
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(.*)$', 'django.views.static.serve', {'document_root': './media/'}),
    url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': './static/',}),
    url(r'^$', 'fornecedor.views.index', name='index'),
    url(r'^entrar/','fornecedor.views.entrar',name='entrar'),
    url(r'^fornecedores/', 'fornecedor.views.fornecedores', name='fornecedores'),
    url(r'^adicionar_produto/', 'fornecedor.views.adicionarProduto', name='adicionar_produto'),
    url(r'^vendas/', 'fornecedor.views.Vendas', name='vendas'),
    url(r'^vendaspagar/(?P<pk>[0-9]+)/$', 'fornecedor.views.VendasPagar',name='vendas_pagar'),
]

