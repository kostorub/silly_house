from gpiozero import DigitalInputDevice
from signal import pause
from time import time

def say_hello():
    print(time(), " activated!")

def say_goodbye():
    print(time(), " deactivated!")

mq = DigitalInputDevice(10)

mq.when_activated = say_hello
mq.when_deactivated = say_goodbye

pause()