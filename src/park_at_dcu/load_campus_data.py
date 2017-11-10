import csv
from park_at_dcu.models import Campus
    
with open('../data/A3/Campus.csv') as ca:
   reader = csv.reader(ca)
   for row in reader:
      campus = Campus(int(row[0]),row[1])
      campus.save()
    

    
