# Generated by Django 5.1.3 on 2024-11-15 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0003_rename_descrpcion_producto_productos_confiteria_descripcion_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos_confiteria',
            name='descuento_productos',
            field=models.FloatField(default=0.15),
            preserve_default=False,
        ),
    ]
