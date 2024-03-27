from django.contrib import admin

# Register your models here.

from .models import Sale, Product
admin.site.register(Sale)
admin.site.register(Product)