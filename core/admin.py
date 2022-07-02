from django.contrib import admin
from .models import Usuario,Tipousuario, Tipoalimento, Alimento,  Tipoproveedor, Proveedor, Transporte
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Tipousuario)
admin.site.register(Tipoalimento)
admin.site.register(Alimento)
admin.site.register(Tipoproveedor)
admin.site.register(Proveedor)
admin.site.register(Transporte)