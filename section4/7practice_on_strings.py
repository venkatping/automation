#!/usr/local/bin/python3
"""
given_string=input("Enter your string: ")
print(given_string.center(113))
print(given_string.ljust(113))
print(given_string.rjust(113))
"""
import os
given_string=input("Enter Your String: ")
print(os.get_terminal_size())
terminal_width=os.get_terminal_size().columns
print(given_string.center(terminal_width).title())
print(given_string.ljust(terminal_width).title())
print(given_string.rjust(terminal_width).title())

