# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.home, name='home'),

    url(r'^listar_usuarios/$', views.listar_usuarios, name='listar_usuarios'),

    url(r'^edicao_produto$', views.edicao_produto, name='edicao_produto'),
    url(r'^editar_produto/$', views.editar_produto, name='editar_produto'),

    url(r'^edicao_servico/$', views.edicao_servico, name='edicao_servico'),
    url(r'^edicao_empresa/$', views.edicao_empresa, name='edicao_empresa'),

    url(r'^cadastro_produto/$', views.cadastro_produto, name='cadastro_produto'),
    url(r'^cadastro_servico/$', views.cadastro_servico, name='cadastro_servico'),
    url(r'^cadastro_empresa/$', views.cadastro_empresa, name='cadastro_empresa'),

    url(r'^register/$', views.register, name='register'),
    url(r'^register/submit$', views.register_submit, name='register_submit'),
    url(r'^product/submit$', views.product_submit, name='product_submit'),
    url(r'^service/submit$', views.service_submit, name='service_submit'),
    url(r'^empresa/submit$', views.empresa_submit, name='empresa_submit'),

    url(r'^log_in/$', views.login, name='login'),
    url(r'^log_in/profile$', views.login_submit, name='login_submit'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^sobre/$', views.sobre, name='sobre'),
    url(r'^empresas/$', views.empresas, name='empresas'),
    url(r'^empresas_favoritas/$', views.empresas_favoritas, name='empresas_favoritas'),
    url(r'^produtos/$', views.produtos, name='produtos'),
    url(r'^produtos_favoritos/$', views.produtos_favoritos, name='produtos_favoritos'),
    url(r'^servicos/$', views.servicos, name='servicos'),
    url(r'^servicos_favoritos/$', views.servicos_favoritos, name='servicos_favoritos'),
    url(r'^contato/$', views.contato, name='contato'),
    url(r'^meus_produtos/$', views.meus_produtos, name='meus_produtos'),
    url(r'^meus_servicos/$', views.meus_servicos, name='meus_servicos'),
    url(r'^minhas_empresas/$', views.minhas_empresas, name='minhas_empresas'),
]
