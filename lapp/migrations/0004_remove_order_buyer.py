# Generated by Django 5.0.6 on 2024-05-21 06:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("lapp", "0003_rename_placed_by_order_buyer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="buyer",
        ),
    ]
