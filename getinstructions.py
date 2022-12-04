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

dcpins = [33,31] #33 is PWM
control_pins = [32,36,38,40]


GPIO.setup(33, GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.output(33, GPIO.LOW)
GPIO.output(31,GPIO.LOW)

while True:
    data, address = s.recvfrom(4096)
    instructions = data.decode('utf-8')
    instructions = instructions.split(",")
    type = instructions[0]
    value = instructions[1]
    print("Type:", type, "Value:", value)
    if (type == "speed" and value == -1): #reverse
        GPIO.output(31,GPIO.HIGH)
        GPIO.output(33,GPIO.LOW)
    elif (type == "speed" and value == 0):
        GPIO.output(33,GPIO.LOW)
        GPIO.output(31,GPIO.LOW)
