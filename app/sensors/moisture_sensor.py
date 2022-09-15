
class MoistureSensor:
    def __init__(self, adc, ref_voltage, pin):
        self.adc = adc
        self.REF_VOLTAGE = ref_voltage
        self.pin = pin
    
    def get_moisture(self):
        return 100 * self.adc.read_adc_voltage(self.pin, 0) / self.REF_VOLTAGE
