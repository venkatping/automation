#!/usr/local/bin/python3
import os
"""
path="/root/python/section10/1os_path.py"
print(os.path.basename(path))
print(os.path.dirname(path))
path1="/home"
path2="automation"
print(os.path.join(path1,path2))
"""

path2="/root/pythonscripts/section10/1os_path.py"
"""
print(os.path.split(path2))
print(os.path.getsize(path2)) #it will give the size of the file 1os_path.py
"""
if os.path.exists(path2):
 print("Path exists")
else:
 print("Path does not exists")

if os.path.isfile(path2):
 print("it is a file")
else:
 print("it is a directory")
