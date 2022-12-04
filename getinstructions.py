import socket
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

IP = '0.0.0.0'  # Receive any incoming UDP packet on this port
PORT = 5000  #Example port
ADDRESS = (IP, PORT)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(ADDRESS)

dcpins = [7,11] #33 is PWM
control_pins = [32,36,38,40]


GPIO.setup(7, GPIO.OUT, initial = 0)
GPIO.setup(11,GPIO.OUT, initial = 0)


while True:
    data, address = s.recvfrom(4096)
    instructions = data.decode('utf-8')
    instructions = instructions.split(",")
    type = instructions[0]
    value = instructions[1]
    print("Type:", type, "Value:", value)
    if value == -1: #reverse
        GPIO.output(7,GPIO.HIGH)
        GPIO.output(11,GPIO.LOW)
    elif value == 0:
        GPIO.output(7,GPIO.LOW)
        GPIO.output(11,GPIO.LOW)
    else:
        pass
    print(GPIO.input(7))
