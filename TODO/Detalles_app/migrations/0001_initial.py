# Generated by Django 5.1 on 2024-10-30 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Detalles',
            fields=[
                ('ID_Detalles', models.IntegerField(primary_key=True, serialize=False)),
                ('ID_Orden', models.IntegerField()),
                ('ID_Cliente', models.IntegerField()),
                ('Cantidad', models.IntegerField()),
                ('Precio_Unitario', models.FloatField()),
                ('Subtotal', models.FloatField()),
                ('Descuento', models.FloatField()),
            ],
        ),
    ]
