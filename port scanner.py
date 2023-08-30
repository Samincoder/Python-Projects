import socket
import subprocess
from datetime import datetime

# Clear the terminal screen
subprocess.call('clear', shell=True)

# Get target information from the user
target = input("Enter the target IP address or hostname: ")

def port_scan(target):
    try:
        # Resolve the target's IP address
        ip = socket.gethostbyname(target)

        # Print scan information
        print("-" * 50)
        print("Scanning target:", ip)
        print("Time started:", datetime.now())
        print("-" * 50)

        # Loop through ports and check if they are open
        for port in range(1, 65635):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)  # Set a timeout for the connection attempt
            result = sock.connect_ex((ip, port))
            if result == 0:
                print("Port {}: Open".format(port))
            sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")

    except socket.error:
        print("Could not connect to the server.")

# Call the port_scan function with the user-provided target
port_scan(target)
