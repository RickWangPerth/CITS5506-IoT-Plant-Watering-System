from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
from apscheduler.schedulers.background import BackgroundScheduler
from sys import platform
from app.pump import Pump

app = Flask(__name__)
app.config["SECRET_KEY"] = '550555055505'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


if platform == "linux":
    from app.sensors.collect_sensors import CollectSensors
    import atexit

    collect_sensors = CollectSensors(db)

    scheduler = BackgroundScheduler()
    scheduler.add_job(func=collect_sensors.update_database, trigger="interval", seconds=3)
    scheduler.start()

    pump = Pump(15)

    def shutdown():
        print("Stopping...")
        collect_sensors.camera.camera.close()
        scheduler.shutdown()

    # Shut down the scheduler when exiting the app
    atexit.register(shutdown)

from app import models, routes

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Setting=models.Setting, History=models.History)

