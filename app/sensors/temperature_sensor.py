
class TemperatureSensor:
    def __init__(self, adc, pin):
        self.adc = adc
        self.pin = pin
    
    def get_temp(self):
        voltage = self.adc.read_adc_voltage(self.pin, 0)
        millivolts = 1000.0 * voltage
        kelvin = millivolts / 10.0
        celcius = kelvin - 273.15
        return celcius
