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

print("Password Reset Done")
time.sleep(1)

print("Searching for .mp3 and .mp4 files")
os.system("sudo locate *.mp3 >> changeLog.txt")

print("Findings in changeLog.txt!")
time.sleep(0.5)

print("Turning on Firewall")
os.system("ufw enable")
time.sleep(0.5)

print("Checking for common unauthorized programs.")
time.sleep(0.5)
os.system("locate nmap >> changelog.txt")
os.system("locate zenmap >> changelog.txt")
os.system("locate wireshark >> changelog.txt")
os.system("locate ophcrack >> changelog.txt")
os.system("locate nginx >> changelog.txt")
print("Findings are in changelog.txt")
time.sleep(0.5)

print("Checking crontab jobs!")
os.system("sudo find /var/spool/cron -type f -ls >> changelog.txt")
time.sleep(0.5)
print("Findins in changelog.txt")
time.sleep(0.5)

print("Script Complete!")
time.sleep(1)
