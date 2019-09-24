# Generated by Django 2.2.4 on 2019-09-23 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenIngreso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(max_length=12)),
                ('numeroTramite', models.PositiveIntegerField()),
                ('numeroFactura', models.PositiveIntegerField()),
                ('identificacion', models.CharField(max_length=10)),
                ('razonSocial', models.CharField(max_length=50)),
                ('centroCosto', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=150)),
                ('formaPago', models.CharField(choices=[('cheque', 'Cheque'), ('transferencia', 'Transferencia'), ('deposito', 'Depósito'), ('tarjeta', 'Tarjeta de Crédito')], default='cheque', max_length=30)),
                ('valor', models.FloatField()),
                ('anexo', models.FileField(upload_to='uploads/')),
                ('fechaPago', models.CharField(max_length=12)),
                ('numeroDocumento', models.PositiveIntegerField()),
                ('banco', models.CharField(max_length=30)),
                ('emisoraTarjeta', models.CharField(choices=[('visa', 'Visa'), ('mastercard', 'Mastercard'), ('american', 'American Express'), ('diners', 'Diners'), ('discover', 'Discover')], max_length=20)),
                ('estado', models.BooleanField(blank=True, default=None, null=True)),
            ],
        ),
    ]
