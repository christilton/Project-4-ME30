import socket

IP = '0.0.0.0'  # Receive any incoming UDP packet on this port
PORT = 5000  #Example port
ADDRESS = (IP, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDRESS)

while True:
    data, address = s.recvfrom(4096)
    print("Received: ", data.decode('utf-8'), "\n")

# You can also still send UDP packets from the socket, even if it's bound already.
