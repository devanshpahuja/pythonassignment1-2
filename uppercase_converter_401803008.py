# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 15:54:49 2020

@author: ashvend
"""
import time 
import csv

def extractDigits(lst): 
    return list(map(lambda el:[el], lst)) 


timetaken=[]
i=0
start_time_T1 = time.time()
for i in range(1,501):
        filename = str(i) + '.txt'
        readFp = open(filename,'r+')
        text = readFp.read()
        readFp.seek(0)
        readFp.write(text.upper())
        readFp.close()
        end_time_T1 = time.time()
        if i%100==0:
         d=end_time_T1-start_time_T1
         timetaken.append(d)
         


timeslots = ["T100","T200","T300","T400","T500"]
timetaken = extractDigits(timetaken)
timeslots=extractDigits(timeslots)   
file = open('timeforuppercase.csv', 'w+', newline ='')  

with file: 
    write = csv.writer(file)
    write.writerows(timetaken)  



    
    
