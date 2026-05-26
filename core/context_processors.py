from products.models import Category, AgeGroup

def site_settings(request):
    """
    Global context processor for SlurrpFarm site settings and navigation database queries.
    """
    # Query categories and age groups for navigation
    # Use prefetch_related/select_related where appropriate or simple queryset
    # Filter only root categories for navigation menu
    nav_categories = Category.objects.filter(parent=None).order_by('order', 'name')
    nav_age_groups = AgeGroup.objects.all().order_by('order')

    return {
        'SITE_NAME': 'Highness',
        'SITE_TAGLINE': 'Made by 2 Mothers. 100% Honest, Healthy Millet Food for Kids.',
        'CONTACT_EMAIL': 'info@slurrpfarm.com',
        'CONTACT_PHONE': '+91 99999 99999',
        'CONTACT_ADDRESS': 'Highness HQ, New Delhi, India',
        'SOCIAL_LINKS': {
            'instagram': 'https://instagram.com/slurrpfarm',
            'facebook': 'https://facebook.com/slurrpfarm',
            'youtube': 'https://youtube.com/slurrpfarm',
            'twitter': 'https://twitter.com/slurrpfarm',
        },
        'NAV_CATEGORIES': nav_categories,
        'NAV_AGE_GROUPS': nav_age_groups,
    }
