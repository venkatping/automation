#!/usr/local/bin/python3
"""
my_list=[]
bool(my_list)
my_list=[2,4,6,'python scripting',5.6]
bool(my_list)
my_list[-1] #it will print 5.6
my_list[-4] #it ill print 4
print(my_list[3]) #it will print python scripting
print(my_list[3][1]) #it will print y
print(my_list[3].strip('p')) #it will print ython scripting
print(my_list[1:]) #it wil print from index 1
print(my_list[0:]) #it will print entire values
print(my_list[:]) #it will print entire values
print(my_list[3:5]) #it will print from index 3 to index 4

my_list[0]=45 #changing index 0 value 2 to 45
print(my_list)
"""
my_list=[3,5,2,7,3,8,5,9]
print(my_list.index(5)) #it will print the index value of 5
print(my_list.index(7))
print(my_list.index(2))
print(my_list.index(5,2)) #it will print the index value of 5 after which were present after index 2
print(my_list.count(5)) #it will count how many times 5 is there
print(my_list.count(7))
print(my_list)
my_list.clear()
print(my_list)








