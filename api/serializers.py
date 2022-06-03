from rest_framework import serializers

from store.models.address import Address
from store.models.customer import Customer
from store.models.order import Order
from store.models.orderline import OrderLine
from store.models.product import Product

from .models import Student


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name", "price", "category", "description"]


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ["phone", "date", "status", "user"]


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ["zip_code", "city", "address", "mobile", "user"]


class OrderlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderLine
        fields = ["order", "user", "product", "quantity"]


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone", "email"]

    # create new model serializer for student model.


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ["id", "name", "roll", "city"]
