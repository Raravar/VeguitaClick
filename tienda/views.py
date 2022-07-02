from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from tienda.Carrito import Carrito
from tienda.models import Despacho, Producto
from tienda.forms import DireccionForm
from django.contrib import messages




def catalogo(request):
    productos = Producto.objects.all()
    return render(request, "tienda/catalogo.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("catalogo")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("catalogo")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("catalogo")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("catalogo")



def despacho(request):
    datos = {'form': DireccionForm()}

    if request.method == 'POST':
        formulario = DireccionForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Despacho guardado correctamente"

    return render(request, 'tienda/despacho.html', datos)

def misdespachos(request):
    despachos = Despacho.objects.all()
    return render(request, "tienda/misdespachos.html", {'despachos':despachos})


