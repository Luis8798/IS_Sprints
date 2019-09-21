# Generated by Django 2.2.5 on 2019-09-20 04:57

from django.db import migrations, models
import ventas.validaciones


class Migration(migrations.Migration):

    dependencies = [
        ('personas_juridicas', '0002_auto_20190918_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='juridica',
            name='celular',
            field=models.CharField(max_length=20, validators=[ventas.validaciones.validate_celular]),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='contacto_apellidos',
            field=models.CharField(max_length=75, validators=[ventas.validaciones.validate_letras]),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='contacto_cedula',
            field=models.CharField(max_length=13, validators=[ventas.validaciones.validate_cedula]),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='contacto_celular',
            field=models.CharField(max_length=20, validators=[ventas.validaciones.validate_celular]),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='contacto_nombres',
            field=models.CharField(max_length=75, validators=[ventas.validaciones.validate_letras]),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='contacto_telefono',
            field=models.CharField(max_length=20, validators=[ventas.validaciones.validate_fono_convencional]),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='ruc',
            field=models.CharField(max_length=13, validators=[ventas.validaciones.validate_ruc]),
        ),
        migrations.AlterField(
            model_name='juridica',
            name='telefono',
            field=models.CharField(max_length=20, validators=[ventas.validaciones.validate_fono_convencional]),
        ),
    ]
