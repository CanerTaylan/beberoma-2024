from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(ShoppingCartItem)
class ShoppingCartItemAdmin(admin.ModelAdmin):
    '''Admin View for ShoppingCartItem'''


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'total_price',
                    'status', 'created_date', 'updated_date']
