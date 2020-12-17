#!/usr/local/bin/python3
import os
req_file=input("Enter the file that you want to search: ")
for r,d,f in list(os.walk("/")):
  for each_file in f:
    if req_file==each_file:
      #print(r)
      #print(f)
      #print(r,d,f)
      print(os.path.join(r,each_file))
