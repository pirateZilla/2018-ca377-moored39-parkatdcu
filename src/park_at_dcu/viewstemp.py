# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import urllib
import json
import requests

# Create your index view here. It should display the message 'Welcome to Park@DCU!'

def index(request):
   template = loader.get_template('park_at_dcu/index.html')
   return HttpResponse(template.render({},request))

def webservice(request):
    template = loader.get_template('park_at_dcu/webservice.html')
    carpark= request.GET['carpark']
    url= "http://suzannelittle.pythonanywhere.com/carpark/" + carpark
    output=requests.get(url)
    parsed_json = json.loads(output.text)
    parsed_json = {'parsed_json': parsed_json}

    return HttpResponse(template.render(parsed_json,request))



# write code to:
    # 1) call the webservice with a particular car park
    # 2) retrieve the returned json in the form of a Python dictionary
    # 3) handle errors in the json (see the 'bad' version of the webservice)
    # 4) render the template (see last line in index method)
