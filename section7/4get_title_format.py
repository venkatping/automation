#!/usr/local/bin/python3
user_string=input("Enter the string: ")
user_choice=input("Do you want to change the string to title format: ")
if user_choice == "yes":
 print(user_string.title())
else:
 print(user_string)
