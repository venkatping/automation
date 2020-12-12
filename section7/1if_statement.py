#!/usr/local/bin/python3
import os
terminal_width=os.get_terminal_size().columns
given_string=input("Enter the string: ")
print(given_string)
user_conf=input("Do you want to align text: say yes or no: ")
if user_conf == "yes":
 print(given_string.center(terminal_width).title())
 print(given_string.ljust(terminal_width).title())
 print(given_string.rjust(terminal_width).title())

