from django.urls import path
from views import home, about, base, contacto, productos, registro, login, tienda, cerrarSesion
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


]