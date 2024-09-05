# Generated by Django 5.1 on 2024-09-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="manufactured_at",
            field=models.DateTimeField(
                blank=True, null=True, verbose_name="Дата производства продукта"
            ),
        ),
    ]