# from itertools import product
# from django.test import TestCase
# from django.urls import reverse
# from PIL import Image
# from platformdirs import user_cache_dir
# from rest_framework.test import APITestCase
# from django.contrib.auth.models import User
# from django.core.files.base import ContentFile
# from django.core.files.uploadedfile import SimpleUploadedFile




# from store.forms import AddressForm
# from store.models import Category, Order, Product
# from store.models.category import Category
# from store.models.product import Product
# import io

# # Create your tests here.
# def create_image(
#     storage, filename, size=(100, 100), image_mode="RGB", image_format="PNG"
# ):
#     data = io.BytesIO()
#     Image.new(image_mode, size).save(data, image_format)
#     data.seek(0)
#     if not storage:
#         return data
#     image_file = ContentFile(data.read())
#     return storage.save(filename, image_file)

# class Test_Addtocart(TestCase):
#    def setUp(self):
#         myimage = create_image(None, "fake.png")
#         self.avatar_file = SimpleUploadedFile("front.png", myimage.getvalue())
#         self.category = Category.objects.create(name="Mobiles")
#         self.user = User.objects.create_user(
#             username="shubham", password="shubham-yadav"
#         )
#         self.product = Product.objects.create(
#             name="apple",
#             price=15000,
#             description="apple is good",
#             category=self.category,
#             image=self.avatar_file,
#         )

#    def test_item_clear(self):
#         self.user.login(email="m@gmail.com", password="12345")
#         response = self.client.post(
#             reverse('customer:item_clear', {"id": self.product.id}}
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/customer/cart-detail/')

#     def test_cart_clear(self):
#         response = self.client.post(reverse('customer:cart_clear'))
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, "/customer/cart-detail/")
    
#     def test_item_increment(self):
#         # self.client.login(email="m@gmail.com", password="12345")
#         response = self.client.post(
#             reverse('customer:item_increment', kwargs={'id': self.product.id}))
#         # print(tst cases chre hai)

#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/customer/cart-detail/')

#      def test_item_decrement(self):
#         # self.client.login(email="m@gmail.com", password="12345")
#         response = self.client.post(
#             reverse('customer:item_increment', kwargs={'id': self.product.id}))
#         response = self.client.post(
#             reverse('customer:item_decrement', kwargs={'id': self.product.id}))
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, '/customer/cart-detail/')