# Generated by Django 4.1.3 on 2022-11-19 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("product", "0010_auto_20221118_1907"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
