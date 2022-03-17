from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    #generate valid url
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def get_absolute_url(self):
        return reverse("store:categories-list", args=[self.slug])

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name="category",on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="product_creator",on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=255, default="admin")
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="images/")
    # generate url for individual elements
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    # triggered only when object is first created
    created_at = models.DateTimeField(auto_now_add=True) 
    # triggered each time the object is updated
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = "Products"
        ordering = ('created_at',)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        return reverse("store:detail", args=[self.slug])

