import sys 

def color_red(text):
    RED = "\033[91m"
    RESET = "\033[0m"
    return f"{RED}{text}{RESET}" 

print(color_red("""  

SELECT PROTOCOL:

"""))

try:
    choice = int(input(color_red("""
    1 - UDP
    2 - TCP
    3 - Back. 
    """)))
    
    if choice == 1:
        import udp_scan
    elif choice == 2:
        import tcp_scan
    elif choice == 3: 
        import main
    else:
        print(color_red("Invalid choice. Please enter 1 - 3."))
except ValueError:
    print(color_red("Invalid input. Please enter a number (1 - 3)."))
