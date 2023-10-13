# Generated by Django 3.0.8 on 2020-07-17 01:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("articles", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="source_link",
            field=models.CharField(
                default="https://akun.dev/", max_length=255, verbose_name="Sources url"
            ),
            preserve_default=False,
        )
    ]
