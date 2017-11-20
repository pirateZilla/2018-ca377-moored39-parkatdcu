# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.urls import reverse

from park_at_dcu.models import Carpark,Facility,Campus,HistoricalData
from datetime import time
         
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
        hist = HistoricalData(1, 1, 10, '7%','8%','9%','10%','11%','12%','13%','14%','15%','16%','17%','18%','19%','20%','21%')
        campus.save()
        carpark1.save()
        carpark2.save()
        carpark3.save()
        facility.save()
        hist.save()
        
    def test_facility(self):
        """                                                                            Test retrieving carparks for a given facility
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:facility'),{'facility':'Test Facility'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'CP1')

    def test_facility_error(self):
        """                                                                            Test error handling when retrieving carparks for a given facility
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:facility'),{'facility':'Invalid Facility'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'No carparks')

    def test_spaces(self):
        """                                                                            Test retrieving carpark spaces for a campus
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:spaces'),{'campus':'Test Campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, '1300')

    def test_spaces_error(self):
        """                                                                            Test error handling when retrieving carpark spaces for a campus
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:spaces'),{'campus':'Invalid Campus'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'No carparks')

    def test_time(self):
        """                                                                            Test retrieving carparks available to the general public for a particular time
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:carpark_for_time'),{'time':'7'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'CP2')
        self.assertNotContains(response,'CP1')
        self.assertNotContains(response,'CP3')

    def test_time_error(self):
        """                                                                            Test error handling when retrieving carparks available to the general public for a particular time
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:carpark_for_time'),{'time':'25'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response, 'Invalid time')

    def test_occupancy(self):
        """  tests retrieving occupancy at 3pm in Week 10 for a given carpark
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:occupancy'),{'carpark':'Test CP1'})
        self.assertEqual(response.status_code,200)
        self.assertContains(response,'15%')

    def test_occupancy_error(self):
        """ tests error handling when retrieving occupancy
        """
        self.setup()
        response = self.client.get(reverse('park_at_dcu:occupancy'),{'carpark':'Invalid Carpark'})
        self.assertEqual(response.status_code,200)
        self.assertIsNotNone(response.context['error_msg'])
        


     
    
    

        
