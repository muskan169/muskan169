from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from api import views

app_name = "api"
# creating router object
router = DefaultRouter()

# REGISTER studentviewset with router
router.register("studenttapi", views.StudentViewSet, basename="student")
router.register("secured", views.StudentModelViewSet, basename="muskan")
router.register("studentTTapi", views.StudentReadOnlyModelViewSet, basename="students")
router.register(
    "orderlineapi", views.OrderlineReadOnlyModelViewSet, basename="orderline"
)
router.register("productlistapi", views.ProductlistView, basename="test")


urlpatterns = [
    path("productapi/", views.ProductAPI.as_view()),
    path("productapi/<int:pk>/", views.ProductAPI.as_view()),
    # path('productsearchapi/', views.ProductlistView.as_view(), name='productlist'),
    path("orderapi/<int:pk>/", views.OrderRetrieveUpdateDestroy.as_view()),
    path("addresslist/<int:pk>/", views.AddressList.as_view()),
    path("addresslist/<city>", views.AddressList.as_view()),
    path("addressapi/<int:pk>/", views.AddressRetrieveUpdate.as_view()),
    path("customerapi/<int:pk>/", views.CustomerListCreate.as_view()),
    path("customerrapi/<int:pk>/", views.CustomerRetrieveUpdateDestroy.as_view()),
    path("", include(router.urls)),
    path("gettoken/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("refreshtoken/", TokenRefreshView.as_view(), name="token_refresh"),
    path("verifytoken/", TokenVerifyView.as_view(), name="token_verify"),
]
