# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class User(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=50)
	email = models.CharField(max_length=80)
	password = models.CharField(max_length=50)

class Product(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=200)

	docfile = models.FileField(upload_to='documents/product/%Y/%m/%d')

	adress_of_location = models.CharField(max_length=100)
	numero = models.CharField(max_length=10)
	localizacao_block = models.CharField(max_length=60)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Company(models.Model):
	company_id = models.AutoField(primary_key=True)
	company_name = models.CharField(max_length=30)
	company_description = models.CharField(max_length=200)
	docfile = models.FileField(upload_to='documents/company/%Y/%m/%d')
	company_adress_of_location = models.CharField(max_length=100)
	company_numero = models.CharField(max_length=10)
	company_block = models.CharField(max_length=60)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favorite_Product(models.Model):
	favorite_product_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Service(models.Model):
	service_id = models.AutoField(primary_key=True)
	service_name = models.CharField(max_length=30)
	service_description = models.CharField(max_length=200)
	docfile = models.FileField(upload_to='documents/service/%Y/%m/%d')
	service_adress_of_location = models.CharField(max_length=100)
	service_numero = models.CharField(max_length=10)
	service_block = models.CharField(max_length=60)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favorite_Service(models.Model):
	favorite_service_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)

class Favorite_Company(models.Model):
	favorite_company_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
