# Generated by Django 4.2.5 on 2023-09-29 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Donation",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "verbose_name_plural": "Donations",
            },
        ),
    ]
