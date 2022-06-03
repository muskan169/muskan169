from warnings import filters

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.filters import SearchFilter
from rest_framework.generics import (ListAPIView, ListCreateAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveUpdateDestroyAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ReadOnlyModelViewSet

from store.models.address import Address
from store.models.customer import Customer
from store.models.order import Order
from store.models.orderline import OrderLine
from store.models.product import Product

from .models import Student
from .serializers import (AddressSerializer, CustomerSerializer,
                          OrderlineSerializer, OrderSerializer,
                          ProductSerializer, StudentSerializer)

# model object - single Product data
# def Product_detail(request, pk):
#  stu = Product.objects.get(id = pk)
#  serializer = ProductSerializer(stu)
#  json_data = JSONRenderer().render(serializer.data)
#  return HttpResponse(json_data, content_type='application/json')


#  #query set - all Products data
# def Product_list(request):
#   stu = Product.objects.all()
#   serializer = ProductSerializer(stu, many = True)
#   json_data = JSONRenderer().render(serializer.data)
#   return HttpResponse(json_data, content_type='application/json')


# creatre class based API


class ProductAPI(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            Prds = Product.objects.get(id=id)
            serializer = ProductSerializer(stu)
            return Response(serializer.data)

        stu = Product.objects.all()
        serializer = ProductSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data Created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def put(self, reuqest, pk, format=None):
        id = pk
        stu = Product.objects.get(pk=id)
        serializer = ProductSerializer(stu, data=reuqest.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "complete Data Updated"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id = pk
        stu = Product.objects.get(pk=id)
        serializer = ProductSerializer(stu, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "partial data updated"})
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        id = pk
        stu = Product.objects.get(pk=id)
        stu.delete()
        return Response({"msg": "data deleted"})

        # create order api


class OrderRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # create address api for update and listing.


class AddressRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


# crate orderline READONLYVIEWSET


class OrderlineReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = OrderLine.objects.all()
    serializer_class = OrderlineSerializer


# create listCreateApiview for customer model and try to replace queryset from (model = customer)


class CustomerListCreate(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    # model = Customer


# create another API for updating and deleting customer.
class CustomerRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


# apply filter
class AddressList(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    city = ""

    def get_queryset(self):
        self.city = self.kwargs["city"]
        return Address.objects.filter(city=self.city)


# apply search filter
class ProductlistView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # filter_backends =[SearchFilter]
    # search_fields = ['name',]


# create viewset for student


class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "data created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # create ModelViewSet


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


# create ReadOnlyModelViewSet


class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
