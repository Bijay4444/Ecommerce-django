from django.shortcuts import render
from rest_framework.response import Response
from .models import Category, Product
from . import serializers
from . import models

from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def category_list(request):
    category = Category.objects.all()
    serializer = serializers.CategorySerializer(category, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    products = Product.objects.select_related('category').all()
    product_serializers = serializers.ProductSerializer(products, many=True)
    return Response(product_serializers.data)