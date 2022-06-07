from ast import ClassDef
from email.mime import image
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    desc = models.CharField(max_length=255)
    image = models.ImageField(blank=True, upload_to='images/')

    def __str__(self):
        return self.name
