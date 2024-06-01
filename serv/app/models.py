import json
from django.db import models

# Create your models here.
class Items(models.Model):
    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"
    title = models.CharField("title", max_length=30)
    description = models.CharField("description", max_length=300)
    price = models.IntegerField("price")

    def __str__(self):
        return self.title

    def get_dict(self):
        data = {
        "title": self.title,
        "description": self.description,
        "price": self.price,
        }
        return data
