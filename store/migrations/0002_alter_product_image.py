# Generated by Django 4.0.3 on 2022-03-25 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("store", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(upload_to="upload/products/"),
        ),
    ]
