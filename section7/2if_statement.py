#!/usr/local/bin/python3
my_even_no=[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42]
user_num=eval(input("Enter your number: "))
if user_num in my_even_no:
 print(f"The number exists in even number list: {user_num}")
else:
 print(f"The number does not exists in my even number list: {user_num}")
