from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import BlogPost, BlogCategory, Recipe
from products.models import AgeGroup

class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog/blog_list.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        queryset = BlogPost.objects.all().order_by('-published_at')

        # Filter by blog category slug
        category_slug = self.kwargs.get('category_slug') or self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = BlogCategory.objects.all()
        context['active_category'] = self.kwargs.get('category_slug') or self.request.GET.get('category', '')

        if context['active_category']:
            try:
                context['page_title'] = BlogCategory.objects.get(slug=context['active_category']).name
            except BlogCategory.DoesNotExist:
                context['page_title'] = "Blog"
        else:
            context['page_title'] = "Highness Blog"

        # Add featured posts (excluding current list if needed or just featured)
        context['featured_posts'] = BlogPost.objects.filter(is_featured=True).order_by('-published_at')[:3]
        return context

class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'blog/blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()

        # Related posts (same category, exclude current, limit 3)
        context['related_posts'] = BlogPost.objects.filter(
            category=post.category
        ).exclude(id=post.id).order_by('-published_at')[:3]

        return context

class RecipeListView(ListView):
    model = Recipe
    template_name = 'blog/recipe_list.html'
    context_object_name = 'recipes'
    paginate_by = 8

    def get_queryset(self):
        queryset = Recipe.objects.all().order_by('-published_at')

        # Filter by age group slug
        age_slug = self.kwargs.get('age_slug') or self.request.GET.get('age')
        if age_slug:
            queryset = queryset.filter(age_group__slug=age_slug)

        # Filter by difficulty
        difficulty = self.request.GET.get('difficulty')
        if difficulty in ['easy', 'medium', 'hard']:
            queryset = queryset.filter(difficulty=difficulty)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['age_groups'] = AgeGroup.objects.all().order_by('order')
        context['active_age'] = self.kwargs.get('age_slug') or self.request.GET.get('age', '')
        context['active_difficulty'] = self.request.GET.get('difficulty', '')
        context['difficulties'] = Recipe.DIFFICULTY_CHOICES

        if context['active_age']:
            try:
                context['page_title'] = f"Recipes for {AgeGroup.objects.get(slug=context['active_age']).name}"
            except AgeGroup.DoesNotExist:
                context['page_title'] = "Healthy Recipes"
        else:
            context['page_title'] = "Healthy Kids Recipes"

        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'blog/recipe_detail.html'
    context_object_name = 'recipe'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        recipe = self.get_object()

        # Related products (M2M relation in model)
        context['related_products'] = recipe.related_products.filter(is_active=True).prefetch_related('images')[:4]

        # Other recent recipes (excluding current, limit 3)
        context['recent_recipes'] = Recipe.objects.exclude(id=recipe.id).order_by('-published_at')[:3]

        return context
