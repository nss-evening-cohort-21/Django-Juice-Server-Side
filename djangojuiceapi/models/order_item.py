from django.db import models
from .order import Order
from .item import Item

class OrderItem(models.Model):
  
 
  order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
  item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
  quantity = models.IntegerField()
