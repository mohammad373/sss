# sss

import os
import time
import sys
import socket
import requests
from colorama import Fore

def __target__():
    os.system("clear")
    time.sleep(1)
    print(Fore.YELLOW + "Hi , My Name Is Bobot ;))")
    time.sleep(1)
    target = input(Fore.YELLOW + "\n[!] ~ " + Fore.BLUE + "Pleass Enter Domain" + Fore.GREEN + " ==>  ")
    time.sleep(1)
    if target == "" or None:
        try:
            print(Fore.RED + "[-] ~ Error : Your Domain Is None ;(")
            time.sleep(1)
            sys.exit()
        except:
            sys.exit()
    if not "http://" in target or not "https://" in target:
        target = "http://" + target
    r1 = requests.get(target)
    if r1.status_code == 200:
        print(Fore.GREEN + "[+] ~ Your Domain Is Found ;))")
    else:
        try:
            time.sleep(1)
            print(Fore.RED + "[-} ~ Error : Your Domain Is Not Found ;(")
            time.sleep(0.5)
            sys.exit()
        except:
            sys.exit()
    my_list = ["admin","ADMIN","Admin","admin/login","ADMIN/LOGIN","Admin/Login","adminlogin","AdminLogin","ADMINLOGIN","pass/admin","PASS/ADMIN","Pass/Admin","admin/pass","ADMIN/PASS","Admin/Pass","adminpass"]
    for i in my_list:
        r2 = target + "/" + i
        r3 = requests.get(r2)
        if r3.status_code == 200:
            print(Fore.GREEN + "[+] ~ " + Fore.GREEN + r2)
        else:
            print(Fore.RED + "[-] ~ " + Fore.RED + r2)
__target__()
