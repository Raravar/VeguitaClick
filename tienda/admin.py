from django.contrib import admin
from .models import Producto, Transporte, Despacho, ProductoStock, Productor
# Register your models here.

admin.site.register(Producto)
admin.site.register(Transporte)
admin.site.register(Productor)
admin.site.register(ProductoStock)
class Admin(admin.ModelAdmin):
    list_display = ('direccion',  'estadodespacho', 'idtransporte', 'nombrereceptor')
    list_editable = ('estadodespacho', 'idtransporte')


admin.site.register(Despacho, Admin)