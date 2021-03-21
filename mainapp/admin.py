from django.contrib import admin

from .models import *


class ProductAdmin(admin.ModelAdmin):
    change_form_template = 'admin.html'
    #exclude = ('features',)


admin.site.register(Category)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment)