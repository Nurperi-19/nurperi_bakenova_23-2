from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=55)
    icon = models.ImageField(blank=True, null=True)

class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.CharField(max_length=255)
    image = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255)
    color = models.TextField(blank=True, null=True)
    description = models.TextField()
    price = models.FloatField()
    categories = models.ManyToManyField(Category)

class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateField(auto_now=True)
