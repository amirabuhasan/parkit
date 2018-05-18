from django.conf import settings
from django.db import models
from django.utils import timezone
#from django.contrib.contenttypes.models import ContentType
#from django.db.models.signals import pre_save

#from django.utils.safestring import mark_safe
#from django.utils.text import slugify
#from markdown_deux import markdown

from rent.models import (
    ParkingForRent,
)

# Create your models here.
class CarDatabase (models.Model):
    user  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    occupied_by = models.ForeignKey(ParkingForRent,on_delete=models.CASCADE,blank=True,default='None')
    car_model = models.CharField(max_length=100,default='None')
    car_registery = models.CharField(max_length=100,default='ABC1234')

    def __str__(self):
        return self.car_registery