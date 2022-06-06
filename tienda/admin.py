from django.contrib import admin
from .models import CategoriaProd, CategoriaProd, Producto
# Register your models here.

class CategoriaProdAdmin(admin.ModelAdmin):
   readonly_frields=("created","update")
class ProductoAdmin(admin.ModelAdmin):
    readonly_frields=("created","update")
admin.site.register(CategoriaProd, CategoriaProdAdmin)
admin.site.register(Producto,ProductoAdmin)