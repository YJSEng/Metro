# Generated by Django 4.1.1 on 2023-06-13 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Member",
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
                ("firstname", models.CharField(max_length=9)),
                ("lastname", models.CharField(max_length=20)),
                ("card", models.CharField(default="Yes", max_length=3)),
                ("topup", models.IntegerField(null=True)),
                (
                    "adharnumber",
                    models.CharField(
                        error_messages={"unique": "The Adhar Number exits."},
                        max_length=12,
                        unique=True,
                    ),
                ),
            ],
        ),
    ]
