from django.urls import path
from views import home, about, base, contacto, productos, registro, login, tienda, cerrarSesion
from tienda.views import catalogo, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, misdespachos, productores, listaproductores, form_mod_productor, form_del_productor, productosstock,form_mod_stock,form_del_stock, stock
urlpatterns = [
    path('', home, name="home"),
    path('about', about, name="about"),
    path('base', base, name="base"),
    path('contacto', contacto, name="contacto"),
    path('productos', productos, name="productos"),
    path('registro', registro, name="registro"),
    path('login', login, name="login"),
    path('cerrarSesion', cerrarSesion, name="cerrarSesion"),
    path('form-tienda', tienda, name="tienda"),
    #Tienda
    path('catalogo', catalogo, name="Catalogo"),
    path('misdespachos', misdespachos, name="misdespachos"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('productores', productores, name="productores"),
    path('listaproductores', listaproductores, name="listaproductores"),
    path('form_mod_productor/<id>', form_mod_productor, name="form_mod_productor"),
    path('form_del_productor/<id>', form_del_productor, name="form_del_productor"),

    path('productosstock', productosstock, name="productosstock"),
    path('form_mod_stock/<id>', form_mod_stock, name="form_mod_stock"),
    path('form_del_stock/<id>', form_del_stock, name="form_del_stock"),
    path('stock', stock, name="stock"),


]
    #Compra
    # path('despacho', despacho, name="despacho"),

