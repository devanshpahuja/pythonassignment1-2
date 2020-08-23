# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 14:53:00 2020

@author: ashvend
"""
import string as s
import random as r
import os
os.getcwd()
i=0
for i in range(1,501):
        filename = str(i) + '.txt'
        writeFp = open(filename,'w')
        x = 1
        for x in range(1,20001):
            d = r.sample(s.ascii_letters,20)
            m="".join(d)
            writeFp.write(m+"\n")
        writeFp.close()
        

        
        
    