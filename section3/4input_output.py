#!/usr/local/bin/python3
"""
a=446
b=682
result=a+b
print(f"The sum of {a} and {b} is: {result}")
"""

"""
a=input("Enter a value: ")
b=input("Enter b value: ")
print(f"The type of {a} is: {type(a)}") #actually the type of a value is integer but in the output it shows as string so use eval instead of input
"""

a=eval(input("Enter a value: "))
b=eval(input("Enter b value: "))
result=a+b
print(f"The sum of {a} and {b} is: {result}")
#print(f"The type of result is:  {type(result)}")
