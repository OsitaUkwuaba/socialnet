import json
import requests
from celery import shared_task
from .models import  Geolocation
from datetime import date
from django.contrib.auth.models import User

# Getting geolocation data
@shared_task
def get_geolocation_data():
    api_url = "https://ipgeolocation.abstractapi.com/v1/"
    api_key = "9674641bf8d5484abcf4bb0d39f48088"
    params = {
       'api_key': api_key,
       
       }
    try:
        request = requests.get(api_url, params=params)
#         print(response.content)
    except requests.exceptions.RequestException as api_error:
        print(f"An error occured connecting to API: {api_error}")
        raise SystemExit(api_error)
        
    geo_data =  json.loads(request.text)
    country_code = geo_data['country_code']
    ip_address =  geo_data['ip_address']
        
    return country_code, ip_address


@shared_task
def get_holiday():
    api_url = "https://holidays.abstractapi.com/v1/"
    key = "75c06a385ad542ab9a11a0cfbce9a143"
    country, _ = get_geolocation_data()
#     year = datetime.now().year
#     month = datetime.now().month
#     day = datetime.now().day
    today = date.today()
    year = date.today().year
    month = date.today().month
    day = date.today().day
    params = {
       'api_key': key,              
        'country': country,
        'year': year,
        'month': month,
        'day': day,
        
       
       }
    try:
        request = requests.get(api_url, params=params)
        
    except requests.exceptions.RequestException as api_error:
        print(f"There was an error contacting the Geolocation API: {api_error}")
        raise SystemExit(api_error)
        
    holiday_data = json.loads(request.text)
       
    if holiday_data:
        return today, holiday_data[0]['name']
    else:
        return today,""
    
        
@shared_task
def enrich_user_data(username):
    # user =  Profile.objects.get(pk = 12)
    # u = User.objects.get(username='john')
    user = User.objects.get(username=username)
    country_code, ip_address = get_geolocation_data()
    day, holiday =  get_holiday()
    
    Geolocation.objects.create(user=user, ip_address= ip_address, country_code= country_code, signup_date =day, holiday=holiday)

    
    