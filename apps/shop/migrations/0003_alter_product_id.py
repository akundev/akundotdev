# Generated by Django 4.1.1 on 2022-09-07 07:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0002_auto_20200727_1759"),
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
