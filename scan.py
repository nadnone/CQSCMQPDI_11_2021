import socket
import threading
import re

class Scanner:

    def port_check_thread(file, ip, port):

        try:

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.04)
            rslt = sock.connect((str(ip), port))

            if rslt == None:
                file.write(f"ip: {str(ip)} -> PORT: {str(port)} OUVERT\n")
            
        except:
            pass

        finally:
            sock.close()


    def scan_ports(ip):


        open("ports_scan_rslt.txt", "w").close()

        file = open("ports_scan_rslt.txt", "a")

        threads = []
        

        for port in range(1, 65535): # quelques ports usuels, vous pouvez en ajouter
            thread = threading.Thread(target=Scanner.port_check_thread, args=(file, ip, port))
            thread.start()
            threads.append(thread)

        for i in range(0, len(threads)):

            threads[i].join()
            
        file.close()
            


    def read_data():

        file = open("ports_scan_rslt.txt", "r", encoding="utf-8")
        data = file.read()

        # check si ports success
        reg = re.findall("ip\:\s([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)\s\-\>\sPORT:\s([0-9]+)\sOUVERT", data)
        for d in reg:
            print(f"IP: {d[0]} a répondu avec le port: {d[1]}")



