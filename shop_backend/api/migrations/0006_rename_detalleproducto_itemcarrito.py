# Generated by Django 5.0.6 on 2024-06-16 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_categoria_descripcion_carrito_detalleproducto'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DetalleProducto',
            new_name='ItemCarrito',
        ),
    ]
