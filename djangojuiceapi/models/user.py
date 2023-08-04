from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=16)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=300)
    uid = models.CharField(max_length=100)

   
   
