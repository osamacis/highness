from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('blog/', views.BlogListView.as_view(), name='blog_list'),
    path('blog/category/<slug:category_slug>/', views.BlogListView.as_view(), name='blog_list_by_category'),
    path('blog/<slug:slug>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('recipes/', views.RecipeListView.as_view(), name='recipe_list'),
    path('recipes/age/<slug:age_slug>/', views.RecipeListView.as_view(), name='recipe_list_by_age'),
    path('recipes/<slug:slug>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]
