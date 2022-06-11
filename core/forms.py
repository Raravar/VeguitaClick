from django.forms import ModelForm
from .models import Usuario
from django import forms

class UsuarioForm(ModelForm):
    Contraseña = forms.CharField(widget=forms.PasswordInput(render_value=True))
    
    class Meta:
        model = Usuario
         
        fields = [ 'nomusuario', 'apellidosusuario', 'idtipousuario', 'correousuario']

        labels = {
        "correousuario": "Correo",
        "nomusuario": "Nombres del Usuario",
        "apellidosusuario": "Apellidos",
        "idtipousuario": "Tipo de Usuario",
    }
