#!/usr/bin/env python

from __future__ import absolute_import, division, print_function, \
                                                    unicode_literals

import time
import os
import sys

try:
    import ExpanderPi
except ImportError:
    print("Failed to import ExpanderPi from python system path")
    print("Importing from parent folder instead")
    try:
        import sys
        sys.path.append('..')
        import ExpanderPi
    except ImportError:
        raise ImportError(
            "Failed to import library from parent folder")


def main():
    '''
    Main program function
    '''
    adc = ExpanderPi.ADC()  # create an instance of the ADC

    # set the reference voltage.  this should be set to the exact voltage
    # measured on the Expander Pi Vref pin.
    adc.set_adc_refvoltage(4.096)
    
    WATER_LEVEL_PIN = 3
    io = ExpanderPi.IO()
    io.set_pin_direction(WATER_LEVEL_PIN, 1)  # Set port 1, INPUT
    

    
    while True:
        # clear the console
        os.system('clear')
        
        # Temperature sensor
        voltage = adc.read_adc_voltage(1, 0)
        millivolts = 1000.0 * voltage
        kelvin = millivolts / 10.0
        celcius = kelvin - 273.15
        sys.stdout.write('Temperature (C):  %f   \n' % celcius)
        sys.stdout.flush()
        
        # Moisture sensor
        moisture = 100 * adc.read_adc_voltage(2, 0) / 4.096
        sys.stdout.write('Moisture:  %f   \n' % moisture)
        sys.stdout.flush()

        
        # Water level sensor
        water_level = io.read_pin(WATER_LEVEL_PIN)
        sys.stdout.write('Water level:  %s' % water_level + ('HIGH\n' if water_level else 'LOW\n'))
        sys.stdout.flush()
        
        
        sys.stdout.write('\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A')
        sys.stdout.flush()

        time.sleep(0.1)
        

if __name__ == "__main__":
    main()
