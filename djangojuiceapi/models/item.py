from django.db import models

class Item(models.Model):
  
    name = models.CharField(max_length=50)
    price = models.FloatField()
    image_url = models.URLField()
    description = models.CharField(max_length=100)
    