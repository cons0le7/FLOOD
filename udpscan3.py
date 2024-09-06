import socket

def color_red(text):
    RED = "\033[91m"
    RESET = "\033[0m"
    return f"{RED}{text}{RESET}"

print(color_red("""  _    _ _____  _____     _____  _____          _   _ 
 | |  | |  __ \|  __ \   / ____|/ ____|   /\   | \ | |
 | |  | | |  | | |__) | | (___ | |       /  \  |  \| |
 | |  | | |  | |  ___/   \___ \| |      / /\ \ | . ` |
 | |__| | |__| | |       ____) | |____ / ____ \| |\  |
  \____/|_____/|_|      |_____/ \_____/_/    \_\_| \_|
                                                      
                                                      
 """))

def scan_udp_port(target_ip, port):

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(2) 

        message = b"Ping!"
        sock.sendto(message, (target_ip, port))

        try:
            response, addr = sock.recvfrom(1024)
            print(color_red(f"Port {port} is open."))
        except socket.timeout:
            print(color_red(f"Port {port} is closed or filtered."))

    except Exception as e:
        print(f"Error scanning port {port}: {e}")

    finally:
        sock.close()

target_ip = input(color_red("Enter target IP: "))
ports_input = input(color_red("Enter ports to scan (comma-separated): "))
ports_to_scan = [int(port.strip()) for port in ports_input.split(",")]

for port in ports_to_scan:
    scan_udp_port(target_ip, port)
