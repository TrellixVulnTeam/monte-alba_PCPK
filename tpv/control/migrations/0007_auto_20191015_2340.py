# Generated by Django 2.2.6 on 2019-10-16 05:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0006_auto_20191014_0030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detallepedido',
            name='pedido',
            field=models.ForeignKey(db_column='pedido_id', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_pedidos', to='control.Pedido'),
        ),
    ]
