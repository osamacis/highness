from django import template

register = template.Library()

@register.filter
def currency_inr(value):
    """
    Format a decimal value to INR price string.
    """
    try:
        return f"₹{float(value):.2f}".rstrip('0').rstrip('.')
    except (ValueError, TypeError):
        return f"₹{value}"

@register.filter
def star_range(rating):
    """
    Convert a rating (e.g. 4.5) to a list of star states: ['full', 'full', 'full', 'full', 'half']
    """
    try:
        rating = float(rating)
    except (ValueError, TypeError):
        rating = 0.0
    
    stars = []
    for i in range(1, 6):
        if rating >= i:
            stars.append('full')
        elif rating >= i - 0.5:
            stars.append('half')
        else:
            stars.append('empty')
    return stars

@register.filter
def split_lines(value):
    """
    Split a string by newline.
    """
    if not value:
        return []
    return [line.strip() for line in value.split('\n') if line.strip()]
