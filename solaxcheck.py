import requests
import threading
from colorama import Fore
import threading
import time
from os import system
import socket
import sys


def connect():
    s = socket.socket()
    host = "SLPTD003080"
    port = 8080
    s.connect((host,port))
    print(" ")

    while 1:    
        incoming_message = s.recv(1024)
        incoming_message = incoming_message.decode()
        print(" Server : ", incoming_message)
        print("")
        message = input(str(">> "))
        message = message.encode()
        s.send(message)
        print("message has been sent...")
        print("")
        quit()





system("title " + "@2L21L1 . TELL-CHECKER")

logog = """
████████╗███████╗██╗░░░░░██╗░░░░░░░░░░░░█████╗░██╗░░██╗███████╗░█████╗░██╗░░██╗
╚══██╔══╝██╔════╝██║░░░░░██║░░░░░░░░░░░██╔══██╗██║░░██║██╔════╝██╔══██╗██║░██╔╝
░░░██║░░░█████╗░░██║░░░░░██║░░░░░█████╗██║░░╚═╝███████║█████╗░░██║░░╚═╝█████═╝░
░░░██║░░░██╔══╝░░██║░░░░░██║░░░░░╚════╝██║░░██╗██╔══██║██╔══╝░░██║░░██╗██╔═██╗░
░░░██║░░░███████╗███████╗███████╗░░░░░░╚█████╔╝██║░░██║███████╗╚█████╔╝██║░╚██╗
░░░╚═╝░░░╚══════╝╚══════╝╚══════╝░░░░░░░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░╚═╝░░╚═╝
       
by @2l21l1 on instagram
"""

pw = input("enter password : ")
if pw == "solax":
	print(logog)
else:
	exit()

time.sleep(1)
	




head = {
"Host": "tellonym.me",
"cache-control": "max-age=0",
"accept-language": "ar-AE,ar,en-US,en",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (Linux; Android 10; SAMSUNG SM-A315F) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36",
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
"sec-fetch-site": "none",
"sec-fetch-mode": "navigate",
"sec-fetch-user": "?1",
"sec-fetch-dest": "document",
"accept-encoding": "gzip, deflate, br"
}
list = input("[+] ENTER THE List NAME : ")


def ch():
	cou = 0
	mou = 0
	file = open(list, 'r')
	while True:
		#free tool not for sell
		user = file.readline().split('\n')[0]
		
		url = f"https://tellonym.me/{user}"
	    
		
		if user == "":
			print("""DONE by solax
             token users and available was saved in folders""")
			time.sleep(1)
			input ("press enter to exit[+]:")

			break
		
		req = requests.get(url, headers=head)
		
		if req.status_code == 200:
			cou += 1
			print(Fore.RED + f"[{cou}] user is token  >_< @{user}")
			with open('token.txt','a') as gg:
					gg.write(f"{user}\n")
		
		elif req.status_code == 404:
			mou += 1
			print(Fore.GREEN + f"[{mou}] user is Available @{user}")
			with open('available.txt','a') as gg:
					gg.write(f"{user}\n")
			
		    
check = input("to start check press (y) : ")


if check == "y":
	ch()
elif check == "n":
	print("""
█▀ █▀▀   █▄█ ▄▀█
▄█ ██▄   ░█░ █▀█ """)

connect()
