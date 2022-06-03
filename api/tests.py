import io
from email.mime import image
from http.client import responses
from unicodedata import category

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from PIL import Image
from rest_framework.test import APITestCase

from store.forms import AddressForm
from store.models import Category, Order, Product
from store.models.category import Category
from store.models.product import Product

# test cases for productlistapi crud operation.

print("muskan ke test case chale")


def create_image(
    storage, filename, size=(100, 100), image_mode="RGB", image_format="PNG"
):
    data = io.BytesIO()
    Image.new(image_mode, size).save(data, image_format)
    data.seek(0)
    if not storage:
        return data
    image_file = ContentFile(data.read())
    return storage.save(filename, image_file)


class TestProductCase(TestCase):
    def setUp(self):
        myimage = create_image(None, "fake.png")
        self.avatar_file = SimpleUploadedFile("front.png", myimage.getvalue())
        self.category = Category.objects.create(name="Mobiles")
        self.user = User.objects.create_user(
            username="shubham", password="shubham-yadav"
        )
        self.product = Product.objects.create(
            name="apple",
            price=15000,
            description="apple is good",
            category=self.category,
            image=self.avatar_file,
        )
        self.product.users_wishlist.set([self.user.pk])

    def test_product_get(self):
        response = self.client.get(reverse("api:test-list"))
        print("response", response.data)
        self.assertEqual(response.status_code, 200)

    def test_product_post(self):
        data = {
            "name": "Red shirt",
            "price": 5490,
            "category": 1,
        }
        response = self.client.post(
            reverse("api:test-list"), data, files=self.avatar_file, format="json"
        )
        print("response", response.data)
        self.assertEqual(response.status_code, 201)

    # def test_product_patch(self):
    #     data = {
    #         "name": "Red shirt"
    #     }
    #     response = self.client.patch(
    #         reverse('api:test-detail', kwargs={'pk':self.product.pk}), data, files=self.avatar_file, format="json")
    #     #print('response', response.data)
    #     self.assertEqual(response.status_code, 200)

    # def test_product_put(self):
    #     data = {
    #         "name": "red shirt",
    #         "price": 549,
    #     }
    #     response = self.client.put(
    #         reverse('api:test-detail', kwargs={'pk':self.product.pk}), data, files=self.avatar_file, format="json")
    #     # print('response', response.data)
    #     response_data = json.loads(response.content)

    #     self.assertEqual(response.status_code, 200)

    def test_product_delete(self):
        response = self.client.delete(
            reverse("api:test-detail", kwargs={"pk": self.product.pk}),
            files=self.avatar_file,
            format="json",
        )
        self.assertEqual(response.status_code, 204)

    # test cases for models


class ProductModelTest(TestCase):
    @classmethod
    def setUp(self):
        self.user = User.objects.create_user(
            username="shubham", password="shubham-yadav"
        )
        self.c = Category.objects.create(name="vegetables")
        self.p = Product.objects.create(
            name="tomato", category=self.c, image="try.jpg", price=23
        )

    def test_category_label(self):
        field_label = Product._meta.get_field("category").verbose_name
        self.assertEqual(field_label, "category")

    def test_name_label(self):
        field_label = Product._meta.get_field("name").verbose_name
        self.assertEqual(field_label, "name")

    def test_description_null_eq_true(self):
        nullvalue = Product._meta.get_field("description").null
        self.assertTrue(nullvalue)

    def test_string_representaion(self):
        self.assertEqual(str(self.p), self.p.name)

    # test cases for address form.


" Tests for AddressForm"


class AddressFormTest(
    TestCase,
):
    def setUp(self):
        self.user = User.objects.create_user(
            username="shubham", password="shubham-yadav"
        )

    # def test_product_form_category_field_label(self):
    #     form = AddressForm()
    #     self.assertTrue(form.fields['zip_code'].label == 'zip_code')

    # Tests for mobile field validation
    def test_address_form_with_zip_code_gt_10_digit(self):
        form = AddressForm(
            data={
                "user": 1,
                "address": "Indore",
                "city": "Indore",
                "state": "MP",
                "zip_code": 111111,
            }
        )
        self.assertFalse(form.is_valid())

    def test_address_form_with_zip_code_gt_10_digit(self):
        form = AddressForm(
            data={
                "user": 1111,
                "address": "Indore",
                "city": "Indore",
                "state": "MP",
                "zip_code": 111111,
            }
        )
        self.assertTrue(form.is_valid())

    def test_address_form_with_valid_zip_code(self):
        form = AddressForm(
            data={
                "user": self.user,
                "address": "Indore",
                "city": "Indore",
                "state": "MP",
                "zip_code": 111111,
            }
        )
        self.assertTrue(form.is_valid())


# test for add to cart func.
class Test_Addtocart(TestCase):
    def setUp(self):
        #     self.user = User.objects.create_user(
        #                 username="shubham", password="shubham-yadav")
        self.c = Category.objects.create(name="vegetables")
        myimage = create_image(None, "fake.png")
        self.avatar_file = SimpleUploadedFile("front.png", myimage.getvalue())
        self.p = Product.objects.create(
            id=1, name="tomato", category=self.c, image="try.jpg", price=23
        )

    def test_product_post(self):
        data = {
            "name": "Red shirt",
            "price": 5490,
            "category": 1,
        }
        response = self.client.post(
            reverse("api:test-list"), data, files=self.avatar_file, format="json"
        )
        print("response add to cart", response.data)
        self.assertEqual(response.status_code, 201)

    def test_product_get(self):
        response = self.client.get(reverse("api:test-list"))
        # import pdb;pdb.set_trace()
        print("get add to cart response", response.data)
        self.assertEqual(response.status_code, 200)

    def test_cart_add(self):
        self.client.login(email="jenny@gmail.com", password="12345")
        response = self.client.get(f"/cart/add/1/")
        kwargs = {"id": self.p.id}
        print("muskan k kwargs", kwargs)
        self.assertEqual(response.status_code, 302)
