# from .customer import Customer
import datetime

from django.contrib.auth.models import User
from django.db import models

from .product import Product


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    price = models.IntegerField()
    phone = models.CharField(max_length=50, blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)
    order_id = models.CharField(max_length=50, blank=True, null=True)
    payment_id = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.id}"
