from django.db import models
from .user import User

class Order(models.Model):
    total = models.FloatField()
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    is_open = models.BooleanField(null=True, blank=True)
