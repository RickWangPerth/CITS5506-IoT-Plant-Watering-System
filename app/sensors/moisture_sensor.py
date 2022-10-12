
class MoistureSensor:
    def __init__(self, adc, ref_voltage, pin):
        """
        An analogue soil moisture sensor.

        @param adc: The ABElectronics Expander Pi ADC object
        @param ref_voltage: The analogue reference voltage.
        @param pin: The ADC pin on the Expander Pi the moisture sensor is connected to.
        """
        self.adc = adc
        self.REF_VOLTAGE = ref_voltage
        self.pin = pin
    
    def get_moisture(self):
        """
        Gets the current moisture value.
        @return: The current moisture as a percentage (0-100).
        """
        return 100 * self.adc.read_adc_voltage(self.pin, 0) / self.REF_VOLTAGE
