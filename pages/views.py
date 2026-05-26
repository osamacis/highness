from django.views.generic import TemplateView, FormView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Banner, Testimonial, USP, TeamMember, FAQ
from .forms import ContactForm
from products.models import Product, Category, AgeGroup
from blog.models import BlogPost, Recipe

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Banners
        context['banners'] = Banner.objects.filter(is_active=True).order_by('order')
        
        # 2. Category Icon Strip (top level only)
        context['categories'] = Category.objects.filter(parent=None).order_by('order', 'name')
        
        # 3. Age Groups
        context['age_groups'] = AgeGroup.objects.all().order_by('order')
        
        # 4. Featured products (is_featured=True, limit 8)
        context['featured_products'] = Product.objects.filter(
            is_active=True, 
            is_featured=True
        ).prefetch_related('images')[:8]
        
        # 5. Bestsellers (is_bestseller=True, limit 8)
        context['bestselling_products'] = Product.objects.filter(
            is_active=True, 
            is_bestseller=True
        ).prefetch_related('images')[:8]
        
        # 6. Testimonials
        context['testimonials'] = Testimonial.objects.filter(is_featured=True).order_by('-created_at')[:6]
        
        # 7. USPs
        context['usps'] = USP.objects.all().order_by('order')
        
        # 8. Blog posts for homepage (limit 3)
        context['recent_posts'] = BlogPost.objects.filter(is_featured=True).order_by('-published_at')[:3]
        if not context['recent_posts'].exists():
            context['recent_posts'] = BlogPost.objects.all().order_by('-published_at')[:3]
            
        return context

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['team_members'] = TeamMember.objects.all().order_by('order')
        context['usps'] = USP.objects.all().order_by('order')
        return context

class ContactPageView(FormView):
    template_name = 'pages/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('pages:contact')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['faqs'] = FAQ.objects.all().order_by('order')
        return context

    def form_valid(self, form):
        # Save inquiry
        form.save()
        messages.success(self.request, "Thank you for reaching out! We will get back to you shortly.")
        return super().form_valid(form)
