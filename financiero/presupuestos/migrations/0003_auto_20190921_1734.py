# Generated by Django 2.2.4 on 2019-09-21 22:34

from django.db import migrations, models
import financiero.presupuestos.models


class Migration(migrations.Migration):

    dependencies = [
        ('presupuestos', '0002_auto_20190920_1737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presupuestoevento',
            name='costo_hora_instructor',
            field=models.DecimalField(decimal_places=3, max_digits=7, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Costo Hora Instructor'),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='estado',
            field=models.BooleanField(default=None),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='honorario_instructor',
            field=models.DecimalField(decimal_places=3, max_digits=7, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Honorario Instructor'),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='ingresos',
            field=models.DecimalField(decimal_places=3, max_digits=14, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Ingresos sin descuento'),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='lapiz',
            field=models.DecimalField(decimal_places=3, max_digits=5, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Lápiz'),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='movilizacion_personal',
            field=models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Movilización del personal'),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='movilizacion_personal_ciudad',
            field=models.DecimalField(decimal_places=3, max_digits=10, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Movilización del personal (dentro de la ciudad'),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='otros_materiales',
            field=models.DecimalField(decimal_places=3, max_digits=7, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Otros materiales'),
        ),
        migrations.AlterField(
            model_name='presupuestoevento',
            name='pendrives',
            field=models.DecimalField(decimal_places=3, max_digits=5, validators=[financiero.presupuestos.models.validate_positivo], verbose_name='Pendrives'),
        ),
    ]