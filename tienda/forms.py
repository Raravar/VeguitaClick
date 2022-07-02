from django.forms import ModelForm
from .models import Despacho, ProductoStock, Productor
from django import forms
from django.forms.forms import *

class DireccionForm(ModelForm):
    class Meta:
        model = Despacho
         
        fields = ['comuna', 'idtransporte', 'nombrereceptor']

        labels = {
            "direccion": "Direccion",
            "comuna" : "Comuna",
            "idtransporte" : "Empresa de transporte",
            "nombrereceptor" : "Nombre de quien recibe la compra"
        }

class ProductoresForm(ModelForm):
    class Meta:
        model = Productor
         
        fields = ['nombreproductor', 'telefonoproductor']

        labels = {
            "nombreproductor": "Nombre del productor",
            "telefonoproductor" : "Telefono del productor",
        }

class ProductosForm(ModelForm):
    class Meta:
        model = ProductoStock
         
        fields = ['nombre', 'categoria', 'nombreproductor']

        labels = {
            "nombre": "Nombre del producto",
            "categoria" : "Categoría del producto",
            "nombreproductor" : "Productor",
        }


