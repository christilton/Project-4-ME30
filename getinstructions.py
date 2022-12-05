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
s.settimeout(0.0)
instructions = [0,0]

control_pins = [32,36,38,40]
control_pins_b = control_pins[::-1]

for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)
GPIO.setup(33, GPIO.OUT, initial = 0) #PWM
GPIO.setup(15,GPIO.OUT, initial = 0)
p = GPIO.PWM(33,5000)
p.start(0)

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

def handle_movement(instructions,STATE,control_pins,control_pins_b,halfstep_seq):
    type = instructions[0]
    value = instructions[1]
    print("Type:", type, "Value:", value)
    if (type == "speed" and float(value) == -1): #reverse
        GPIO.output(15,GPIO.HIGH)
        p.ChangeDutyCycle(0)
    if (type == "speed" and float(value) == 0): #stop
        GPIO.output(15,GPIO.LOW)
        p.ChangeDutyCycle(0)
    if (type == 'speed' and float(value) > 0): #forward
        speedmod = float(value)
        dc = 100*speedmod
        p.ChangeDutyCycle(dc)
    if (type == "direction" and value == "left"):
        STATE = LEFTTURN
    if (type == "direction" and value == "right"):
        STATE = RIGHTTURN
    if (type == "direction" and value == "none"):
        STATE = STOPPED
    if (STATE == RIGHTTURN):
        for halfstep in range(8):
          for pin in range(4):
              GPIO.output(control_pins_b[pin], halfstep_seq[halfstep][pin])
              time.sleep(.0001)
        #steps += 1
    if (STATE == LEFTTURN):
        for halfstep in range(8):
          for pin in range(4):
              GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
              time.sleep(.0001)
        #steps -= 1
    if(STATE == STOPPED):
        pass
    else:
        pass

while True:
    try:
        data, address = s.recvfrom(4096, socket.MSG_DONTWAIT)
        instructions = data.decode('utf-8')
        instructions = instructions.split(",")
        handle_movement(instructions,STATE,control_pins,control_pins_b,halfstep_seq)

    except BlockingIOError:
        handle_movement(instructions,STATE,control_pins,control_pins_b,halfstep_seq)

    except KeyboardInterrupt:
        GPIO.cleanup()
        p.stop()
