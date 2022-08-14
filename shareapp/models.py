from django.db import models
from django.conf import settings
from datetime import date
# import django

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',
                              blank=True)
        
    def __str__(self):
        return f'Profile for user {self.user.username}'

class Geolocation(models.Model):
    user =  models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ip_address = models.GenericIPAddressField()
    country_code = models.CharField(max_length = 3, blank=True, null=True)    
    signup_date = models.DateField(default=date.today().day)
    holiday = models.CharField(max_length = 100, blank=True, null=True)