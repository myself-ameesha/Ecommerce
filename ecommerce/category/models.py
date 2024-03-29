from django.db import models

# Create your models here.
class category(models.Model):
    category_name=models.SlugField(max_length=50,unique=True)
    slug= models.CharField(max_length=100,unique=True)
    description=models.CharField(max_length=255)
    cat_img= models.ImageField(upload_to='photos/category' ,blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    
    def __str__(self):
        return self.category_name 