# Generated by Django 3.2.3 on 2022-07-02 11:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alimento',
            fields=[
                ('idalimento', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomalimento', models.CharField(max_length=100, verbose_name='Nombre alimento')),
                ('codalimento', models.CharField(blank=True, max_length=100, null=True, verbose_name='Codigo alimento')),
                ('pesoalimento', models.DecimalField(blank=True, decimal_places=1, max_digits=38, null=True, verbose_name='Peso alimento')),
                ('precioalimento', models.BigIntegerField(verbose_name='Precio alimento')),
            ],
            options={
                'db_table': 'alimento',
            },
        ),
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('idcompra', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechacompra', models.DateField(blank=True, null=True)),
                ('fechaestadocompra', models.DateField()),
                ('numcompra', models.BigIntegerField()),
                ('totalcompra', models.BigIntegerField()),
                ('estadocompra', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'compra',
            },
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idempleado', models.BigIntegerField(primary_key=True, serialize=False)),
                ('nomempleado', models.CharField(max_length=150)),
                ('apmaternoemp', models.CharField(max_length=150)),
                ('appaternoemp', models.CharField(max_length=150)),
                ('rutemp', models.BigIntegerField()),
                ('dvrutemp', models.CharField(max_length=1)),
                ('direccionemp', models.CharField(max_length=250)),
                ('correoemp', models.CharField(blank=True, max_length=80, null=True)),
            ],
            options={
                'db_table': 'empleado',
            },
        ),
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('idinventario', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechainventario', models.DateField(blank=True, null=True)),
                ('nominventario', models.CharField(blank=True, max_length=250, null=True)),
                ('conteoinventario', models.BigIntegerField(blank=True, null=True)),
                ('precioconteoinventario', models.DecimalField(blank=True, decimal_places=2, max_digits=38, null=True)),
            ],
            options={
                'db_table': 'inventario',
            },
        ),
        migrations.CreateModel(
            name='Tipoalimento',
            fields=[
                ('idtipoalimento', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomtipoalimento', models.CharField(max_length=150, verbose_name='Nombre tipo alimento')),
                ('codtipoalimento', models.CharField(blank=True, max_length=150, null=True, verbose_name='Codigo tipo alimento')),
            ],
            options={
                'verbose_name_plural': 'Tipo Alimentos',
                'db_table': 'tipoalimento',
            },
        ),
        migrations.CreateModel(
            name='Tipoempleado',
            fields=[
                ('idtipoempleado', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomtipoempleado', models.CharField(max_length=250)),
                ('salariotipoempleado', models.BigIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'tipoempleado',
            },
        ),
        migrations.CreateModel(
            name='Tipoproveedor',
            fields=[
                ('idtipoproveedor', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomtipoproveedor', models.CharField(blank=True, max_length=300, null=True, verbose_name='Nombre tipo proveedor')),
            ],
            options={
                'verbose_name_plural': 'Tipo Proveedores',
                'db_table': 'tipoproveedor',
            },
        ),
        migrations.CreateModel(
            name='Tipousuario',
            fields=[
                ('idtipousuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomtipousuario', models.CharField(max_length=50, verbose_name='Nombre tipo Cliente')),
            ],
            options={
                'verbose_name_plural': 'Tipo Cliente',
                'db_table': 'tipousuario',
            },
        ),
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('idventa', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fechaventa', models.DateField()),
                ('numventa', models.BigIntegerField()),
                ('totalventa', models.BigIntegerField(blank=True, null=True)),
                ('estadoventa', models.CharField(max_length=100)),
                ('idempleado', models.ForeignKey(db_column='idempleado', on_delete=django.db.models.deletion.DO_NOTHING, to='core.empleado')),
            ],
            options={
                'db_table': 'venta',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idusuario', models.BigAutoField(primary_key=True, serialize=False)),
                ('correousuario', models.CharField(max_length=200, verbose_name='Correo cliente')),
                ('Contraseña', models.CharField(max_length=20)),
                ('nomusuario', models.CharField(max_length=100, verbose_name='Nombre cliente')),
                ('apellidosusuario', models.CharField(max_length=500, verbose_name='Apellidos cliente')),
                ('estadousuario', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado cliente')),
                ('fecharegistrousuario', models.DateField(blank=True, null=True, verbose_name='Fecha registro cliente')),
                ('idtipousuario', models.ForeignKey(db_column='idtipousuario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipousuario', verbose_name='Tipo cliente')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idproveedor', models.BigAutoField(primary_key=True, serialize=False)),
                ('nomproveedor', models.CharField(max_length=150, verbose_name='Nombre proveedor')),
                ('telefproveedor', models.IntegerField(blank=True, null=True, verbose_name='Telefono proveedor')),
                ('celuproveedor', models.IntegerField(blank=True, null=True, verbose_name='Celular proveedor')),
                ('direccionproveedor', models.CharField(blank=True, max_length=500, null=True, verbose_name='Direccion proveedor')),
                ('rutproveedor', models.BigIntegerField(verbose_name='Rut provedor')),
                ('dvrutproveedor', models.BigIntegerField(verbose_name='Digito verificador proveedor')),
                ('idtipoproveedor', models.ForeignKey(db_column='idtipoproveedor', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipoproveedor', verbose_name='Tipo proveedor')),
            ],
            options={
                'verbose_name_plural': 'Proveedores',
                'db_table': 'proveedor',
            },
        ),
        migrations.AddField(
            model_name='empleado',
            name='idtipoempleado',
            field=models.ForeignKey(db_column='idtipoempleado', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipoempleado'),
        ),
        migrations.CreateModel(
            name='Detalleventa',
            fields=[
                ('iddetalleventa', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cantidaddetalleventa', models.BigIntegerField()),
                ('precioventa', models.BigIntegerField()),
                ('descuentoventa', models.BigIntegerField(blank=True, null=True)),
                ('idalimento', models.ForeignKey(db_column='idalimento', on_delete=django.db.models.deletion.DO_NOTHING, to='core.alimento')),
                ('idventa', models.ForeignKey(db_column='idventa', on_delete=django.db.models.deletion.DO_NOTHING, to='core.venta')),
            ],
            options={
                'db_table': 'detalleventa',
            },
        ),
        migrations.CreateModel(
            name='Detallecompra',
            fields=[
                ('iddetallecompra', models.BigIntegerField(primary_key=True, serialize=False)),
                ('cantidadcompra', models.BigIntegerField()),
                ('preciocompra', models.BigIntegerField()),
                ('idalimento', models.ForeignKey(db_column='idalimento', on_delete=django.db.models.deletion.DO_NOTHING, to='core.alimento')),
                ('idcompra', models.ForeignKey(db_column='idcompra', on_delete=django.db.models.deletion.DO_NOTHING, to='core.compra')),
                ('idproveedor', models.ForeignKey(db_column='idproveedor', on_delete=django.db.models.deletion.DO_NOTHING, to='core.proveedor')),
            ],
            options={
                'db_table': 'detallecompra',
            },
        ),
        migrations.AddField(
            model_name='alimento',
            name='idtipoalimento',
            field=models.ForeignKey(db_column='idtipousuario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.tipoalimento', verbose_name='Tipo alimento'),
        ),
        migrations.CreateModel(
            name='ProveAlmto',
            fields=[
                ('idproveedor', models.OneToOneField(db_column='idproveedor', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.proveedor')),
                ('idalimento', models.ForeignKey(db_column='idalimento', on_delete=django.db.models.deletion.DO_NOTHING, to='core.alimento')),
            ],
            options={
                'db_table': 'prove_almto',
                'unique_together': {('idproveedor', 'idalimento')},
            },
        ),
        migrations.CreateModel(
            name='EmpInv',
            fields=[
                ('idempleado', models.OneToOneField(db_column='idempleado', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.empleado')),
                ('idinventario', models.ForeignKey(db_column='idinventario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.inventario')),
            ],
            options={
                'db_table': 'emp_inv',
                'unique_together': {('idempleado', 'idinventario')},
            },
        ),
        migrations.CreateModel(
            name='AlmtoInv',
            fields=[
                ('idalimento', models.OneToOneField(db_column='idalimento', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='core.alimento')),
                ('idinventario', models.ForeignKey(db_column='idinventario', on_delete=django.db.models.deletion.DO_NOTHING, to='core.inventario')),
            ],
            options={
                'db_table': 'almto_inv',
                'unique_together': {('idalimento', 'idinventario')},
            },
        ),
    ]
