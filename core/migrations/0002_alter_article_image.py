# Generated by Django 4.2.2 on 2023-06-16 17:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="image",
            field=models.ImageField(upload_to="articles", verbose_name="Imagen"),
        ),
    ]
