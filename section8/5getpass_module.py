#!/usr/local/bin/python3
#db_pass=input("Enter your password: ")  #By using this command it prompts to enter password but the disadvantage is the password will be visible on the screen, to void this we are using getpass so that password will be hidden
import getpass
#db_pass=getpass.getpass()
db_pass=getpass.getpass(prompt="Enter the password: ")
print(f"The entered password is: {db_pass}")
