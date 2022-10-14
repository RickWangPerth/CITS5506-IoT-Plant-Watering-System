from gpiozero import LED


class Pump:
    def __init__(self, pin):
        """
        @param pin: The pin that the relay for the pump is connected to.
        """
        self.led = LED(pin)
        return

    def on(self):
        """
        Turns the pump on.
        """
        self.led.on()

    def off(self):
        """
        Turns the pump off.
        """
        self.led.off()


if __name__ == "__main__":
    p = Pump(15)
    while True:
        p.off()
        input("Press enter to toggle")
        p.on()
        input("Press enter to toggle")