# Import some modules
from os import system
from sys import exit
from time import sleep

# Color Class
class Colours:
    bold = "\033[1m"
    blue = "\033[34m"
    cyan = "\033[36m"
    yellow = "\033[93m"


def mainFunction():
    # Print Banner.
    print(
        f"""{Colours.bold}{Colours.yellow}

    ███    ██ ███████ ████████ ███    ███  █████  ██████  
    ████   ██ ██         ██    ████  ████ ██   ██ ██   ██ 
    ██ ██  ██ █████      ██    ██ ████ ██ ███████ ██████  
    ██  ██ ██ ██         ██    ██  ██  ██ ██   ██ ██      
    ██   ████ ███████    ██    ██      ██ ██   ██ ██ v1.0  
                                                                                
    NETMAP - Network Scanning Tool."""
    )


    print(
        """
            
            -------------------------------------
                Author  : Md. Nur habib
            GitHub  : github.com/thenurhabib
            Twitter : twitter.com/thenurhab1b
            -------------------------------------
            
        """
    )

    # Print Options
    print(
        f"""{Colours.cyan}
            1. TCP syn port scan.
            2. TCP connect port scan.
            3. UDP port scan.
            4. TCP ack port scan.
            5. only port scan.
            6. only host discover.
            7. arp discovery on a local network.
            8. disable DNS resolution.
            9.  scan all ports.
            10. fast port scan.
            11. detect the version of services running.
            12. aggressive scan.
            13. detect operating system of the target.
            14. paranoid IDS evasion.
            15. sneaky IDS evasion.
            16. polite IDS evasion.
            17. normal IDS evasion.
            18. aggressive speed scan.
            19. insane speed scan.
            20. default script scan.
            21. banner grabbing.
            22. use fragmented IP packets.
            23. decoy scans.
            24. use a given source port number.

    """
    )

    try:

        # Take Input From User.
        getInputForScan = str(input(f"\n{Colours.blue}Select a Option : "))

        # execute Nmap commands
        if getInputForScan == "01" or "1":
            domainOrIP1 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -sS {domainOrIP1}")

        elif getInputForScan == "02" or "2":
            domainOrIP2 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -sT {domainOrIP2}")

        elif getInputForScan == "03" or "3":
            domainOrIP3 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -sU {domainOrIP3}")

        elif getInputForScan == "04" or "4":
            domainOrIP4 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -sA {domainOrIP4}")

        elif getInputForScan == "05" or "5":
            domainOrIP5 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -Pn {domainOrIP5}")

        elif getInputForScan == "06" or "6":
            domainOrIP6 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -Sn {domainOrIP6}")

        elif getInputForScan == "07" or "7":
            domainOrIP7 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -PR {domainOrIP7}")

        elif getInputForScan == "08" or "8":
            domainOrIP8 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -n {domainOrIP8}")

        elif getInputForScan == "09" or "9":
            domainOrIP9 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -P-a {domainOrIP9}")

        elif getInputForScan == "10":
            domainOrIP10 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -F {domainOrIP10}")

        elif getInputForScan == "11":
            domainOrIP11 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -sV {domainOrIP11}")

        elif getInputForScan == "12":
            domainOrIP12 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -A {domainOrIP12}")

        elif getInputForScan == "13":
            domainOrIP13 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -O {domainOrIP13}")

        elif getInputForScan == "14":
            domainOrIP14 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -T0 {domainOrIP14}")

        elif getInputForScan == "15":
            domainOrIP15 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -T1 {domainOrIP15}")

        elif getInputForScan == "16":
            domainOrIP16 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -T2 {domainOrIP16}")

        elif getInputForScan == "17":
            domainOrIP17 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -T3 {domainOrIP17}")

        elif getInputForScan == "18":
            domainOrIP18 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -T4 {domainOrIP18}")

        elif getInputForScan == "19":
            domainOrIP19 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -T5 {domainOrIP19}")

        elif getInputForScan == "20":
            domainOrIP20 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap –sC {domainOrIP20}")

        elif getInputForScan == "21":
            domainOrIP21 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap –script banner {domainOrIP21}")

        elif getInputForScan == "22":
            domainOrIP22 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -f {domainOrIP22}")

        elif getInputForScan == "23":
            domainOrIP23 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -D {domainOrIP23}")

        elif getInputForScan == "24":
            domainOrIP2 = input("\nEnter Domain or IP :")
            print("")
            system(f"sudo nmap -g {domainOrIP34}")
        else:
            print("Please Enter a Valid Number.")
            try:
                system("python3 netmap.py")
            except:
                system("python netmap.py")
                

    except Exception:
        print("Something was wrong.")


if __name__ == '__main__':
    mainFunction()
    