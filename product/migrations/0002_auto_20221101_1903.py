# Generated by Django 3.0.14 on 2022-11-01 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': '상품', 'verbose_name_plural': '상품'},
        ),
        migrations.AlterModelTable(
            name='product',
            table='shopping_product',
        ),
    ]
