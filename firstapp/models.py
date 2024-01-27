from django.db import models

class Details(models.Model):
    name = models.CharField(max_length=500)
    cname = models.CharField(max_length=100)
    photo = models.CharField(max_length=500)
    time = models.CharField(default = '',max_length=100)  # str
    month =  models.PositiveIntegerField(default=0)  # Set your desired default value
    view = models.PositiveIntegerField(default=0)  # Set your desired default value
