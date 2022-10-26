from rest_framework import serializers

from menu import models

class PriceSerializers(serializers.ModelSerializer):
    price = serializers.FloatField()
    class Meta:
        model = models.Price
        fields = '__all__'

class ProductsSerializers(serializers.ModelSerializer):
    price = PriceSerializers(many=True)
    class Meta:
        model = models.Products
        fields = '__all__'
        # depth = 2
    
    

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = models.Categories
        fields = '__all__'
