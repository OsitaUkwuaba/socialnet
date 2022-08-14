from django.contrib import admin
from .models import Profile, Geolocation
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    
@admin.register(Geolocation)
class GeolocationAdmin(admin.ModelAdmin):
    list_display = ["user","ip_address", "country_code", "signup_date", "holiday"]

# Register your models here.

# from .models import Profile
# @admin.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user','date_of_birth','photo']
