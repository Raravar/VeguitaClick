from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from tienda.Carrito import Carrito
from tienda.models import Despacho, Producto, Productor
from tienda.forms import DireccionForm, ProductoresForm
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

def productores(request):
    datos = {
        'form' : ProductoresForm()
    }

    if request.method == 'POST':
        formulario = ProductoresForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Guardados correctamente"

    return render(request, 'tienda/productores.html', datos)

def listaproductores(request):
    productores = Productor.objects.all()
    datos = {
        "productores" : productores
    }
    return render(request, 'tienda/listaproductores.html', datos)


def form_mod_productor(request, id):

    productor = Productor.objects.get(nombreproductor=id)

    datos = {
        'form' : ProductoresForm(instance=productor)
    }

    if request.method == 'POST':
        formulario = ProductoresForm(request.POST, instance=productor)
        if formulario.is_valid:
            formulario.save()
            datos['form'] = formulario
            datos['mensaje'] = "Modificados correctamente"

    return render(request, 'tienda/form_mod_productor.html', datos)


def form_del_productor(request, id):

    productor = Productor.objects.get(nombreproductor=id)

    productor.delete()
    
    return redirect(to="listaproductores")
