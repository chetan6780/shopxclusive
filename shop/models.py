from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    seller_name = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name
