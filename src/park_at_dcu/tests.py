# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from park_at_dcu.models import Carpark,Facility,Campus,HistoricalData
from datetime import time

# Create your tests here.
class IndexTests(TestCase):

    def test_welcome(self):
        """
        An appropriate welcome message is displayed once the page is loaded
        """
        response = self.client.get(reverse('park_at_dcu:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to Park@DCU!")

class WebServiceTests(TestCase):
    
    def test_webservice(self):
        """                                                                            Test calling of webservice for each carpark
        """ 
        for carpark in ['multistorey','creche','invent','library','StPats','alpha','allhallows']:
           self.webservice(carpark)
    
    def test_bad_webservice(self):
        """                                                                            Test error handling using the bad version of webservice
        """
        for carpark in ['multistorey','creche','invent','library','StPats','alpha','allhallows']:
           self.bad_webservice(carpark)

    def test_invalid_name(self):
        """                                                                            Test calling webservice for invalid carpark  
        """
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'multistory'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'An error has occurred')
        self.assertNotContains(response, 'Spaces Available')
        self.assertNotContains(response,'<table>')
        
    
    def webservice(self, carpark):
        """                                                                            Test calling webservice for individual carpark  
        """
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':carpark})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, carpark)
        self.assertNotContains(response,'An error has occurred')

    def bad_webservice(self,carpark):
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':carpark,'version':'bad'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'An error has occurred')
        self.assertNotContains(response, 'Spaces Available')
        self.assertNotContains(response,'<table>')
         
class DatabaseTests(TestCase):
   
    def setup(self):
        """
        Sets up a test database
        """
        campus = Campus(1,'Test Campus')
        carpark1 = Carpark(1, 'Test CP1', 1,'off Collins Ave',time(hour=8),time(hour=22),750,17,"53.386284, -6.256948",0,1)
        carpark2 = Carpark(2, 'Test CP2', 1,'Ballymun Road',time(hour=7),time(hour=22),250,23,"53.386284, -6.256948",0,1)
        carpark3 = Carpark(3, 'Test CP3', 1,'off Collins Ave',time(hour=7),time(hour=22),300,25,"37.386284, -10.256948",0,0)
        facility = Facility(1,'Test Facility',1)
        historicaldata = HistoricalData('1',94,10,'83%','71%','12%','66%','89%','47%','17%','46%','2%','7%','84%','47%','9%','1%','64%')
        campus.save()
        carpark1.save()
        carpark2.save()
        carpark3.save()
        facility.save()
        historicaldata.save()
        

    def test_historicaldata(self): #TEST CASE 3 
    
        self.setup()
        response = self.client.get(reverse('park_at_dcu:occupancy'),{'historicaldata':'Test his'})
        self.assertEqual(response.status_code,200)
        self.assertNotContains(response, {})


