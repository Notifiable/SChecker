import requests
import colorama
from colorama import Fore
import os 
colorama.init()

os.system("title SCHECKER ~ [ Snapchat Username Availability Checker ] ~ By: Biscuits")
a = f""" 
{Fore.LIGHTYELLOW_EX}		
		███████╗ ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗███████╗██████╗ 
		██╔════╝██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝██╔════╝██╔══██╗
		███████╗██║     ███████║█████╗  ██║     █████╔╝ █████╗  ██████╔╝
		╚════██║██║     ██╔══██║██╔══╝  ██║     ██╔═██╗ ██╔══╝  ██╔══██╗
		███████║╚██████╗██║  ██║███████╗╚██████╗██║  ██╗███████╗██║  ██║
		╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                           {Fore.LIGHTRED_EX}Made By Biscuits / @netuser on Insta{Fore.RESET}
    """
print(a)

def check():
	Fore.LIGHTCYAN_EX
	username = input(f'{Fore.LIGHTCYAN_EX} Username > ')
	headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept": "*/*",
        "Accept-Language": "en-US,en;q=0.5",
        "Referer": "https://accounts.snapchat.com/",
        "Cookie": "xsrf_token=PlEcin8s5H600toD4Swngg; sc-cookies-accepted=true; web_client_id=b1e4a3c7-4a38-4c1a-9996-2c4f24f7f956; oauth_client_id=c2Nhbg==",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
	}

	url = "https://accounts.snapchat.com/accounts/get_username_suggestions?requested_username={}&xsrf_token=PlEcin8s5H600toD4Swngg".format(username)

	r = requests.post(url, headers=headers)
	data = r.json()

	status = data.get("reference").get("status_code")

	if status == "OK":
		print(f'\n{Fore.LIGHTGREEN_EX} [+] {username.upper()} IS AVAILABLE{Fore.RESET}')
		again = input(f'\n{Fore.LIGHTYELLOW_EX} Do You want to test another username? [y/n]{Fore.RESET} ')
		if again == 'y':
			os.system("cls")
			print(a)
			check()
		else:
			os.system('exit')
	elif status == "TAKEN":
		print(f'\n{Fore.LIGHTRED_EX} [-] {username.upper()} IS NOT AVAILABLE{Fore.RESET}')
		again2 = input(f'\n{Fore.LIGHTYELLOW_EX} Do You want to test another username? [y/n]{Fore.RESET} ')
		if again2 == 'y':
			os.system("cls")
			print(a)
			check()
		else:
			os.system("exit")

check()



