from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    category_image = models.ImageField(upload_to="vrequest/static/category")
    slug = models.SlugField(default="", null=False)