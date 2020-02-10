# Generated by Django 2.2.4 on 2020-02-10 15:19

from django.db import migrations, models
import django.db.models.deletion
import financiero.validaciones


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orden_pago', '0001_initial'),
        ('personas_naturales', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrdenFacturacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_cliente', models.CharField(choices=[('Natural', 'Natural'), ('Jurídica', 'Jurídica')], max_length=15)),
                ('cod_orden_fact', models.CharField(blank=True, max_length=15)),
                ('n_tramite', models.CharField(blank=True, default='No asignado', max_length=15, null=True)),
                ('n_factura', models.CharField(blank=True, default='No asignado', max_length=15, null=True)),
                ('anexo_factura', models.FileField(blank=True, null=True, upload_to='uploads/facturas/')),
                ('fecha', models.CharField(max_length=30)),
                ('ruc_ci', models.CharField(max_length=13)),
                ('razon_nombres', models.CharField(max_length=200)),
                ('concepto', models.CharField(max_length=300)),
                ('n_participantes', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('observaciones', models.CharField(max_length=500)),
                ('comentarios', models.CharField(blank=True, max_length=500, null=True)),
                ('estado', models.CharField(blank=True, choices=[('ACTV', 'Grabado'), ('SLCE', 'Solicitud Enviada'), ('ACPF', 'Autorizada por Financiero'), ('PNDP', 'Pendiente de Cobro'), ('CNCL', 'Cancelada'), ('ANLD', 'Anulada')], default='ACTV', max_length=5, null=True)),
                ('subtotal', models.FloatField(blank=True, default=0.0, null=True)),
                ('descuento_fact', models.FloatField(blank=True, default=0.0, null=True)),
                ('descuento_total', models.FloatField(blank=True, default=0.0, null=True)),
                ('valor_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, validators=[financiero.validaciones.validate_positivo])),
                ('valor_pendiente', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, validators=[financiero.validaciones.validate_positivo])),
                ('motivo_anular', models.CharField(blank=True, max_length=500, null=True)),
                ('centro_costos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orden_pago.Centro_Costos')),
            ],
            options={
                'ordering': ['cod_orden_fact'],
            },
        ),
        migrations.CreateModel(
            name='OrdenFacturacionParticipante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_evento', models.CharField(max_length=500)),
                ('cod_evento', models.CharField(max_length=20)),
                ('valor_evento', models.FloatField(default=0)),
                ('descuento', models.FloatField(default=0)),
                ('valor', models.FloatField(default=0)),
                ('orden', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orden_facturacion.OrdenFacturacion')),
                ('participante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='personas_naturales.Persona_Natural')),
            ],
        ),
    ]
