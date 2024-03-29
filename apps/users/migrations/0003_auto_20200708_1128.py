# Generated by Django 3.0.8 on 2020-07-08 02:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("users", "0002_customuser_photo")]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="cv_link",
            field=models.CharField(
                blank=True, max_length=255, verbose_name="Resume (CV)"
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="github_link",
            field=models.CharField(blank=True, max_length=255, verbose_name="Github"),
        ),
        migrations.AddField(
            model_name="customuser",
            name="linkedin_link",
            field=models.CharField(blank=True, max_length=255, verbose_name="LinkedIn"),
        ),
        migrations.AddField(
            model_name="customuser",
            name="main_user",
            field=models.BooleanField(
                default=False, unique=True, verbose_name="Main User"
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="public_email",
            field=models.CharField(blank=True, max_length=255, verbose_name="Email"),
        ),
    ]
