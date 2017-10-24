# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Campus(models.Model):
   campus = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name

class Carpark(models.Model):
   carpark = models.IntegerField(primary_key=True)
   name = models.CharField(max_length=100)
   campus = models.ForeignKey(Campus,on_delete = models.CASCADE)
   location = models.CharField(max_length=200)
   opening_hours = models.TimeField()
   closing_hours = models.TimeField()
   spaces = models.IntegerField()
   disabled_spaces = models.IntegerField()
   entrance_location = models.CharField(max_length=50)
   is_free = models.BooleanField()
   is_for_public = models.BooleanField()

   def __str__(self):
      return self.name

class Facility(models.Model):
   facility_id = models.IntegerField(primary_key=True)
   facility_name = models.CharField(max_length=100)
   carpark = models.ForeignKey(Carpark,on_delete=models.CASCADE)

   def __str__(self):
      return self.facility_name + "," + str(self.carpark)

class HistoricalData(models.Model):
   data_id = models.IntegerField(primary_key=True)
   carpark = models.ForeignKey(Carpark,on_delete=models.CASCADE)
   week = models.IntegerField()
   am7 = models.CharField(max_length=10)
   am8 = models.CharField(max_length=10)
   am9 = models.CharField(max_length=10)
   am10 = models.CharField(max_length=10)
   am11 = models.CharField(max_length=10)
   pm12 = models.CharField(max_length=10)
   pm13 = models.CharField(max_length=10)
   pm14 = models.CharField(max_length=10)
   pm15 = models.CharField(max_length=10)
   pm16 = models.CharField(max_length=10)
   pm17 = models.CharField(max_length=10)
   pm18 = models.CharField(max_length=10)
   pm19 = models.CharField(max_length=10)
   pm20 = models.CharField(max_length=10)
   pm21 = models.CharField(max_length=10)

   
