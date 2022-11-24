from django.contrib import admin
from .models import Shoppingcart


class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product',)


admin.site.register(Shoppingcart, OrderAdmin)
