from rest_framework import serializers
from . import models
from decimal import Decimal


class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)


class ProductSerializer(serializers.Serializer):
    # class Meta:
    #     model = models.Product
    #     fields = ['name','description','price','inventory','category']

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    inventory = serializers.IntegerField()
    category = serializers.StringRelatedField()
    price_with_tax = serializers.SerializerMethodField('taxed_price')

    def taxed_price(self, product):
        return product.price + (product.price * Decimal(0.13))
