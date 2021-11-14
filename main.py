import time
import sys


from Scan import Scanner
from Ping import Pings


def main():

    start_time = float(time.time())

    if sys.argv[1] == "ping": 

        Pings.ping_all(sys.argv[2], sys.argv[3]) # ip_start and ip_end

        end_time = float(time.time())

        print("\n")
        Pings.read_data()

        print(f"\n\nTemps écoulé : {end_time - start_time} secondes.\n")


    elif sys.argv[1] == "scan":

        Scanner.scan_ports(sys.argv[2])

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