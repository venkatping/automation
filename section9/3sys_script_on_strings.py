#!/usr/local/bin/python3
"""
given_string=input("Enter the string: ")
user_action=input("Enter your action lower:upper:title that you want to perform on the given string: ")
if user_action=="lower":
 print(given_string.lower())
elif user_action=="upper":
 print(given_string.upper())
elif user_action=="title":
 print(given_string.title())
else:
 print("you entered invalid choice, your choice should be lower:upper:title")
"""
import sys
#print("The length of th command line arguments should be 3: ", len(sys.argv))
if len(sys.argv) != 3:
 print("usage:")
 print(f"{sys.argv[0]} <your string> <lower|upper|title")
 sys.exit()
given_string=sys.argv[1]
user_action=sys.argv[2]
if user_action=="lower":
 print(given_string.lower())
elif user_action=="upper":
 print(given_string.upper())
elif user_action=="title":
 print(given_string.title())
else:
 print("you entered invalid choice, your choice should be lower:upper:title")
