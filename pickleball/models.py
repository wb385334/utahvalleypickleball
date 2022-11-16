from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class location(models.Model):
    court_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, default='UT')
    courts = models.IntegerField(default=0)
    openTime = models.TimeField(default=0)
    closeTime = models.TimeField(default=0)
    indoor = models.BooleanField
        

