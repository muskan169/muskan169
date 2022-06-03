from django.contrib.auth.models import User
from django.db import models


class Address(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=20, default="")
    state = models.CharField(max_length=20, default="")
    zip_code = models.IntegerField()

    def __str__(self):
        return f"{self.user}"
