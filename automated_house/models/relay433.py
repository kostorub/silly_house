from rpi_rf import RFDevice
from models.dht22 import MockPin

rf_device = RFDevice(17, tx_pulselength=433)
rf_device.enable_tx()


class Relay433:
    id = 0

    def __init__(self, code_on, code_off, name, phrase_on, phrase_off):
        Relay433.id += 1
        self.pin = MockPin(433 + Relay433.id)
        self.code_on = code_on
        self.code_off = code_off
        self.phrase_on = phrase_on
        self.phrase_off = phrase_off
        self.name = name
        self.off()
        self.is_active = False

    def on(self):
        rf_device.tx_code(self.code_on)
        self.is_active = True
        print(self)

    def off(self):
        rf_device.tx_code(self.code_off)
        self.is_active = False
        print(self)

    def is_active():
        return self.is_active

    def __repr__(self):
        return f"{self.name} {self.is_active}"