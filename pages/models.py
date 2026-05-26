from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    image_desktop = models.ImageField(upload_to='banners/')
    image_mobile = models.ImageField(upload_to='banners/', blank=True)
    cta_text = models.CharField(max_length=50, blank=True)
    cta_link = models.CharField(max_length=200, blank=True) # Change URLField to CharField for simple local links
    order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_photo = models.ImageField(upload_to='testimonials/', blank=True)
    rating = models.PositiveIntegerField(default=5)  # 1-5
    review_text = models.TextField()
    product = models.ForeignKey('products.Product', null=True, blank=True, on_delete=models.SET_NULL, related_name='testimonials')
    is_featured = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Review by {self.customer_name}"

class USP(models.Model):   # "Why Highness" selling points
    title = models.CharField(max_length=100)        # "No Maida"
    description = models.TextField(max_length=200)
    icon = models.ImageField(upload_to='usps/', blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "USP"
        verbose_name_plural = "USPs"
        ordering = ['order']

    def __str__(self):
        return self.title

class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)          # "Co-Founder"
    bio = models.TextField()
    photo = models.ImageField(upload_to='team/')
    linkedin_url = models.URLField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()
    category = models.CharField(max_length=50, blank=True)  # "Shipping", "Products"
    order = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"
        ordering = ['order']

    def __str__(self):
        return self.question

class ContactInquiry(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Contact Inquiry"
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"Inquiry from {self.name} - {self.subject}"
