import time
import sys


from scan import Scanner
from ping import Pings



def main():

    

    
    if sys.argv[1] == "ping": 

        start_time = float(time.time())

        Pings.ping_all(sys.argv[2], sys.argv[3]) # ip_start and ip_end

        end_time = float(time.time())

        print("\n")
        Pings.read_data()

        print(f"\n\nTemps écoulé : {end_time - start_time} secondes.\n")


    elif sys.argv[1] == "scan":

        start_time = float(time.time())

        Scanner.scan_ports(sys.argv[2]) # ip_start and ip_end

        end_time = float(time.time())

        print("\n")
        Scanner.read_data()

        print(f"\n\nTemps écoulé : {end_time - start_time} secondes.\n")


    else: 
        print("""
        Commands: 
        - ./main.py ping <ip_start> <ip_end>
        - ./main.py scan <ip>

        """)


main()