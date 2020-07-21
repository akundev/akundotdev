# Generated by Django 3.0.8 on 2020-07-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [("articles", "0003_auto_20200717_1302")]

    operations = [
        migrations.CreateModel(
            name="Tool",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=150, verbose_name="Tool")),
                ("slug", models.SlugField(unique=True, verbose_name="Slug")),
                (
                    "description",
                    models.CharField(max_length=280, verbose_name="Description"),
                ),
                (
                    "img_link",
                    models.CharField(max_length=255, verbose_name="Image url"),
                ),
                (
                    "link",
                    models.CharField(max_length=255, verbose_name="Url of the tool"),
                ),
                (
                    "tags",
                    models.ManyToManyField(to="articles.Tag", verbose_name="Tags"),
                ),
            ],
            options={"verbose_name": "Tool", "verbose_name_plural": "Tools"},
        )
    ]
