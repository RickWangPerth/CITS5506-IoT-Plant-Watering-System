
class TemperatureSensor:
    def __init__(self, adc, pin):
        """
        An analogue LM335Z temperature sensor.
        @param adc: The ABElectronics Expander Pi ADC object
        @param pin: The ADC pin on the Expander Pi the temperature sensor is connected to.
        """
        self.adc = adc
        self.pin = pin
    
    def get_temp(self):
        """
        Gets the current temperature.
        @return: The temperature in °C.
        """
        voltage = self.adc.read_adc_voltage(self.pin, 0)
        millivolts = 1000.0 * voltage
        kelvin = millivolts / 10.0
        celcius = kelvin - 273.15
        return celcius
