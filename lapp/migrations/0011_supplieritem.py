# Generated by Django 5.0.6 on 2024-05-22 06:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lapp", "0010_orderhistory_buyer"),
    ]

    operations = [
        migrations.CreateModel(
            name="SupplierItem",
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
                ("name", models.CharField(max_length=300)),
                ("status", models.CharField(max_length=300)),
                ("description", models.CharField(max_length=1000)),
                ("supplier", models.CharField(max_length=300)),
            ],
        ),
    ]
