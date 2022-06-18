from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from tienda.Carrito import Carrito
from tienda.models import Producto


def catalogo(request):
    #return HttpResponse("Hola Pythonizando")
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

