# Generated by Django 3.0.8 on 2020-07-08 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("users", "0005_auto_20200708_1208")]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="main_user",
            field=models.BooleanField(default=False, verbose_name="Main User"),
        ),
        migrations.AlterField(
            model_name="customuser",
            name="public_email",
            field=models.CharField(blank=True, max_length=255, verbose_name="Email"),
        ),
    ]
