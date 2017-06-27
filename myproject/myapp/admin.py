from django.contrib import admin
from myproject.myapp.models import Document, User, Product, Service, Company

admin.site.register(Document)

admin.site.register(User)
admin.site.register(Product)
admin.site.register(Service)
admin.site.register(Company)
