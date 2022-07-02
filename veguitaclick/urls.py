"""veguitaclick URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from tienda import views as tv
from tienda.views import agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, despacho, misdespachos, productores, listaproductores, form_mod_productor, form_del_productor, productosstock, stock

urlpatterns = [
    path('', views.home, name="home"),
    path('about-me/', views.about, name="about"),
    path('productos/', views.productos, name="productos"),
    path('tienda/', views.tienda, name="tienda"),
    path('contacto/', views.contacto, name="contacto"),
    path('registro/', views.registro, name="registro"),
    path('login/', views.login, name="login"),
    path('admin/', admin.site.urls),
    path('cerrarSesion/', views.cerrarSesion, name="cerrarSesion"),
    # Tienda
    path('catalogo/', tv.catalogo, name="catalogo"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('despacho/', tv.despacho, name="despacho"),
    path('misdespachos/', tv.misdespachos, name="misdespachos"),
    path('productores', productores, name="productores"),
    path('listaproductores', listaproductores, name="listaproductores"),
    path('form_mod_productor/<id>', form_mod_productor, name="form_mod_productor"),
    path('form_del_productor/<id>', form_del_productor, name="form_del_productor"),

    path('productosstock', productosstock, name="productosstock"),
    path('stock', stock, name="stock"),
]
