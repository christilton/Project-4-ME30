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
socket.settimeout(0)

control_pins = [32,36,38,40]
control_pins_b = control_pins[::-1]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
GPIO.setup(13, GPIO.OUT, initial = 0)
GPIO.setup(15,GPIO.OUT, initial = 0)

STOPPED = 1
LEFTTURN = 2
RIGHTTURN = 3
steps = 90

STATE = STOPPED

halfstep_seq = [
  [1,0,0,0],
  [1,1,0,0],
  [0,1,0,0],
  [0,1,1,0],
  [0,0,1,0],
  [0,0,1,1],
  [0,0,0,1],
  [1,0,0,1]
]


while True:
    data, address = s.recvfrom(4096)
    instructions = data.decode('utf-8')
    instructions = instructions.split(",")
    type = instructions[0]
    value = instructions[1]
    print("Type:", type, "Value:", value)
    print(steps)
    if (type == "speed" and float(value) == -1): #reverse
        GPIO.output(13,GPIO.HIGH)
        GPIO.output(15,GPIO.LOW)
    elif (type == "speed" and float(value) == 0): #stop
        GPIO.output(13,GPIO.LOW)
        GPIO.output(15,GPIO.LOW)
    elif (type == 'speed' and float(value) > 0): #forward
        GPIO.output(15, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    elif (type == "direction" and value == "left"):
        STATE = LEFTTURN
    elif (type == "direction" and value == "right"):
        STATE = RIGHTTURN
    elif (type == "direction" and value == "none"):
        STATE = STOPPED
    elif (steps == 0 or steps == 180):
        STATE = STOPPED
    if (STATE == RIGHTTURN and steps < 180):
        for halfstep in range(8):
          for pin in range(4):
              GPIO.output(control_pins_b[pin], halfstep_seq[halfstep][pin])
              time.sleep(.0001)
        steps += 1
    elif (STATE == LEFTTURN and steps > 0):
        for halfstep in range(8):
          for pin in range(4):
              GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
              time.sleep(.0001)
        steps -= 1
    elif(STATE == STOPPED):
        pass
    else:
        pass
