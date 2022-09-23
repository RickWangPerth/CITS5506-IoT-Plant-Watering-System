from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
from apscheduler.schedulers.background import BackgroundScheduler
from sys import platform

app = Flask(__name__)
app.config["SECRET_KEY"] = '550555055505'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models

if platform == "linux":
    from app.sensors.collect_sensors import CollectSensors
    import atexit

    sensors = CollectSensors(db)


    scheduler = BackgroundScheduler()
    scheduler.add_job(func=sensors.update_database, trigger="interval", seconds=3)
    scheduler.start()

    # Shut down the scheduler when exiting the app
    atexit.register(lambda: scheduler.shutdown())


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Setting=models.Setting, History=models.History)

