# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 13:58:37 2020

@author: ashvend
"""
import csv 
import time
import random as r

def extractDigits(lst): 
    return list(map(lambda el:[el], lst)) 

i=5000
finallist=[]
while(i<=25000):
    
    xyz=r.sample(range(1,i+1),i)
    start_time_T1 = time.time()
    xyz.sort()
    end_time_T1 = time.time()
    d=end_time_T1-start_time_T1
    finallist.append(d)
    print("the time taken to sort" ,i, "elements in a list is ",d)
    i+=5000
    

finallist = extractDigits(finallist)
 
file = open('time.csv', 'w+', newline ='')    

with file: 
    write = csv.writer(file)
    write.writerows(finallist)