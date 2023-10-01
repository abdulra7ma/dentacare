# Generated by Django 4.2.5 on 2023-10-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("health", "0005_category_blog"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactMessage",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("subject", models.CharField(max_length=15)),
                ("message", models.TextField()),
            ],
        ),
    ]