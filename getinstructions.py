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


GPIO.setup(13, GPIO.OUT, initial = 0)
GPIO.setup(15,GPIO.OUT, initial = 0)


while True:
    data, address = s.recvfrom(4096)
    instructions = data.decode('utf-8')
    instructions = instructions.split(",")
    type = instructions[0]
    value = instructions[1]
    print("Type:", type, "Value:", value)
    if (type == "speed" and int(value) == -1): #reverse
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.LOW)
    elif (type == "speed" and int(value) == 0): #stop
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
    elif (type == 'speed' and int(value) > 0): #forward
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    elif (type == "direction" and value == "left"):
        pass
    elif (type == "direction" and value == "right"):
        pass
    elif (type == "direction" and value == "none"):
        pass
    else:
        pass
