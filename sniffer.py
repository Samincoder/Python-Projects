import socket
from scapy.all import *

def main():
    # Create a socket to capture raw packets
    sniffer_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    # Specify the network interface to capture packets on
    interface = "eth0"
    sniffer_socket.bind((interface, 0))

    try:
        while True:
            # Receive raw packet data and the sender's address
            raw_data, addr = sniffer_socket.recvfrom(65535)
            
            # Parse the raw packet data using Scapy
            packet = Ether(raw_data)
            
            # Print a summary of the packet
            print(packet.summary())

    except KeyboardInterrupt:
        # Close the socket when the user interrupts the program
        sniffer_socket.close()

if __name__ == "__main__":
    main()
