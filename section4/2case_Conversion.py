#!/usr/local/bin/python3
my_string="pYtHoN sCrIpTiNg"
print(my_string.lower())
print(my_string.upper())
print(my_string.title())
print(my_string)
#strings are immutable, you cannot change/modify the string or cannot modify the part of the string, if you to have lower case string as your variable just follow below command
my_string_lower=my_string.lower()
print(my_string_lower)

print(my_string.swapcase()) #swapcase will perform lower case letters into uppercase letter can uppercase letters into lowercase letters in a variable
print(my_string.capitalize()) #starting letter of the variable will become capital
print(my_string.casefold())
