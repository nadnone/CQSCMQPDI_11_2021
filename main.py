import time
import sys
import os
import threading
import re
import ipaddress
from ping3 import ping

def pingthread(ip, file):

    ms = ping(f"{ip}", unit="ms", timeout=1)
    file.write(f"ip: {ip} -> {ms}\n")


def ping_all(ip, ip_e):
    
    os.remove("ip_list.txt")
    file = open("ip_list.txt", "a")

    value = ipaddress.ip_address(ip)
    ip_e = ipaddress.ip_address(ip_e)
    threads = []

    while True:

        thread = threading.Thread(target=pingthread, args=(value, file))
        thread.start()
        threads.append(thread)

        value+=1

        if value >= ip_e:
            break    

    for i in range(0, len(threads)):

        threads[i].join()
        
    file.close()

def read_data():

    file = open("ip_list.txt", "r")
    data = file.read()

    reg = re.findall("ip\:\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s\-\>\s([0-9]+)\.[0-9]+", data)
    

    for ip in reg:
        print(f"IP: {ip[0]} a répondu avec {ip[1]} millisecondes")


def main():

    if len(sys.argv) < 4 : 
        print("""
        Commands: 
        - ping

        ./main.py <Command> <ip_start> [<ip_end>]

        """)
        return

    
    elif sys.argv[1] == "ping": 

        start_time = int(time.time())

        ping_all(sys.argv[2], sys.argv[3]) # ip_start and ip_end

        end_time = int(time.time())

        print("\n")
        read_data()

        print(f"\n\nTemps écoulé : {end_time - start_time} secondes.\n")



main()