from django.contrib import admin

from .models.address import Address
from .models.category import Category
from .models.customer import Customer
from .models.order import Order
from .models.orderline import OrderLine
from .models.product import Product

# class AdminProduct(admin.ModelAdmin):
#     list_display = ['name','price','category']


# class AdminCategory(admin.ModelAdmin):
#     list_display = ['name',]


# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Address)
admin.site.register(OrderLine)
