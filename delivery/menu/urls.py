from django.urls import path
from django.views.decorators.cache import cache_page

from .view_rest import ItemView, ProductsFromCategoryView, CategoriesView

urlpatterns = [
    path('menu/<pk>/', cache_page(3600 * 12)(ItemView.as_view({'get': 'retrieve'})), name='product'),
    path('category/<pk>/', cache_page(3600 * 12)(ProductsFromCategoryView.as_view({'get': 'list'})), name='category'),
    path('categories/', cache_page(3600 * 12)(CategoriesView.as_view({'get': 'list'}))),
]