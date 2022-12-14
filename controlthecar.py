from pyPS4Controller.controller import Controller
import socket
#import RPi.GPIO as o

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
address = ('10.245.146.202', 5000)
speed = 0
direction = 0

def send_udp(identifier,val,address):
    instructions = str(identifier + "," + str(val))
    print(instructions)
    sock.sendto(bytes(instructions, 'utf-8'), address)


class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_L2_press(self,value):
        pass

    def on_L2_release(self):
        pass

    def on_R2_press(self,value):
        val = int((value+33000)/660)/100
        send_udp('speed',val,address)

    def on_R2_release(self):
        val = 0
        send_udp('speed',val,address)

    def on_R1_press(self):
        val = -1
        send_udp('speed',val,address)

    def on_R1_release(self):
        val = 0
        send_udp('speed',val,address)

    def on_left_arrow_press(self):
        val = 'left'
        send_udp('direction',val,address)

    def on_right_arrow_press(self):
        val = 'right'
        send_udp('direction',val,address)

    def on_left_right_arrow_release(self):
        val = 'none'
        send_udp('direction',val,address)

    def on_options_press(self):
        val = 'option'
        send_udp('option',val, address)

controller = MyController(interface = '/dev/input/js0', connecting_using_ds4drv=False)

controller.listen(timeout=60)
