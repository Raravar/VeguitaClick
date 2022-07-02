from django.forms import ModelForm
from .models import Despacho
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
