import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [32,36,38,40]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

GPIO.setup(13, GPIO.OUT)
GPIO.output(13,0)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15,1)

pos = 0

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

newpins = control_pins[::-1]

for i in range(256):
  for halfstep in range(8):
    for pin in range(4):
        GPIO.output(newpins[pin], halfstep_seq[halfstep][pin])
        time.sleep(.0001)
    pos += .5
    print(pos)
for i in range(256):
  for halfstep in range(8):
    for pin in range(4):
        GPIO.output(control_pins[pin], halfstep_seq[halfstep][pin])
        time.sleep(.0001)
    pos += .5
    print(pos)
GPIO.cleanup()
