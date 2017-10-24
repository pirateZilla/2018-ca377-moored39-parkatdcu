import csv
from datetime import time
from park_at_dcu.models import HistoricalData

with open('../data/A3/CarparkHistoricalData.csv') as hd:
   reader = csv.reader(hd)
   
   
   for row in reader:
      i = 0
      history = HistoricalData(i,int(row[0]),int(row[1]),row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13],row[14],row[15],row[16])
      history.save()
   i= i+ 1
    



























"""      history = HistoricalData(int(col_0),int(col_1),int(col_2),col_3,col_4,col_5,col_6,col_7,col_8,col_9,col_10,col_11,col_12,col_13,col_14,col_15,col_16)
      history.save()
    
    

"""


""""col_0 = list(zip(*reader))[0]
   col_1 = list(zip(*reader))[0]
   col_2 = list(zip(*reader))[2]
   col_3 = list(zip(*reader))[3]
   col_4 = list(zip(*reader))[4]
   col_5 = list(zip(*reader))[5]
   col_6 = list(zip(*reader))[6]
   col_7 = list(zip(*reader))[7]
   col_8 = list(zip(*reader))[8]
   col_9 = list(zip(*reader))[9]
   col_10 = list(zip(*reader))[10]
   col_11 = list(zip(*reader))[11]
   col_12 = list(zip(*reader))[12]
   col_13 = list(zip(*reader))[13]
   col_14 = list(zip(*reader))[14]
   col_15 = list(zip(*reader))[15]
   col_16 = list(zip(*reader))[16]"""
