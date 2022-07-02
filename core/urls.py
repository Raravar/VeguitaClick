from django.urls import path
from views import home, about, base, contacto, productos, registro, login, tienda, cerrarSesion
from tienda.views import catalogo, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito, misdespachos
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
    #Compra
    # path('despacho', despacho, name="despacho"),

]