import os
from flask import render_template,request, flash, redirect, session, url_for
from app import app, db
from app.models import Setting, History
from sys import platform
import time
import json
if platform == "linux":
    from app import collect_sensors, scheduler, pump

camera_schedule_job = None

@app.before_first_request
def start_camera():
    """
    Starts the camera and initialises settings when the Flask server starts.
    """
    print("Running")
    if platform == "linux":
        global camera_schedule_job

        # Initialise settings if they are not yet set (first time startup)
        setting = Setting.query.first()
        if setting is None:
            setting = Setting(
                id = 1,
                moisMin = 20,
                moisMax = 95,
                tempMin  = 5,
                tempMax = 35,
                lightMax = 1000,
                lightMin = 0,
                wateringTime = 500,
                pictureFrequency = 15)
            db.session.add(setting)
            db.session.commit()

        collect_sensors.camera.save_picture()

        frequency = setting.pictureFrequency if setting.pictureFrequency is not None else 2
        camera_schedule_job = scheduler.add_job(func=collect_sensors.camera.save_picture, trigger="interval", hours=frequency)


@app.route('/')
@app.route('/index/')
def index():
    """
    The home page.
    """
    # Get latest data from the database
    history = History.query.order_by(History.timestamp.desc()).first()
    setting = Setting.query.first()

    # Return defaults if required.
    if history is None and setting is None:
        return render_template("index.html", data={'moisture': "null", 'temperature': "null", \
        'light': "null", 'updateTime': "null", 'waterLevel': "null", 'moisMin': 20, \
        'moisMax': 95, 'tempMin': 5, 'tempMax': 35, \
        'lightMax': 1000, 'lightMin':5, 'wateringTime': 500,'pictureFrequency': 15}, title="Dashboard")
    if history is not None and setting is None:
        return render_template("index.html", data={'moisture': history.moisture, 'temperature': history.temperature, \
        'light': history.light, 'updateTime': history.timestamp.timestamp(), 'waterLevel': int(history.waterLevel), 'moisMin': 20, \
        'moisMax': 95, 'tempMin': 5, 'tempMax': 35, \
        'lightMax': 1000, 'lightMin':5, 'wateringTime': 500,'pictureFrequency': 15}, title="Dashboard")
    if history is None and setting is not None:
        return render_template("index.html", data={'moisture': "null", 'temperature': "null", \
        'light': "null", 'updateTime': "null", 'waterLevel': "null", 'moisMin': setting.moisMin, \
        'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
        'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime, 'pictureFrequency': setting.pictureFrequency}, title="Dashboard")

    # Render the page using the retrieved data
    return render_template("index.html", data={'moisture': history.moisture, 'temperature': history.temperature, \
    'light': history.light, 'updateTime': history.timestamp.timestamp(),'waterLevel': int(history.waterLevel), 'moisMin': setting.moisMin, \
    'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
    'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime, 'pictureFrequency': setting.pictureFrequency}, title="Dashboard")


@app.route('/historical/')
def historical():
    """
    The historical data page.
    """
    moisData = []
    tempData = []
    lightData = []
    ## Modified in 07/10/2022 BY LEON
    timeStamp = []
    moisAlert = []
    tempAlert = []
    lightAlert = []

    entries = History.query.order_by(History.timestamp).all()
    if entries is None:
        return render_template("historical.html", data={'moisData': moisData, 'tempData': tempData, \
        'lightData': lightData, 'timeStamp': timeStamp, 'moisAlert': moisAlert, 'tempAlert': tempAlert, \
        'lightAlert': lightAlert}, title="Historical Data")
    # Create a list for each of the sensors
    for entry in entries:
        moisData.append(entry.moisture)
        tempData.append(entry.temperature)
        lightData.append(entry.light)
        ## Modified in 07/10/2022 BY LEON
        timeStamp.append(entry.timestamp.timestamp())
        moisAlert.append(entry.moistureAlert)
        tempAlert.append(entry.temperatureAlert)
        lightAlert.append(entry.lightAlert)

    return render_template("historical.html", data={'moisData': moisData, 'tempData': tempData, \
    'lightData': lightData, 'timeStamp': timeStamp, 'moisAlert': moisAlert, 'tempAlert': tempAlert, \
        'lightAlert': lightAlert}, title="Historical Data")

@app.route('/advance', methods=['GET', 'POST'])
def advance():
    """
    The advanced settings page
    """
    # Get the current settings
    setting = Setting.query.first()
    if setting is None:
        return render_template('advance.html', data={'moisMin': 20, \
        'moisMax': 95, 'tempMin': 5, 'tempMax': 35, \
        'lightMax': 1000, 'lightMin':5, 'wateringTime': 500,'pictureFrequency': 15}, Title="Default Settings")

    # Return the page with the current settings
    return render_template('advance.html', data={'moisMin': setting.moisMin, \
    'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
    'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime, 'pictureFrequency': setting.pictureFrequency}, Title="Advanced Settings")

@app.route('/Setting', methods=["POST"])
def store_Setting():
    """
    A POST route to store the current settings.
    Payload should include moisMin, moisMax, tempMin, tempMax, lightMax, lightMin, wateringTime and pictureFrequency.
    @return: The new settings as a dictionary (JSON).
    """
    id = request.json.get("id")
    moisMin = request.json.get("moisMin")
    moisMax = request.json.get("moisMax")
    tempMin = request.json.get("tempMin")
    tempMax = request.json.get("tempMax")
    lightMax = request.json.get("lightMax")
    lightMin = request.json.get("lightMin")
    wateringTime = request.json.get("wateringTime")
    pictureFrequency = request.json.get("pictureFrequency")
    print(request.json, 'sss')

    setting = Setting.query.first()
    if setting is None:
        # add default settings
        setting = Setting(
        id = 1,
        moisMin = 20,
        moisMax = 95,
        tempMin  = 5,
        tempMax = 35,
        lightMax = 1000,
        lightMin = 0,
        wateringTime = 500,
        pictureFrequency = 15)
        db.session.add(setting)
        db.session.commit()
    else:
        # Store the new settings
        db.session.commit()
        setting.moisMin = moisMin
        setting.moisMax = moisMax
        setting.tempMin = tempMin
        setting.tempMax = tempMax
        setting.lightMin = lightMin
        setting.lightMax = lightMax
        setting.wateringTime = wateringTime
        setting.pictureFrequency = pictureFrequency
        db.session.commit()

    # Reschedule the regular pictures based on the new settings
    camera_schedule_job.reschedule(trigger="interval", hours=pictureFrequency)
    return setting.to_dict()

@app.route('/latest_picture/', methods=["GET"])
def get_latest_picture():
    """
    Returns the path of the latest image.
    @return: {'image_path': <image_path>}
    """
    return {'image_path': "/" + collect_sensors.camera.latest_image.split("app/")[1]}, 200

@app.route('/take_picture/', methods=["GET"])
def take_picture():
    """
    Takes a picture and saves it.
    @return: {'image_path': <image_path>}
    """
    collect_sensors.camera.save_picture()
    return get_latest_picture()

@app.route('/water_plant/', methods=["GET"])
def water_plant_fixed():
    """
    Waters the plant for the amount specified by the settings.
    @return: {'success': True}
    """
    settings: Setting = Setting.query.first()
    pump.on()
    time.sleep(settings.wateringTime/1000)
    pump.off()
    return {'success': True}, 200

@app.route('/get_data')
def get_data():
    """
    Gets the most recent sensor data.
    @return: The sensor data as a JSON object.
    """
    entry = History.query.order_by(History.timestamp.desc()).first()
    if entry is None:
        x = {'moisture': None, 'temperature': None, \
        'light': None, 'waterLevel': 1, 'updateTime': None}
        return json.dumps(x)
    x = {'moisture': entry.moisture, 'temperature': entry.temperature, \
    'light': entry.light, 'waterLevel': entry.waterLevel, 'updateTime': entry.timestamp.timestamp()}
    return json.dumps(x)
