import csv
from datetime import time
from park_at_dcu.models import Carpark

with open('../data/A3/Carpark.csv') as cp:
   reader = csv.reader(cp)
   for row in reader:
      carpark = Carpark(int(row[0]),row[1],int(row[2]),row[3],time(hour=int(row[4])),time(hour=int(row[5])),int(row[6]),int(row[7]),row[8],int(row[9]),int(row[10]))
      carpark.save()
    
    
