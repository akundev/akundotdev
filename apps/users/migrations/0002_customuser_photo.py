# Generated by Django 3.0.8 on 2020-07-07 08:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="photo",
            field=models.CharField(
                default="https://photo.com/photo.png",
                max_length=255,
                verbose_name="Photo",
            ),
            preserve_default=False,
        )
    ]
