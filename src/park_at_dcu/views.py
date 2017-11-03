# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import requests

from .models import Carpark, Facility, Campus, HistoricalData

def index(request):
   template = loader.get_template('park_at_dcu/index.html')
   return HttpResponse(template.render({},request))

def webservice(request):
    template = loader.get_template('park_at_dcu/webservice.html')
    carpark = request.GET.get('carpark', '')
    version = request.GET.get('version', '')
    webservice_url = 'http://suzannelittle.pythonanywhere.com/carpark/'+carpark
    
    if version == 'bad':
       real_time_info = requests.get(webservice_url+'?version=bad')
    else:
       real_time_info = requests.get(webservice_url)
         
    error_msg = get_error_msg(real_time_info)
    if error_msg == '':
       return HttpResponse(template.render(real_time_info.json(),request))
    else:
       return HttpResponse(template.render({'error_msg':error_msg},request))
       
def get_error_msg(info):
    '''
    returns an error message if there is a problem with the data 
    returned by the webservice
    '''
    try:
       info_json = info.json()
       if 'error_msg' in info_json:
         return info_json['error_msg']
       elif 'timestamp' not in info_json:
         return 'Invalid key'
       elif 'spaces_available' not in info_json:
         return 'Invalid key' 
       elif 'carpark_name' not in info_json:
         return 'Invalid key'
       elif info_json['spaces_available'] < 0:
         return 'Invalid value'
       elif isinstance(info_json['spaces_available'],float):
         return 'Invalid value'
       return ''
    except:
         return 'Invalid JSON'   


def facility(request):
    '''
    display the car parks suitable for a particular facility
    '''
    template = loader.get_template('park_at_dcu/facility.html')
    try:
       facility = request.GET.get('facility')
       carparks = Carpark.objects.filter(facility__facility_name=facility)
       if len(carparks) == 0:
         return HttpResponse(template.render({'error_msg':'No carparks for ' + facility}))
    except Facility.DoesNotExist:
       return HttpResponse(template.render({'error_msg':'Facility does not exist'}))
    except Carpark.DoesNotExist:
       return HttpResponse(template.render({'error_msg':'Carpark does not exist'}))
    return HttpResponse(template.render({'carparks':carparks},request))

def spaces(request):
    '''
    display the number of spaces in a campus
    '''
    template = loader.get_template('park_at_dcu/spaces.html')
    spaces = request.GET.get('spaces')
    campus = Carpark.objects.values('spaces','name').filter(campus__campus_name=spaces)
    if len(campus)==0:
      return HttpResponse(template.render({'error_msg':'no carpark associated with this campus ' + spaces}))
    return HttpResponse(template.render({'campus':campus},request))
    # write code for Q2

def occupancy(request):
    '''
    display the historical occupancy for a particular carpark at week 10, 3pm
    '''
    template = loader.get_template('park_at_dcu/occupancy.html')
    try:
       facility = request.GET.get('facility')
       carparks = Carpark.objects.filter(facility__facility_name=facility)
       if len(carparks) == 0:
         return HttpResponse(template.render({'error_msg':'No carparks for ' + facility}))
    except Facility.DoesNotExist:
       return HttpResponse(template.render({'error_msg':'Facility does not exist'}))
    except Carpark.DoesNotExist:
       return HttpResponse(template.render({'error_msg':'Carpark does not exist'}))
    return HttpResponse(template.render({'carparks':carparks},request))# write code for Q3

def carpark_for_time(request):
    '''
    display the carparks for a particular time on 26th Sept. 2016
    '''
    template = loader.get_template('park_at_dcu/carpark_for_time.html')
    try:
       facility = request.GET.get('facility')
       carparks = Carpark.objects.filter(facility__facility_name=facility)
       if len(carparks) == 0:
         return HttpResponse(template.render({'error_msg':'No carparks for ' + facility}))
    except Facility.DoesNotExist:
       return HttpResponse(template.render({'error_msg':'Facility does not exist'}))
    except Carpark.DoesNotExist:
       return HttpResponse(template.render({'error_msg':'Carpark does not exist'}))
    return HttpResponse(template.render({'carparks':carparks},request))# write code for Q4

