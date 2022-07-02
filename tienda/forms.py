from django.forms import ModelForm
from .models import Despacho
from django import forms
from django.forms.forms import *

class DireccionForm(ModelForm):
    class Meta:
        model = Despacho
         
        fields = ['direccion', 'comuna']

        labels = {
            "direccion": "Direccion",
            "comuna" : "Comuna",
        }
