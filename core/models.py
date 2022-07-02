# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Tipoalimento(models.Model):
    idtipoalimento = models.BigAutoField(primary_key=True)
    nomtipoalimento = models.CharField(max_length=150, verbose_name="Nombre tipo alimento")
    codtipoalimento = models.CharField(max_length=150, blank=True, null=True, verbose_name="Codigo tipo alimento")

    class Meta:

        db_table = 'tipoalimento'
        verbose_name_plural = "Tipo Alimentos"

    def __str__(self):
        return self.nomtipoalimento


class Alimento(models.Model):
    idalimento = models.BigAutoField(primary_key=True)
    nomalimento = models.CharField(max_length=100, verbose_name="Nombre alimento")
    codalimento = models.CharField(max_length=100, blank=True, null=True, verbose_name="Codigo alimento")
    idtipoalimento = models.ForeignKey('Tipoalimento', models.DO_NOTHING, db_column='idtipousuario', verbose_name="Tipo alimento")
    pesoalimento = models.DecimalField(max_digits=38, decimal_places=1, blank=True, null=True, verbose_name="Peso alimento")
    precioalimento = models.BigIntegerField(verbose_name="Precio alimento")

    class Meta:

        db_table = 'alimento'

    def __str__(self):
        return self.nomalimento


class AlmtoInv(models.Model):
    idalimento = models.OneToOneField(Alimento, models.DO_NOTHING, db_column='idalimento', primary_key=True)
    idinventario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='idinventario')

    class Meta:

        db_table = 'almto_inv'
        unique_together = (('idalimento', 'idinventario'),)


class Compra(models.Model):
    idcompra = models.BigIntegerField(primary_key=True)
    fechacompra = models.DateField(blank=True, null=True)
    fechaestadocompra = models.DateField()
    numcompra = models.BigIntegerField()
    totalcompra = models.BigIntegerField()
    estadocompra = models.CharField(max_length=150)

    class Meta:

        db_table = 'compra'


class Despacho(models.Model):
    iddespacho = models.BigIntegerField(primary_key=True)
    nomdespacho = models.CharField(max_length=250, blank=True, null=True)
    fechainicdespacho = models.DateField(blank=True, null=True)
    fechafindespacho = models.DateField(blank=True, null=True)
    estadodespacho = models.CharField(max_length=250, blank=True, null=True)
    direcciondespacho = models.CharField(max_length=250, blank=True, null=True)
    idtransporte = models.ForeignKey('Transporte', models.DO_NOTHING, db_column='idtransporte')
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa', blank=True, null=True)

    class Meta:

        db_table = 'despacho'


class Detallecompra(models.Model):
    iddetallecompra = models.BigIntegerField(primary_key=True)
    cantidadcompra = models.BigIntegerField()
    preciocompra = models.BigIntegerField()
    idcompra = models.ForeignKey(Compra, models.DO_NOTHING, db_column='idcompra')
    idproveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='idproveedor')
    idalimento = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='idalimento')

    class Meta:

        db_table = 'detallecompra'


class Detalleventa(models.Model):
    iddetalleventa = models.BigIntegerField(primary_key=True)
    cantidaddetalleventa = models.BigIntegerField()
    precioventa = models.BigIntegerField()
    descuentoventa = models.BigIntegerField(blank=True, null=True)
    idventa = models.ForeignKey('Venta', models.DO_NOTHING, db_column='idventa')
    idalimento = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='idalimento')

    class Meta:

        db_table = 'detalleventa'


class EmpInv(models.Model):
    idempleado = models.OneToOneField('Empleado', models.DO_NOTHING, db_column='idempleado', primary_key=True)
    idinventario = models.ForeignKey('Inventario', models.DO_NOTHING, db_column='idinventario')

    class Meta:

        db_table = 'emp_inv'
        unique_together = (('idempleado', 'idinventario'),)


class Empleado(models.Model):
    idempleado = models.BigIntegerField(primary_key=True)
    nomempleado = models.CharField(max_length=150)
    apmaternoemp = models.CharField(max_length=150)
    appaternoemp = models.CharField(max_length=150)
    rutemp = models.BigIntegerField()
    dvrutemp = models.CharField(max_length=1)
    direccionemp = models.CharField(max_length=250)
    correoemp = models.CharField(max_length=80, blank=True, null=True)
    idtipoempleado = models.ForeignKey('Tipoempleado', models.DO_NOTHING, db_column='idtipoempleado')

    class Meta:

        db_table = 'empleado'


