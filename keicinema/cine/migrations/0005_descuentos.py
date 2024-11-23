# Generated by Django 5.1.3 on 2024-11-15 01:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cine', '0004_productos_confiteria_descuento_productos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Descuentos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_descuento', models.CharField(max_length=50)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cine.usuarios')),
            ],
        ),
    ]