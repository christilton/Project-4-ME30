import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.output(13,0)
GPIO.setup(15, GPIO.OUT)
GPIO.output(15,1)
