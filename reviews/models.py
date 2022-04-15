from products.models import Product
from django.db import models

# Create your models here.
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    score = models.BooleanField()