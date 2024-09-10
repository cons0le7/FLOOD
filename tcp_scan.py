import sys
from scapy.all import *

def color_red(text):
    RED = "\033[91m"
    RESET = "\033[0m"
    return f"{RED}{text}{RESET}"
    
def color_green(text):
    GREEN = "\033[32m" 
    RESET = "\033[0m"
    return f"{GREEN}{text}{RESET}"
    
    
print(color_red(""" 
  _______ _____ _____     _____  _____          _   _ 
 |__   __/ ____|  __ \   / ____|/ ____|   /\   | \ | |
    | | | |    | |__) | | (___ | |       /  \  |  \| |
    | | | |    |  ___/   \___ \| |      / /\ \ | . ` |
    | | | |____| |       ____) | |____ / ____ \| |\  |
    |_|  \_____|_|      |_____/ \_____/_/    \_\_| \_|
                                                                                        
"""))
    
def syn_scan(target_ip, port_list):

    open_ports = []

    for port in port_list:

        syn_packet = IP(dst=target_ip)/TCP(dport=port, flags='S')

        response = sr1(syn_packet, timeout=1, verbose=0)

        

        if response is None:

            print(color_red(f"Port {port} is closed or filtered (no response)"))

        elif response.haslayer(TCP):

            if response[TCP].flags == 0x12:

                print(color_green(f"Port {port} is open"))

                open_ports.append(port)

                rst_packet = IP(dst=target_ip)/TCP(dport=port, flags='R')

                send(rst_packet, verbose=0)

            elif response[TCP].flags == 0x14:

                print(color_red(f"Port {port} is closed"))

    return open_ports


common_ports = [22, 80, 443, 21, 25, 53, 110, 143, 3306, 8080]


target = input(color_red("Enter the target IP address: "))

ports_input = input(color_red("Enter ports to scan separated by commas (or type '?' for common ports): "))


if ports_input.strip() == '?':

    port_list = common_ports

else:

    port_list = [int(port.strip()) for port in ports_input.split(',')]


print(color_red(f"Scanning {target} for open ports: {port_list}..."))

open_ports = syn_scan(target, port_list)


if open_ports:

    print(color_green(f"Open ports: {open_ports}"))

else:

    print(color_red("No open ports found."))
    
    
complete_choice = input("Scan complete. Open flood tool? (y/n): ") 

if complete_choice == 'y': 
    import  tcp_flood 
elif complete_choice == 'n': 
    sys.exit() 
else:
    print(color_red("Invalid choice. Please y or n."))
    

