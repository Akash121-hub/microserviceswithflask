from .producer import publish
from ast import Pass
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.views import APIView

from .serializers import ProductSerializer
from rest_framework.response import Response
from .models import Product, User
import random

# Create your views here.

class ProductViewSet(viewsets.ViewSet):
    def list(self,request):
        products_obj = Product.objects.all()
        serializer = ProductSerializer(products_obj,many=True)
        publish()
        return Response(serializer.data)

    

    def create(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()    
        return Response(serializer.data,status=status.HTTP_201_CREATED)

    def retrieve(self,request,pk=None):
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(products)  
        return Response(serializer.data)

    def update(self,request,pk=None):
        products = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=products,data=request.data)  
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self,request,pk=None):
        pass
        products = Product.objects.get(id=pk)       
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserApiView(APIView):
    def get(self,_):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id':user.id
        })

