# Generated by Django 2.2.4 on 2020-01-10 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Centro_Costos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Egresos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=200)),
                ('centroc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orden_pago.Centro_Costos')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenPago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_ord_pago', models.CharField(blank=True, max_length=15, null=True)),
                ('n_tramite', models.CharField(blank=True, max_length=15, null=True)),
                ('fecha', models.CharField(max_length=30)),
                ('fecha_tramite', models.CharField(max_length=30)),
                ('fecha_pago', models.CharField(max_length=30)),
                ('estado', models.CharField(blank=True, choices=[('GRBD', 'Grabado'), ('ENVD', 'Enviado'), ('AUTR', 'Autorizado'), ('ANLD', 'Anulado')], default='GRBD', max_length=5, null=True)),
                ('tipo_proveedor', models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], max_length=10)),
                ('proveedor', models.CharField(max_length=200)),
                ('tipo_comprobante', models.CharField(choices=[('FC', 'Factura'), ('NV', 'Nota de venta'), ('LC', 'Liquidación de compra'), ('CP', 'Comprobantes de pago')], max_length=5)),
                ('n_comprobante', models.CharField(blank=True, max_length=20, null=True)),
                ('concepto', models.CharField(max_length=500)),
                ('forma_pago', models.CharField(blank=True, choices=[('TR', 'Transferencia'), ('CH', 'Cheque')], max_length=5, null=True)),
                ('observacion', models.CharField(blank=True, max_length=500, null=True)),
                ('anexo', models.FileField(blank=True, null=True, upload_to='uploads/orden_pago/')),
                ('motivo_anular', models.CharField(blank=True, max_length=500, null=True)),
                ('centro_costos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orden_pago.Centro_Costos')),
                ('egreso', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orden_pago.Egresos')),
            ],
        ),
    ]
