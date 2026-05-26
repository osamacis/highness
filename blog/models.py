from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"

    def __str__(self):
        return self.name

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True, related_name='posts')
    featured_image = models.ImageField(upload_to='blog/')
    excerpt = models.TextField(max_length=300)
    content = models.TextField()                    # HTML/text content
    author = models.CharField(max_length=100, default='Highness')
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'),
        ('hard', 'Hard'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    featured_image = models.ImageField(upload_to='recipes/')
    prep_time = models.PositiveIntegerField(help_text='in minutes')
    cook_time = models.PositiveIntegerField(help_text='in minutes')
    servings = models.PositiveIntegerField(default=2)
    age_group = models.ForeignKey('products.AgeGroup', null=True, on_delete=models.SET_NULL, related_name='recipes')
    difficulty = models.CharField(max_length=20, choices=DIFFICULTY_CHOICES, default='easy')
    ingredients_list = models.TextField(help_text='Newline-separated list of ingredients')            # Newline-separated
    instructions = models.TextField(help_text='Step-by-step instructions (can contain HTML)')                # HTML step-by-step
    related_products = models.ManyToManyField('products.Product', blank=True, related_name='recipes')
    is_featured = models.BooleanField(default=False)
    published_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title

    @property
    def total_time(self):
        return self.prep_time + self.cook_time

    def get_ingredients_list(self):
        return [i.strip() for i in self.ingredients_list.split('\n') if i.strip()]