class Inventario(models.Model):
    idinventario = models.BigIntegerField(primary_key=True)
    fechainventario = models.DateField(blank=True, null=True)
    nominventario = models.CharField(max_length=250, blank=True, null=True)
    conteoinventario = models.BigIntegerField(blank=True, null=True)
    precioconteoinventario = models.DecimalField(max_digits=38, decimal_places=2, blank=True, null=True)

    class Meta:

        db_table = 'inventario'


class ProveAlmto(models.Model):
    idproveedor = models.OneToOneField('Proveedor', models.DO_NOTHING, db_column='idproveedor', primary_key=True)
    idalimento = models.ForeignKey(Alimento, models.DO_NOTHING, db_column='idalimento')

    class Meta:

        db_table = 'prove_almto'
        unique_together = (('idproveedor', 'idalimento'),)


class Proveedor(models.Model):
    idproveedor = models.BigAutoField(primary_key=True)
    nomproveedor = models.CharField(max_length=150, verbose_name="Nombre proveedor")
    telefproveedor = models.IntegerField(blank=True, null=True, verbose_name="Telefono proveedor")
    celuproveedor = models.IntegerField(blank=True, null=True, verbose_name="Celular proveedor")
    direccionproveedor = models.CharField(max_length=500, blank=True, null=True, verbose_name="Direccion proveedor")
    idtipoproveedor = models.ForeignKey('Tipoproveedor', models.DO_NOTHING, db_column='idtipoproveedor', verbose_name="Tipo proveedor")
    rutproveedor = models.BigIntegerField(verbose_name="Rut provedor")
    dvrutproveedor = models.BigIntegerField(verbose_name="Digito verificador proveedor")

    def __str__(self):
        return self.nomproveedor
    class Meta:

        db_table = 'proveedor'
        verbose_name_plural = "Proveedores"


class Tipoempleado(models.Model):
    idtipoempleado = models.BigAutoField(primary_key=True)
    nomtipoempleado = models.CharField(max_length=250)
    salariotipoempleado = models.BigIntegerField(blank=True, null=True)

    class Meta:

        db_table = 'tipoempleado'


class Tipoproveedor(models.Model):
    idtipoproveedor = models.BigAutoField(primary_key=True)
    nomtipoproveedor = models.CharField(max_length=300, blank=True, null=True, verbose_name="Nombre tipo proveedor")

    class Meta:

        db_table = 'tipoproveedor'
        verbose_name_plural = "Tipo Proveedores"

    def __str__(self):
        return self.nomtipoproveedor


class Tipousuario(models.Model):
    idtipousuario = models.BigAutoField(primary_key=True)
    nomtipousuario = models.CharField(max_length=50, verbose_name="Nombre tipo Cliente")

    class Meta:
        db_table = 'tipousuario'
        verbose_name_plural = "Tipo Cliente"

    def __str__(self):
        return self.nomtipousuario


class Transporte(models.Model):
    idtransporte = models.BigAutoField(primary_key=True)
    nomtransporte = models.CharField(max_length=250, verbose_name="Nombre Transporte")
    preciotransporte = models.IntegerField(verbose_name="Precio del transporte")
    # idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idempleado')

    class Meta:

        db_table = 'transporte'
        verbose_name_plural = "Transportes"
        verbose_name = "Transporte"

    def __str__(self):
        return self.nomtransporte


class Usuario(models.Model):
    idusuario = models.BigAutoField(primary_key=True)
    correousuario = models.CharField(max_length=200, verbose_name="Correo cliente")
    Contraseña = models.CharField(max_length=20)
    nomusuario = models.CharField(max_length=100, verbose_name="Nombre cliente")
    apellidosusuario = models.CharField(max_length=500, verbose_name="Apellidos cliente")
    estadousuario = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado cliente")
    fecharegistrousuario = models.DateField(blank=True, null=True, verbose_name="Fecha registro cliente")
    idtipousuario = models.ForeignKey(Tipousuario, models.DO_NOTHING, db_column='idtipousuario', verbose_name="Tipo cliente")

    class Meta:

        db_table = 'usuario'
        verbose_name_plural = "Clientes"
        verbose_name = "Cliente"

    def __str__(self):
        return self.nomusuario


class Venta(models.Model):
    idventa = models.BigIntegerField(primary_key=True)
    fechaventa = models.DateField()
    numventa = models.BigIntegerField()
    totalventa = models.BigIntegerField(blank=True, null=True)
    estadoventa = models.CharField(max_length=100)
    idempleado = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='idempleado')

    class Meta:

        db_table = 'venta'