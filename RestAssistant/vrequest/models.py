from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    category_image = models.ImageField(upload_to="vrequest/static/category")
    slug = models.SlugField(default="", null=False)


class ShowAllFood(models.Model):
    name = models.CharField(max_length=250)
    foodImage = models.ImageField(upload_to='vrequest/static/allFoodImg')
    description = models.CharField(max_length=1000)
    price = models.IntegerField()
    slug = models.SlugField(default="", null=False)
