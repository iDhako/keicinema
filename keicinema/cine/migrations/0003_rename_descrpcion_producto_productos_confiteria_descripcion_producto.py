# Generated by Django 5.1.3 on 2024-11-15 00:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0002_peliculas_valor_peliculas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productos_confiteria',
            old_name='descrpcion_producto',
            new_name='descripcion_producto',
        ),
    ]
