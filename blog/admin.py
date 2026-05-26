from django.contrib import admin
from .models import BlogCategory, BlogPost, Recipe

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'is_featured', 'published_at')
    list_filter = ('category', 'is_featured', 'published_at')
    search_fields = ('title', 'excerpt', 'content')
    prepopulated_fields = {'slug': ('name',)} # Let's prepopulate from title instead of name
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('-published_at',)

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title', 'age_group', 'difficulty', 'prep_time', 'cook_time', 'is_featured', 'published_at')
    list_filter = ('age_group', 'difficulty', 'is_featured', 'published_at')
    search_fields = ('title', 'ingredients_list', 'instructions')
    prepopulated_fields = {'slug': ('title',)}
    filter_horizontal = ('related_products',)
    ordering = ('-published_at',)
