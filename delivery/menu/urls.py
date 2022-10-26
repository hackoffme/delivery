from django.urls import path

from .view_rest import ItemView, ProductsFromCategoryView, CategoriesView

urlpatterns = [
    # path('menu/', ProductsView.as_view({'get': 'list'})),
    path('menu/<pk>/', ItemView.as_view({'get': 'retrieve'})),
    path('category/<pk>/', ProductsFromCategoryView.as_view({'get': 'list'})),
    path('categories/', CategoriesView.as_view({'get': 'list'})),
]