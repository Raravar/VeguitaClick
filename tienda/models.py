from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'

class Transporte(models.Model):
    idtransporte = models.BigAutoField(primary_key=True)
    nomtransporte = models.CharField(max_length=250, verbose_name="Nombre Empresa Transporte")
    preciotransporte = models.IntegerField(verbose_name="Precio del transporte")

    def __str__(self):
        return self.nomtransporte  

    class Meta:

        db_table = 'transporte'
        verbose_name_plural = "Transportes"
        verbose_name = "Transporte"

OPCIONES_ESTADO = (
    ('Pendiente', 'Pendiente'),
    ('Aceptado', 'Aceptado'),
    ('Empacado', 'Empacado'),
    ('En camino', 'En camino'),
    ('Cancelado', 'Cancelado')
)

class Despacho(models.Model):
    iddespacho = models.BigAutoField(primary_key=True)
    direccion = models.CharField(max_length=64)
    comuna = models.CharField(max_length=32)
    estadodespacho = models.CharField(
        choices=OPCIONES_ESTADO,
        max_length=50,
        default="Pendiente",
        verbose_name="Estado del despacho"
        )

    idtransporte = models.ForeignKey(Transporte, models.DO_NOTHING, db_column='idtransporte', verbose_name="Empresa de transporte")
    nombrereceptor = models.CharField(max_length=64, verbose_name="Nombre de quien recibe el la compra")
    fechacompra = models.DateTimeField(auto_now_add=True, verbose_name="Fecha generación despacho")
    
    def __str__(self):
        return f'{self.nombrereceptor} -> {self.estadodespacho} -> {self.fechacompra} '

    class Meta:
        db_table = 'despacho'
        verbose_name_plural = "Despachos"
        verbose_name = "Despacho"
