# Generated by Django 3.0.8 on 2020-07-08 03:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("users", "0003_auto_20200708_1128")]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="main_user",
            field=models.BooleanField(default=False, verbose_name="Main User"),
        )
    ]
