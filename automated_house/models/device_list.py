class DeviceList:
    def __init__(self, devices=[]):
        self.devices = devices
    
    def __getitem__(self, value):
        for device in self.devices:
            if isinstance(value, str):
                if device.name == value:
                    return device
            if isinstance(value, int):
                try:
                    if device.pin.number == value:
                        return device
                except:
                    pass
                try:
                    if device.id == value:
                        return device
                except:
                    pass
        else:
            raise NoDevice(f"No device found on this pin: {value}")
    
    def __iter__(self):
        return iter(self.devices)

    def append(self, value):
        self.devices.append(value)
    
    def extend(self, value):
        self.devices.extend(value)

    def find_similar_phrase(self, text):
        phrases = text.split()
        for device in self.devices:
            if all(phrase in device.phrase_on for phrase in phrases):
                return device, True
            if all(phrase in device.phrase_off for phrase in phrases):
                return device, False
        return None, False

    def __len__(self):
        return len(self.devices)

class NoDevice(Exception):
    def __init__(self, message):
        self.message = message

if __name__ == "__main__":
    devices = DeviceList()
    print(devices[1])