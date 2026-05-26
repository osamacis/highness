from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Product, Category, AgeGroup

class CategoryListView(ListView):
    model = Category
    template_name = 'products/category_list.html'
    context_object_name = 'categories'
    
    def get_queryset(self):
        return Category.objects.filter(parent=None).order_by('order', 'name')

class ProductListView(ListView):
    model = Product
    template_name = 'products/product_list.html'
    context_object_name = 'products'
    paginate_by = 12

    def get_queryset(self):
        queryset = Product.objects.filter(is_active=True).prefetch_related('images', 'age_groups')
        
        # Filter by category slug (either from URL kwargs or query params)
        category_slug = self.kwargs.get('category_slug') or self.request.GET.get('category')
        if category_slug:
            queryset = queryset.filter(Q(category__slug=category_slug) | Q(category__parent__slug=category_slug))
            
        # Filter by age group slug
        age_slug = self.kwargs.get('age_slug') or self.request.GET.get('age')
        if age_slug:
            queryset = queryset.filter(age_groups__slug=age_slug)
            
        # Search query
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | 
                Q(short_description__icontains=search_query) |
                Q(description__icontains=search_query)
            )

        # Sorting
        sort_by = self.request.GET.get('sort', 'default')
        if sort_by == 'price_low_high':
            queryset = queryset.order_by('selling_price')
        elif sort_by == 'price_high_low':
            queryset = queryset.order_by('-selling_price')
        elif sort_by == 'bestselling':
            queryset = queryset.order_by('-is_bestseller', '-rating')
        elif sort_by == 'newest':
            queryset = queryset.order_by('-created_at')
        else:
            queryset = queryset.order_by('category__order', 'id')
            
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Add filtering choices to context
        context['categories'] = Category.objects.filter(parent=None).order_by('order', 'name')
        context['age_groups'] = AgeGroup.objects.all().order_by('order')
        
        # Pass active filters to retain in pagination
        context['active_category'] = self.kwargs.get('category_slug') or self.request.GET.get('category', '')
        context['active_age'] = self.kwargs.get('age_slug') or self.request.GET.get('age', '')
        context['active_sort'] = self.request.GET.get('sort', 'default')
        context['search_query'] = self.request.GET.get('q', '')
        
        # Page title customization
        if context['active_category']:
            try:
                context['page_title'] = Category.objects.get(slug=context['active_category']).name
            except Category.DoesNotExist:
                context['page_title'] = "Products"
        elif context['active_age']:
            try:
                context['page_title'] = f"Shop for {AgeGroup.objects.get(slug=context['active_age']).name}"
            except AgeGroup.DoesNotExist:
                context['page_title'] = "Products"
        elif context['search_query']:
            context['page_title'] = f"Search Results for '{context['search_query']}'"
        else:
            context['page_title'] = "All Products"
            
        return context

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product_detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        return Product.objects.filter(is_active=True).prefetch_related('images', 'age_groups')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = self.get_object()
        
        # Main primary image & other images
        context['primary_image'] = product.images.filter(is_primary=True).first() or product.images.first()
        context['gallery_images'] = product.images.all().order_by('order')
        
        # Related products (same category, excluding current product, limit to 4)
        context['related_products'] = Product.objects.filter(
            category=product.category, 
            is_active=True
        ).exclude(id=product.id)[:4]
        
        # Add reviews/testimonials associated with this product
        context['product_testimonials'] = product.testimonials.filter(is_featured=True).order_by('-created_at')
        
        return context
