# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

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
         
