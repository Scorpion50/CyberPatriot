import os
import time

input("Have you ran this program in the default user's desktop?")
input("Have you ran this as root?")
input("Have you added the users.txt file?")
    
users = open("./users.txt","r")

password = input("Password for all users: ")
os.system(f"echo {password} is the password for all users in user.txt >> changelog.txt")
for user in users:
    os.system(f'echo "{password}\n{password}" | sudo passwd {user}')



print("Script Complete!")
time.sleep(1)
