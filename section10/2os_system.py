#!/usr/local/bin/python3
import os
cmd="uname -r"
print(os.system(cmd))
rt=os.system(cmd) #once the command is executed it will provide ouput and return code also, if return code is 0 then it means command executed successfully
if rt==0:
 print("your command executed successfully")
else:
 print("your command is not executed")
