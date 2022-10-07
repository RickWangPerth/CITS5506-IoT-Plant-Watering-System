from sys import platform
import time
if platform == "linux":
    from app.models import Setting, History


class AutomaticWatering:
    def __init__(self, pump):
        self.water_pump = pump

    def water_plant(self):
        settings: Setting = Setting.query.first()
        self.water_pump.on()
        time.sleep(settings.wateringTime / 1000)
        self.water_pump.off()

    def check_and_water(self):
        data: History = History.query.order_by(History.timestamp.desc()).first()
        settings: Setting = Setting.query.first()

        if data.waterLevel and data.moisture < settings.moisMin:
            self.water_plant()
