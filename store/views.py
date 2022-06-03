import datetime
from itertools import product

import pytz
import razorpay
from cart.cart import Cart
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from store.models.wishlist import Wishlist, wishlist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from Eshop import settings
from store.forms import AddressForm
from store.models import customer, orderline
from store.models.category import Category
from store.models.order import Order

# from store.models.customer import Customer
from store.models.orderline import OrderLine
from store.models.product import Product

from .models.product import Product

IST = pytz.timezone("Asia/Kolkata")

# <!class based views

# try to create list view of product model here
class List(ListView):
    model = Product
    context_object_name = "products"
    template_name = "store/list.html"

    # creating detail view of order model


class OrderDetailView(DetailView):
    model = Order
    template_name = "store/detailview.html"

    # creating create view


class ProductCreate(CreateView):
    model = Product
    fields = "__all__"
    template_name = "store/forms.html"
    success_url = ""

    # creating update view


class ProductUpdateView(UpdateView):
    model = Product
    fields = ["price", "description"]
    template_name = "store/update.html"
    success_url = ""


# create delete view
class ProductDeleteView(DeleteView):
    model = Product
    field = ["description"]
    success_url = "/"
    template_name = "store/deleteview.html"

    # create searchproduct func


class SearchProductView(ListView):
    model = Product
    template_name = "index.html"
    context_object_name = "products"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return self.model.objects.filter(name__icontains=query)


# Create your views here.
def index(request):
    prds = Product.objects.all()
    categories = Category.get_all_categories()
    categoryID = request.GET.get("category")
    if categoryID:
        prds = prds.filter(category=categoryID)
    data = {}
    data["products"] = prds
    data["categories"] = categories
    paginator = Paginator(prds, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data["products"] = page_obj
    return render(request, "index.html", data)


# create detail view
def detail_view(request, id):
    context = {}
    context["data"] = Product.objects.get(id=id)
    return render(request, "detail_view.html", context)


# signup function in class based views
class Signup(View):
    def get(self, request):
        return render(request, "signup.html")


def signup(request):
    return render(request, "signup.html")


# myorders detail page

# def order(request):
#     return render(request , 'store/myorders.html')


def order(request):
    orders = Order.objects.filter(user=request.user)  # filter user
    result = {}  # blank context
    for order in orders:
        orderlines = OrderLine.objects.filter(order=order)
        result[order] = orderlines
    print("resultssss", result)
    return render(request, "store/myorders.html", {"result": result})

    # create login function.


def login(request):
    if request.method == "GET":
        return render(request, "index.html")

    else:
        email = request.POST.get("email")
        password = request.POST.get("password")
        # customer = Customer.get_customer_by_email(email)
        print(customer)
        print(email, password)
        return render(request, "index.html")

    # add to cart func.


# @login_required(login_url=reverse("account_login"))
def cart_add(request, id):
    print("add to cart", request)
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("home")


@login_required(login_url="/users/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail.html")


@login_required(login_url="/users/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/users/login")
def cart_detail(request):
    form = AddressForm()
    return render(request, "store/cart_detail.html", {"form": form})


#     #checkout function

# class Checkout(View):
#     def post(self , request):
#         print("fesfdresfesrf")
#         print(request.POST)
#         return('cart_detail')

# razorpay

client = razorpay.Client(auth=(settings.razorpay_id, settings.razorpay_account_id))


class PaymentView(View):
    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            form.instance.user = self.request.user
            form.save()
        address = form.instance

        cart = Cart(request)
        user = request.user
        print("hhhhhhhhhhhhhhhhhhhhh", user)
        today = datetime.datetime.now(IST)
        final_price = 0
        order = Order.objects.create(user=user, date=today, price=final_price)
        all_orderlines = []
        for product in cart.cart.values():
            quantity = int(product.get("quantity"))
            price = int(product.get("price"))
            product = int(product.get("product_id"))

            all_orderlines.append(
                OrderLine(user=user, order=order, product_id=product, quantity=quantity)
            )
            final_price += price * quantity
        orderline = OrderLine.objects.bulk_create(all_orderlines)

        order.price = final_price

        # http://127.0.0.1:8000//handlerequest/

        callback_url = "http://127.0.0.1:8000" + "/handlerequest/"
        razorpay_order = client.order.create(
            dict(
                amount=final_price * 100,
                currency=settings.order_currency,
                payment_capture="1",
            )
        )

        order.order_id = razorpay_order["id"]
        order.save()
        cart.clear()
        orderlines = OrderLine.objects.filter(order=order)
        context = {
            "order": order,
            "order_id": razorpay_order["id"],
            "final_price": final_price,
            "razorpay_merchant_id": settings.razorpay_id,
            "callback_url": callback_url,
            "orderlines": orderlines,
            "address": address,
        }
        return render(request, "store/pay.html", context)


# request handling


@csrf_exempt
def handlerequest(request):
    if request.method == "POST":
        payment_id = request.POST.get("razorpay_payment_id", "")
        order_id = request.POST.get("razorpay_order_id", "")
        signature = request.POST.get("razorpay_signature", "")

        params_dict = {
            "razorpay_payment_id": payment_id,
            "razorpay_order_id": order_id,
            "razorpay_signature": signature,
        }

        order_db = Order.objects.get(order_id=order_id)
        try:
            check = client.utility.verify_payment_signature(params_dict)
            order_db.status = True
            order_db.save()
            return render(request, "store/success.html")

        except:
            order_db.status = False
            order_db.save()
            return render(request, "store/failed.html")


# wishlist func.


@login_required(login_url="/accounts/login")
def wishlist(request):
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, "store/user_wish_list.html", {"wishlist": products})


@login_required(login_url="/accounts/login")
def add_to_wishlist(request, id):
    product = get_object_or_404(Product, id=id)
    if product.users_wishlist.filter(id=request.user.id).exists():
        product.users_wishlist.remove(request.user)
    else:
        product.users_wishlist.add(request.user)
    return HttpResponseRedirect(request.META["HTTP_REFERER"])
