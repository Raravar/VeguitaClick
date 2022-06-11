from django.shortcuts import redirect, render
from core.forms import UsuarioForm


# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
   return render(request, "core/about.html")

def productos(request):
   return render(request, "core/productos.html")

def tienda(request):
       return render(request, "core/tienda.html")

def contacto(request):
   return render(request, "core/contacto.html")

def registro(request):
    datos = {'form': UsuarioForm()}

    if request.method == 'POST':
        formulario = UsuarioForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/registro.html', datos)