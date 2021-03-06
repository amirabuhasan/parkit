from __future__ import unicode_literals

from django.db import models

# Create your models here.

class ParkingEnquiry (models.Model):
    db_office     = models.TextField(default="Office Location")
    db_email      = models.EmailField(max_length=254,default="example@parkitmy.com")
    db_contact    = models.CharField(max_length=255, default="0123456789")
    first_name    = models.CharField(max_length=255, default="first_name")
    last_name     = models.CharField(max_length=255, default="last_name")
    db_longitude  = models.CharField(max_length=255, default="Longitude")
    db_latitude   = models.CharField(max_length=255, default="Latitude")
    db_location   = models.CharField(max_length=100,default='Where?')
    db_period     = models.CharField(max_length=100,blank=True)
    db_price      = models.CharField(max_length=100, blank=True)
    list_status   = (
        ('New' , 'New'),        
        ('Done', 'Done'),
        ('WIP', 'WIP'),
    )
    db_status     = models.CharField(max_length=100, choices=list_status, default='New')
    timestamp     = models.DateTimeField(auto_now=False, auto_now_add=True)