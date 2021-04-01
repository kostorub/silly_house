import time
from adafruit_blinka.microcontroller.bcm283x.pin import Pin
from adafruit_dht import DHT22 as DHT


class DHT22(DHT):
    def __init__(self, bcm_pin, name, phrase):
        super(DHT22, self).__init__(Pin(bcm_pin))
        self.pin = MockPin(bcm_pin)
        self.name = name
        self.phrase = phrase

    def status(self):
        try:
            temperature = self.temperature
            humidity = self.humidity
            return self.temperature, self.humidity
        except Exception:
            return -1, -1

class MockPin:
    def __init__(self, pin):
        self.number = pin
