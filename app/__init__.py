from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.config["SECRET_KEY"] = '550555055505'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app import routes, models
from app.sensors.collect_sensors import CollectSensors
import atexit

sensors = CollectSensors(db)

def update_sensors():
    print(sensors.get_current())
    time.sleep(1)


scheduler = BackgroundScheduler()
scheduler.add_job(func=update_sensors, trigger="interval", seconds=3)
scheduler.start()

# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Setting=models.Setting, History=models.History)

