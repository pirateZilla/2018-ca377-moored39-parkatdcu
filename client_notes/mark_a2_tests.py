# -*- coding: utf-8 -*-
# For marking purposes, some tests are designed to work with a non-randomized version of the website 
# which associates specific errors with specific carparks
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from park_at_dcu.models import Carpark,Facility,Campus,HistoricalData
from datetime import time

class WebServiceTests(TestCase):
    
    def test_webservice(self):
        """
        Test calling of webservice for each carpark
        """ 
        for carpark in ['multistorey','creche','invent','library','StPats','alpha','allhallows']:
           self.webservice(carpark)

    def test_bad_webservice(self):
        """                                                                    
        Test error handling using the bad version of webservice             
        """
        for carpark in ['multistorey','creche','invent','library','StPats','alpha','allhallows']:
           self.bad_webservice(carpark)    
     
    def test_webservice_401(self):
        '''
        Test what happens when a 401 is returned
        Works with non-randomized version of the website which associates specific errors with specific carparks
        '''
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'creche','version':'bad'})
        self.assertContains(response,'Sorry')
    
    def test_webservice_503(self):
        '''
        Test what happens when a 503 is returned
        '''
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'multistorey','version':'bad'})
        self.assertContains(response,'Sorry')

    def test_webservice_neg(self):
        '''
        Test what happens when a negative value is returned as the number of spaces
        '''
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'invent','version':'bad'})
        self.assertContains(response,'Invalid value')
    
    def test_webservice_nonint(self):
        '''
        Test what happens when a non-integer value is returned as the number of spaces
        '''
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'library','version':'bad'})
        self.assertContains(response,'Invalid value')
    
    def test_webservice_invalid_key(self):
        '''
        Test what happens when an invalid key is returned
        '''
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'alpha','version':'bad'})
        self.assertContains(response,'Invalid key')
        
    def test_webservice_invalid_json(self):
        '''
        Test what happens when invalid json is returned
        '''
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'allhallows','version':'bad'})
        self.assertContains(response,'Invalid JSON')
    
    def test_invalid_name(self):
        """
        Test calling webservice for invalid carpark  
        """
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':'multistory'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'An error has occurred')
        self.assertNotContains(response, 'Spaces Available')
        self.assertNotContains(response,'<table>')
            
    def webservice(self, carpark):
        """
        Test calling webservice for individual carpark  
        """
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':carpark})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, carpark)
        self.assertNotContains(response,'An error has occurred')

    def bad_webservice(self,carpark):
        """
        Test calling bad webservice for individual carpark  
        """
        response = self.client.get(reverse('park_at_dcu:webservice'),{'carpark':carpark,'version':'bad'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'An error has occurred')
        self.assertNotContains(response, 'Spaces Available')
        self.assertNotContains(response,'<table>')

         




     
    
    

        
