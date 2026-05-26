from django.db import models

class AgeGroup(models.Model):
    name = models.CharField(max_length=50)        # "6+ Months", "12+ Months"
    slug = models.SlugField(unique=True)
    icon = models.ImageField(upload_to='age_groups/', blank=True)
    description = models.TextField(blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)        # "Cereals", "Pancake Mixes"
    slug = models.SlugField(unique=True)
    icon = models.ImageField(upload_to='categories/', blank=True)
    image = models.ImageField(upload_to='categories/', blank=True)
    description = models.TextField(blank=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')
    order = models.PositiveIntegerField(default=0)
    is_featured = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    age_groups = models.ManyToManyField(AgeGroup, blank=True)
    short_description = models.TextField(max_length=300)
    description = models.TextField()               # Rich text description
    ingredients = models.TextField()
    nutritional_info = models.TextField(blank=True)
    weight = models.CharField(max_length=50)        # "200g", "Pack of 6"
    mrp = models.DecimalField(max_digits=8, decimal_places=2)
    selling_price = models.DecimalField(max_digits=8, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    review_count = models.PositiveIntegerField(default=0)
    is_bestseller = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_bestseller', '-created_at']

    def __str__(self):
        return self.name

    @property
    def discount_percentage(self):
        if self.mrp > self.selling_price:
            discount = ((self.mrp - self.selling_price) / self.mrp) * 100
            return round(discount)
        return 0

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='products/')
    alt_text = models.CharField(max_length=200, blank=True)
    is_primary = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.product.name} Image {self.id}"
