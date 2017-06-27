# -*- coding: utf-8 -*-

from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file'
    )

class RegisterForm(forms.Form):
	name = forms.CharField(max_length = 30)
	email = forms.EmailField(max_length = 30)
	password = forms.CharField(widget = forms.PasswordInput())

class LoginForm(forms.Form):
	email = forms.EmailField(max_length = 30)
	password = forms.CharField(widget = forms.PasswordInput())

class RegisterProduct(forms.Form):
	product_name = forms.CharField(max_length=30)
	product_description = forms.CharField(max_length=200)
	image = forms.FileField()
	endereco = forms.CharField(max_length=100)
	numero = forms.CharField(max_length=10)
	bairro = forms.CharField(max_length=60)

class RegisterService(forms.Form):
	service_name = forms.CharField(max_length=30)
	service_description = forms.CharField(max_length=200)
	image = forms.FileField()
	endereco = forms.CharField(max_length=100)
	numero = forms.CharField(max_length=10)
	bairro = forms.CharField(max_length=60)

class RegisterEmpresa(forms.Form):
	empresa_name = forms.CharField(max_length=30)
	empresa_description = forms.CharField(max_length=200)
	image = forms.FileField()
	endereco = forms.CharField(max_length=100)
	numero = forms.CharField(max_length=10)
	bairro = forms.CharField(max_length=60)