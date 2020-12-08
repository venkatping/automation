#!/usr/local/bin/python3
'''
my_name="Naveen"
my_short_name='venkata'
my_goal="""
i started my career as Linux admin
and moved to python"""
print(f"my name is: {my_name} \nmy short name is: {my_short_name} \nmy goal is: {my_goal}")
'''

'''
my_str="" #This is empty string so it will output as False
print(f"{bool(my_str)}")
my_string=" " #In python space is also a character so it ouput as True
print(f"{bool(my_string)}")
'''
'''
#slicing of a string
my_fav_scripting="python scripting"
print(f"{my_fav_scripting}") #one way of printing a variable
print(my_fav_scripting) #second way of printing a variable
print(my_fav_scripting[0]) #printing index 0 value
print(my_fav_scripting[5]) #printing index 5 value
print(my_fav_scripting[0:5]) #printing index 0 to 5 values
print(my_fav_scripting[0:6]) #printing index 0 to 6 values
print(my_fav_scripting[:5]) #printing 0 to 5 index values
print(my_fav_scripting[2:]) #printing 2 to last index values
print(my_fav_scripting[-1]) #printing last index value
print(my_fav_scripting[5:10]) #printing 5 to 10 index values
'''
'''
#deleting aa string is not possibel so iam reassigning
my_fav_string="python tutorials"

#Finding length of a string
print(len(my_fav_string))
my_str_len=len(my_fav_string)
print(f"The length of the string is: {my_str_len}")
print(f"The length of the string is: {len(my_fav_string)}")
'''
#concatenate two strings

#my_str1="python "
my_str1="python"
my_str2="scripting"
#my_str3=my_str1+my_str2
#my_str3=my_str1+" "+my_str2+" "+"Tutorials"
my_str3=my_str1+" "+my_str2
print(f"Concatenate {my_str1} and {my_str2} is: {my_str3}")
