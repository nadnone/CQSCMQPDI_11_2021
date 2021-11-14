import socket
import threading
import re
import ipaddress
from ping3 import ping

class Pings:
        
    def pingthread(ip, file):

        ms = ping(f"{ip}", unit="ms", timeout=1)

        if ms != None:
            file.write(f"ip: {ip} -> {ms}\n")

        else:

            for port in [80, 443, 21, 43, 22, 25, 587, 465, 143, 8080]: # quelques ports usuels, vous pouvez en ajouter
                try:

                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.settimeout(0.04)
                    rslt = sock.connect((str(ip), port))

                    if rslt == None:
                        file.write(f"ip: {str(ip)} -> PORT: {str(port)} OUVERT\n")
                        break
                        
                except:
                    pass

                finally:
                    sock.close()






    def ping_all(ip, ip_e):

        open("ip_list.txt", "w").close()

        file = open("ip_list.txt", "a", encoding="utf-8")

        value = ipaddress.ip_address(ip)
        ip_e = ipaddress.ip_address(ip_e)
        threads = []

        while True:

            thread = threading.Thread(target=Pings.pingthread, args=(value, file))
            thread.start()
            threads.append(thread)

            value+=1

            if value >= ip_e:
                break    

        for i in range(0, len(threads)):

            threads[i].join()
            
        file.close()






    def read_data():

        file = open("ip_list.txt", "r", encoding="utf-8")
        data = file.read()

        # check si ping success
        reg = re.findall("ip\:\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s\-\>\s([0-9]+)\.[0-9]+", data)
        for ip in reg:
            print(f"IP: {ip[0]} a répondu avec {ip[1]} millisecondes")

        # check si ports success
        reg = re.findall("ip\:\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s\-\>\sPORT:\s([0-9]+)\sOUVERT", data)
        for d in reg:
            print(f"IP: {d[0]} a répondu avec le port: {d[1]}")




