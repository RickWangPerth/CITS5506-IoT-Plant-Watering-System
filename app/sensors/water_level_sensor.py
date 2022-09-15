
class WaterLevelSensor:
    def __init__(self, io, pin):
        self.io = io
        self.pin = pin
        io.set_pin_direction(self.pin, 1)  # Set port 1, INPUT
        io.set_pin_pullup(self.pin, 0)
    
    def water_detected(self):
        return bool(self.io.read_pin(self.pin))