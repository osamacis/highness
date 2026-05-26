from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('products/', views.ProductListView.as_view(), name='product_list'),
    path('products/category/<slug:category_slug>/', views.ProductListView.as_view(), name='product_list_by_category'),
    path('products/age/<slug:age_slug>/', views.ProductListView.as_view(), name='product_list_by_age'),
    path('products/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('categories/', views.CategoryListView.as_view(), name='category_list'),
]
