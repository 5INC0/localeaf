# Generated by Django 5.0.1 on 2024-05-21 06:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lapp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("placed_by", models.CharField(max_length=300)),
                ("supplier", models.CharField(max_length=300)),
                ("item", models.CharField(max_length=300)),
                ("quantity", models.IntegerField()),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("location", models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("item", models.CharField(max_length=300)),
                ("quantity", models.IntegerField()),
                ("stock_added_on", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]