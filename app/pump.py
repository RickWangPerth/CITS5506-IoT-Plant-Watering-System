from gpiozero import LED

class Pump:
    def __init__(self, pin):
        self.led = LED(pin)
        return

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

if __name__ == "__main__":
    p = Pump(15)
    while True:
        p.off()
        input("Press enter to toggle")
        p.on()
        input("Press enter to toggle")