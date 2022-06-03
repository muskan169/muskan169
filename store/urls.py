from itertools import product

from django.urls import path

from . import views
from .views import (
    OrderDetailView,
    ProductCreate,
    ProductDeleteView,
    ProductUpdateView,
    detail_view,
    index,
    login,
    signup,
)

# from .views import Checkout

urlpatterns = [
    path("list/", views.List.as_view()),
    path("detail/<pk>/", OrderDetailView.as_view()),
    path("forms/", ProductCreate.as_view()),
    path("update/<pk>/", ProductUpdateView.as_view()),
    path("delete/<pk>/", ProductDeleteView.as_view()),
    path("", index, name="home"),
    path("detail/<id>", detail_view),
    path("signup", signup),
    path("login", login),
    path("allorders/", views.order, name="allorders"),
    path("cart/add/<int:id>/", views.cart_add, name="cart_add"),
    #     path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    path("cart/item_increment/<int:id>/", views.item_increment, name="item_increment"),
    path("cart/item_decrement/<int:id>/", views.item_decrement, name="item_decrement"),
    path("cart/cart_clear/", views.cart_clear, name="cart_clear"),
    path("cart/cart-detail/", views.cart_detail, name="cart_detail"),
    # path('checkout/' , Checkout.as_view(), name='checkout'),
    path("payment/", views.PaymentView.as_view(), name="payment"),
    path("handlerequest/", views.handlerequest, name="handlerequest"),
    path("search_product/", views.SearchProductView.as_view(), name="search_product"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path(
        "wishlist/add_to_wishlist/<int:id>", views.add_to_wishlist, name="user_wishlist"
    ),
]
# razorpay
