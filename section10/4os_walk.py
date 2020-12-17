#!/usr/local/bin/python3
import os
"""
path="/root/pythonscripts/section10"
#print(list(os.walk(path))) 
for each in list(os.walk(path)):
 print(each)
"""
"""
path="/root/pythonscripts/section10"
for r,d,f in list(os.walk(path)):
 #print(r)
 #print(d)
 #print(f)
 #print(r,d,f)
 print(r,f)
"""
path="/root/pythonscripts/section10"
for r,d,f in list(os.walk(path)):
 if len(f) != 0:
   print(r)
   #print(d)
   for each_file in f:
     print(os.path.join(r,each_file))
   print("---------------")




