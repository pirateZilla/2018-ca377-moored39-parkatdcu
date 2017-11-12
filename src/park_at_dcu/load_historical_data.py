import csv

from park_at_dcu.models import HistoricalData
    
with open('../data/A3/CarparkHistoricalData.csv') as h:
   reader = csv.reader(h)
   i = 0
   for row in reader:
      #data = HistoricalData(i,int(row[0]),int(row[1]))
      data = HistoricalData(i,int(row[0]),int(row[1]),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
      i = i + 1
      data.save()
    

    

