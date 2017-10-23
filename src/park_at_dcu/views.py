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
   carpark=request.GET['carpark']
   url= "http://suzannelittle.pythonanywhere.com/carpark/" + carpark
   urlbad= "http://suzannelittle.pythonanywhere.com/carpark/%s?version=bad" % carpark
   
   dataType = request.GET.get("dataType", "correct")

   if dataType != "bad":
      output = requests.get(url) 
      output.text

      def is_json(myjson):
         try:
            json_object = json.loads(myjson)
         except ValueError:
            return False

      if is_json(output.text)== False:
         dict = {"error":"Invalid JSON"}
         return HttpResponse(template.render(dict,request))

      else:
         parsed_json = json.loads(output.text)

         return HttpResponse(template.render(parsed_json,request))
         
    
   else:
      output = requests.get(urlbad) 
      output.text
      parsed_json = json.loads(output.text)
   
      return HttpResponse(template.render(parsed_json,request))
      
    




# write code to:
    # 1) call the webservice with a particular car park
    # 2) retrieve the returned json in the form of a Python dictionary
    # 3) handle errors in the json (see the 'bad' version of the webservice)
    # 4) render the template (see last line in index method)

