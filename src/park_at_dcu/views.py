# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import requests

def index(requests):

   #return HttpResponse("Welcome to Park@DCU!")

   template = loader.get_template('park_at_dcu/index.html')
   return HttpResponse(template.render({},requests))

def webservice(requests):
    template = loader.get_template('park_at_dcu/webservice.html')
    return HttpResponse(template.render({},requests))

    # write code to:
    # 1) call the webservice with a particular car park
    # 2) retrieve the returned json in the form of a Python dictionary
    # 3) handle errors in the json (see the 'bad' version of the webservice)
    # 4) render the template (see last line in index method)
    
#r = requests.get("http://suzannelittle.pythonanywhere.com/carpark/StPats")
#r.text


#data = json.loads(r.text)

#for item in data:
  #print data[item]
