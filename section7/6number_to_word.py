#!/usr/local/bin/python3
"""
num=eval(input("Enter Your number: "))
if num==1:
 print("One")
elif num==2:
 print("Two")
elif num==3:
 print("Three")
elif num not in [1,2,3]:
 print("Invalid number")
"""
"""
num=eval(input("Enter Your number: "))
if num==1:
 print("One")
elif num==2:
 print("Two")
elif num==3:
 print("Three")
else:
 print("Invalid number")
"""
"""
num=eval(input("Enter any number between 1 to 4: "))
if num in [1,2,3,4]:
 if num==1:
   print("One")
 elif num==2:
   print("Two")
 elif num==3:
   print("Three")
 elif num==4:
   print("Four")
else:
 print("Invalid number")
"""
num=eval(input("Enter any number between 1 to 4: "))
num_word={1:'One',2:'Two',3:'Three',4:'Four'}
if num in [1,2,3,4]:
 print(num_word.get(num))
else:
 print("Invalid number")
