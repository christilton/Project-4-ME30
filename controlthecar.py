from pyPS4Controller.controller import Controller
import socket
#import RPi.GPIO as o

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ('10.245.148.78', 5000)
speed = 0
direction = 0

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L2_press(self,value):
        pass

    def on_L2_release(self):
        pass

    def on_R2 Press(self,value):
        speed = int((value+33000)/660)

    def on_R2_release(self):
        speed = 0

    def on_R1_press(self):
        speed = -1

    def on_R1_release(self):
        speed = 0

    def on_left_arrow_press(self):
        direction = 'left'

    def on_right_arrow_press(self):
        direction = 'right'

controller = MyController(interface = '/dev/input/js0', connecting using ds4drv=False)

while True:
    controller.listen(timeout=60)
    instructions = str(speed) + "," + str(direction)
    print(instructions)
    sock.sendto(bytes(instructions), 'utf-8', address)
