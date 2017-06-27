# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm

from myproject.myapp.forms import RegisterForm, LoginForm, RegisterProduct, RegisterService, RegisterEmpresa
from myproject.myapp.models import User, Product, Service, Company

# Create your views here.

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )


def listar_usuarios(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:

            users = User.objects.all()
            return render(request, 'listar_usuarios.html', {'users':users})
    except:
        return redirect('/users/log_in/')


def home(request):
    return render(request, 'home.html', {})

def sobre(request):
    return render(request, 'sobre.html', {})

def produtos(request):
    products = Product.objects.all()
    return render(request, 'produtos.html', {'products':products})

def empresas(request):
    company = Company.objects.all()
    return render(request, 'empresas.html', {'company':company})

def servicos(request):
    services = Service.objects.all()
    return render(request, 'servicos.html', {'services':services})

def empresas_favoritas(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:         
            return render(request, 'empresas_favoritas.html', {})
    except:
        return redirect('/users/log_in/')

def produtos_favoritos(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:         
            return render(request, 'produtos_favoritos.html', {})
    except:
        return redirect('/users/log_in/')

def servicos_favoritos(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:         
            return render(request, 'servicos_favoritos.html', {})
    except:
        return redirect('/users/log_in/')

def minhas_empresas(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:
            empresas = Company.objects.filter(user_id=user_logged.id)
            return render(request, 'minhas_empresas.html', {'empresas':empresas})
    except:
        return redirect('/users/log_in/')

def meus_produtos(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:
            products = Product.objects.filter(user_id=user_logged.id)
            return render(request, 'meus_produtos.html', {'products':products})
    except:
        return redirect('/users/log_in/')

def meus_servicos(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:
            services = Service.objects.filter(user_id=user_logged.id)   
            return render(request, 'meus_servicos.html', {'services':services})
    except:
        return redirect('/users/log_in/')

def register(request):
    return render(request, 'cadastro.html', {})

def cadastro_produto(request):
    return render(request, 'cadastro_produto.html', {})

def cadastro_servico(request):
    return render(request, 'cadastro_servico.html', {})

def cadastro_empresa(request):
    return render(request, 'cadastro_empresa.html', {})

def edicao_produto(request):
    produto_id = request.GET['id_produto']
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:
            products = Product.objects.get(product_id=produto_id)
            return render(request, 'editar_produto.html', {'products':products})
    except:
        return redirect('/users/meus_produtos/')

def editar_produto(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:
            products = Product.objects.filter(user_id=user_logged.id)
            return render(request, 'editar_produto.html', {'products':products})
    except:
        return redirect('/users/log_in/')
    
def edicao_servico(request):
    return render(request, 'edicao_servico.html', {})

def edicao_empresa(request):
    return render(request, 'edicao_empresa.html', {})

def contato(request):
    return render(request, 'contato.html', {})

def register_submit(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            data = register_form.cleaned_data
            
            try:
                user_new = User(name=data['name'], email=data['email'],
                         password=data['password'])
                user_new.save()
            except ValidationError, e:
                pass

            return render(request, 'login.html', {'type': 2,
        'msg': 'Cadastro realizado com sucesso!'})

        return render(request, 'cadastro.html', {'type': 1,
        'msg': 'Dados invalidos!'})
    else:
        return render(request, 'cadastro.html', {'type': 0,
        'msg': 'Erro ao realizar seu cadastro, entre em contato com o administrador do site.'})

def product_submit(request):
    if request.method == "POST":
        register_form = RegisterProduct(request.POST, request.FILES)

        if register_form.is_valid():
            data = register_form.cleaned_data
            
            try:
                user_logged = User.objects.get(id = request.session['id'])

                product_new = Product(name=data['product_name'], description=data['product_description'], docfile=request.FILES['image'],  adress_of_location=data['endereco'], numero=data['numero'], localizacao_block=data['bairro'], user_id=user_logged.id)
                product_new.save()
            except ValidationError, e:
                pass
                        
            return render(request, 'perfil.html', {'type': 2, 'msg': 'Cadastro realizado com sucesso!'})
            
        return render(request, 'cadastro_produto.html', {'type': 1,
        'msg': 'Dados invalidos!'})
    else:
        return render(request, 'cadastro_produto.html', {'type': 0,
        'msg': 'Erro ao realizar seu cadastro, entre em contato com o administrador do site.'})

def service_submit(request):    
    if request.method == "POST":
        register_form = RegisterService(request.POST, request.FILES)

        if register_form.is_valid():
            data = register_form.cleaned_data
            
            try:
                user_logged = User.objects.get(id = request.session['id'])

                service_new = Service(service_name=data['service_name'], service_description=data['service_description'], docfile=request.FILES['image'], service_adress_of_location=data['endereco'], service_numero=data['numero'], service_block=data['bairro'], user_id=user_logged.id)
                service_new.save()
            except ValidationError, e:
                pass
                        
            return render(request, 'perfil.html', {'type': 2, 'msg': 'Cadastro realizado com sucesso!'})
            
        return render(request, 'cadastro_servico.html', {'type': 1,
        'msg': 'Dados invalidos!'})
    else:
        return render(request, 'cadastro_servico.html', {'type': 0,
        'msg': 'Erro ao realizar seu cadastro, entre em contato com o administrador do site.'})

def empresa_submit(request):    
    if request.method == "POST":
        register_form = RegisterEmpresa(request.POST, request.FILES)

        if register_form.is_valid():
            data = register_form.cleaned_data
            
            try:
                user_logged = User.objects.get(id = request.session['id'])

                empresa_new = Company(company_name=data['empresa_name'], company_description=data['empresa_description'], docfile=request.FILES['image'], company_adress_of_location=data['endereco'], company_numero=data['numero'], company_block=data['bairro'], user_id=user_logged.id)
                empresa_new.save()
            except ValidationError, e:
                pass
                        
            return render(request, 'perfil.html', {'type': 2, 'msg': 'Cadastro realizado com sucesso!'})
            
        return render(request, 'cadastro_empresa.html', {'type': 1,
        'msg': 'Dados invalidos!'})
    else:
        return render(request, 'cadastro_empresa.html', {'type': 0,
        'msg': 'Erro ao realizar seu cadastro, entre em contato com o administrador do site.'})

def login(request):
    return render(request, 'login.html', {})

def login_submit(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            data = login_form.cleaned_data

            try:
                user_loged = User.objects.get(email = unicode(data['email']),
                    password = data['password'])

                if user_loged:
                    request.session['id'] = user_loged.id
                    request.session['usr_success'] = True
                    # Retornar Usuario
                    return render(request, 'perfil.html', {})
                else:
                    return render(request, 'login.html', {'type': 1,
                        'msg': 'E-mail e/ou Senha invalidos!'})
            except User.DoesNotExist, e:
                pass

        return render(request, 'login.html', {'type': 1,
                        'msg': 'E-mail e/ou Senha invalidos!'})
    else:
        return render(request, 'login.html', {'type': 0,
        'msg': 'Erro ao realizar seu login, entre em contato com o administrador do site.'})

def logout(request):
    request.session.pop('id'), request.session.pop('usr_success')
    return redirect('/users/home/')

def profile(request):
    try:
        user_logged = User.objects.get(id = request.session['id'])
        
        if user_logged:         
            return render(request, 'perfil.html', {})
    except:
        return redirect('/users/log_in/')

