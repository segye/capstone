# Generated by Django 3.0.14 on 2022-11-18 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20221118_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(blank=True, max_length=10000),
        ),
    ]
