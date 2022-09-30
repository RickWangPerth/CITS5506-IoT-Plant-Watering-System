from gpiozero import LED

class Pump:
    def __init__(self):
        self.led = LED(15)
        return

    def on(self):
        self.led.on()

    def off(self):
        self.led.off()

if __name__ == "__main__":
    p = Pump()
    while True:
        p.off()
        input("Press enter to toggle")
        p.on()
        input("Press enter to toggle")