# Generated by Django 4.0.3 on 2022-04-08 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0010_remove_order_customer_order_user_delete_customer"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="quantity",
        ),
    ]
