# Generated by Django 4.1.6 on 2023-06-03 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articulos', '0011_imagenesarticulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagenesarticulo',
            old_name='id_articulo',
            new_name='imagen',
        ),
    ]