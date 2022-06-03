# Generated by Django 4.0.3 on 2022-04-08 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0012_remove_order_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="order_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="order",
            name="payment_id",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
