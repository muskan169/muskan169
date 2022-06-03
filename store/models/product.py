from django.conf import settings
from django.db import models
from django.urls import reverse

from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.CharField(max_length=200, default="", null=True, blank=True)
    image = models.ImageField(upload_to="upload/products/")
    users_wishlist = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="user_wishlist", blank=True
    )

    # @staticmethod
    # def get_all_products():
    #     return Product.objects.all()

    def get_absolute_url(self):
        return reverse("home")

    def __str__(self):
        return f"{self.name}"

    # @staticmethod
    # def get_all_products_by_categoryid(category_id):
    #     if category_id:
    #         return Product.objects.filter(category = category_id)
    #     else:
    #         return Product.get_all_products()
