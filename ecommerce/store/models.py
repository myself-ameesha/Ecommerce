from django.db import models
from category.models import category

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=255,blank=True)
    slug = models.SlugField(max_length=200, unique=True,blank=True)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    images =  models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    created_date = models.DateField(auto_now_add = True)
    modified_date = models.DateField(auto_now = True)
    is_active = models.BooleanField(default=True)# Soft delete flag
    

    def __str__(self):
        return self.product_name