# Generated by Django 2.2.5 on 2019-09-24 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orden_facturacion', '0003_auto_20190924_1354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordenfacturacion',
            name='fecha',
            field=models.CharField(max_length=30),
        ),
    ]