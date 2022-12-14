from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
from apscheduler.schedulers.background import BackgroundScheduler
from sys import platform


# Flask app setup
app = Flask(__name__)
app.config["SECRET_KEY"] = '550555055505'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


if platform == "linux":
    from app.sensors.collect_sensors import CollectSensors
    from app.automatic_watering import AutomaticWatering
    import atexit
    from app.pump import Pump

    # Initialise all sensors
    collect_sensors = CollectSensors(db)

    # Set up the watering system
    pump = Pump(15)
    auto_watering = AutomaticWatering(pump)

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=collect_sensors.update_database, trigger="interval", seconds=3)  # Update sensor values regularly
    watering_check_scheduler = scheduler.add_job(func=auto_watering.check_and_water, trigger="interval", seconds=20)  # Check for auto-watering regularly
    scheduler.start()


    def shutdown():
        print("Stopping...")
        collect_sensors.camera.camera.close()  # Close the camera connection on shutdown
        scheduler.shutdown()  # Cancel background tasks (sensor updates and auto-watering)

    # Shut down the scheduler when exiting the app
    atexit.register(shutdown)

from app import models, routes

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Setting=models.Setting, History=models.History)

