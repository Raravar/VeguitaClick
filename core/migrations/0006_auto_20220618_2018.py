# Generated by Django 3.2.3 on 2022-06-19 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_rename_contrasenausuario_usuario_contraseña'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='idproveedor',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tipoempleado',
            name='idtipoempleado',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
