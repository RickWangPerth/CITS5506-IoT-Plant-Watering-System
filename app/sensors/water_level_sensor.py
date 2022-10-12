
class WaterLevelSensor:
    def __init__(self, io, pin):
        """
        A SEN0205 Liquid level sensor.

        @param io: The Expander Pi digital IO object.
        @param pin: The digital pin on the Expander Pi the sensor is connected to.
        """
        self.io = io
        self.pin = pin
        io.set_pin_direction(self.pin, 1)  # Set port 1, INPUT
        io.set_pin_pullup(self.pin, 0)
    
    def water_detected(self):
        """
        Returns whether there is water detected.
        @return: True if water detected, false otherwise.
        """
        return bool(self.io.read_pin(self.pin))