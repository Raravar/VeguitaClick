from django.shortcuts import redirect, render
from core.forms import UsuarioForm
from .models import Usuario
from django.contrib import messages


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
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'core/registro.html', datos)


def login(request):
    if request.method == 'POST':
        try:
            detalleUsuario = Usuario.objects.get(correousuario=request.POST['correo'], Contraseña =request.POST['password'])
            print("Usuario=", detalleUsuario)
            request.session['correousuario'] = detalleUsuario.correousuario
            return render(request, 'core/home.html')
        except Usuario.DoesNotExist as e:
            messages.success(request, 'Datos Incorrectos')
    return render(request, 'core/login.html')


def cerrarSesion(request):
    try:
        del request.session['correousuario']
    except:
        return render(request, 'core/home.html')
    return render(request, 'core/home.html')

def despacho(request):
    return render(request, "tienda/despacho.html")

