from django.db import models
from .user import User

class Order(models.Model):
    total = models.DecimalField(max_digits=7, decimal_places=2)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    is_open = models.BooleanField(null=True, blank=True)
