from django.urls import path

from .view_rest import ItemView, ProductsFromCategoryView, CategoriesView

urlpatterns = [
    path('menu/<pk>/', ItemView.as_view({'get': 'retrieve'}), name='product'),
    path('category/<pk>/', ProductsFromCategoryView.as_view({'get': 'list'}), name='category'),
    path('categories/', CategoriesView.as_view({'get': 'list'})),
]