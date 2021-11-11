import sys
import os
import threading
import re


def pingthread(ip, i):

    os.system(f"ping -n 10 {ip[0]}.{ip[1]}.{ip[2]}.{i} > {i}_rslt.txt") # 0 = ok 1 = error

    with open(f"{i}_rslt.txt", "r") as file:

        text = file.read()
        reg = re.search("\sImpossible\sde\sjoindre\s.*de\sdestination\.", text)

        if reg == None:
            print(f"PING REUSSI POUR {ip[0]}.{ip[1]}.{ip[2]}.{i} !")
    

    os.remove(f"{i}_rslt.txt")

"""
def pingthread_enterprise(ip_s, computers):

    print(computers)

    for i in range(0, len(ip_s)):
        if len(ip_s[i]) < 3: 
            ip_s[i] = "0" * (3-len(ip_s[i])) + ip_s[i]

    print(ip_s)

    for i in range(0, computers):

        ip = f"{ip_s[0] + ip_s[1] + ip_s[2] + ip_s[3]}"
        ip = format(int(ip), "b") 
        print(ip)




def ping_enterprise(ip_s, ip_e):

    ip_s = str(ip_s).split("/")[0].split(".")
    ip_e = str(ip_e).split("/")[0].split(".")

    hosts = []

    for byte in range(0, 4):

        hosts.append(int(ip_e[byte]) - int(ip_s[byte]))
                

    computers = (hosts[0] * 255*255*255) + (hosts[1] * 255*255) + (hosts[2] * 255) + hosts[3]
    
    pingthread_enterprise(ip_s, computers)

"""


def ping_all(ip):
    
    ip_range = int(str(ip).split(".")[3])
    ip = str(ip).split(".")

    ip_range = 256 - ip_range


    for i in range(1, ip_range):
        
        thread = threading.Thread(target=pingthread, args=(ip, i))
        thread.start()




def main():
    

    if len(sys.argv) < 3 : 
        print("""
        Commands: 
        - scanICMPlocal (scan ICMP réseau local ipv4)
        - scanICMPenterprise (scan des grosses ip avec un masque)

        (dans le cas du réseau local)
        ip_start sera par exemple : 
        - 192.168.0.1
        - 10.0.0.1
        à noter que cette fonction va tester le delta d'ip entre 256 et le dernier bit donné à l'ip de départ

        (dans le cas du réseau d'entreprise)
        ip de début et ip de fin, exemple:
        - 10.0.0.1 10.0.255.254

        main.py <Command> <ip_start> [<ip_end>]

        !!! (Le program va créer des fichier texts qu'il va ensuite supprimer) !!!
        """)
        return

    
    elif sys.argv[1] == "scanICMPlocal": 
        ip = sys.argv[2]
        ping_all(ip)
"""
    elif sys.argv[1] == "scanICMPenterprise" and len(sys.argv) == 4: 
        ip_s = sys.argv[2]
        ip_e = sys.argv[3]
        ping_enterprise(ip_s, ip_e)
"""



main()