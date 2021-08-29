from rpi_rf import RFDevice
from time import sleep


code_on = 16777200
code_off = 16777201

rf_device = RFDevice(17, tx_pulselength=433)
rf_device.enable_tx()

rf_device.tx_code(code_on)
sleep(2)
rf_device.tx_code(code_off)
