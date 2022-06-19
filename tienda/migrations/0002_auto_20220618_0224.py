# Generated by Django 3.2.3 on 2022-06-18 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='producto',
            options={},
        ),
        migrations.RemoveField(
            model_name='producto',
            name='created',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='disponibilidad',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='update',
        ),
        migrations.AlterField(
            model_name='producto',
            name='categoria',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='CategoriaProd',
        ),
    ]