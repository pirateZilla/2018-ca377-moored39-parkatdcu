import csv
from park_at_dcu.models import Facility
    
with open('../data/A3/Facility.csv') as f:
   reader = csv.reader(f)
   i = 0
   for row in reader:
      facility = Facility(i,row[0],int(row[1]))
      facility.save()
      i = i+1
    

    
