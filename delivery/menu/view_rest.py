from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAdminUser

from menu import models
from menu import serializers

class ItemView(viewsets.mixins.RetrieveModelMixin,
                   viewsets.GenericViewSet):
    queryset = models.Products.objects.filter(aviable=True)
    serializer_class = serializers.ProductsSerializers
    
    
class ProductsFromCategoryView(viewsets.mixins.ListModelMixin, 
                               viewsets.GenericViewSet):
    serializer_class = serializers.ProductsSerializers
    def get_queryset(self, slug=None):
        return models.Products.objects.filter(aviable=True, category=self.kwargs['pk'])


class CategoriesView(viewsets.mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = serializers.CategorySerializers
    queryset = models.Categories.objects.all()
    
