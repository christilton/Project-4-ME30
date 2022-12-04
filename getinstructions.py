import socket

IP = '0.0.0.0'  # Receive any incoming UDP packet on this port
PORT = 5000  #Example port
ADDRESS = (IP, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDRESS)

while True:
    data, address = s.recvfrom(4096)
    instructions = data.decode('utf-8')
    instructions = instructions.split(",")
    type = instructions[0]
    value = instructions[1]
    print("Type:", type, "Value:", value)
