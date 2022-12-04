import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
control_pins = [32,36,38,40]
for pin in control_pins:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin, 0)

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

for i in range(512):
  for halfstep in range(8):
    for pin in range(4):
        GPIO.output(newpins[pin], halfstep_seq[halfstep][pin])
        time.sleep(.0001)
    pos += .5
    print(pos)
GPIO.cleanup()
