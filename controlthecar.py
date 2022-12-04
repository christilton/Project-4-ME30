from pyPS4Controller.controller import Controller
import socket
#import RPi.GPIO as o

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ('10.245.148.78', 5000)

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
