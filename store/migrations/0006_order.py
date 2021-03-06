# Generated by Django 2.2.12 on 2022-04-06 07:09

import datetime

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0005_auto_20220329_0926"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("quantity", models.IntegerField(default=1)),
                ("price", models.IntegerField()),
                ("address", models.CharField(blank=True, default="", max_length=50)),
                ("phone", models.CharField(blank=True, default="", max_length=50)),
                ("date", models.DateField(default=datetime.datetime.today)),
                ("status", models.BooleanField(default=False)),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.Customer"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="store.Product"
                    ),
                ),
            ],
        ),
    ]
