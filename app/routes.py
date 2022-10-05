import os
from flask import render_template,request, flash, redirect, session, url_for
from app import app, db
from app.models import Setting, History
from sys import platform
import time
if platform == "linux":
    from app import collect_sensors, scheduler, pump

camera_schedule_job = None

@app.before_first_request
def start_camera():
    print("Running")
    if platform == "linux":
        global camera_schedule_job
        setting = Setting.query.first()
        if setting is None:
            setting = Setting(
                id = 1,
                moisMin = 20,
                moisMax = 50,
                tempMin  = 5,
                tempMax = 35,
                lightMax = 1000,
                lightMin = 0,
                wateringTime = 2,
                pictureFrequency = 2)
            db.session.add(setting)
            db.session.commit()

        collect_sensors.camera.save_picture()

        frequency = setting.pictureFrequency if setting.pictureFrequency is not None else 2
        camera_schedule_job = scheduler.add_job(func=collect_sensors.camera.save_picture, trigger="interval", hours=frequency)


@app.route('/')
@app.route('/index/')
def index():
    history = History.query.order_by(History.timestamp.desc()).first()
    setting = Setting.query.first()
    if history is None and setting is None:
        return render_template("index.html", data={'moisture': "null", 'temperature': "null", \
        'light': "null", 'updateTime': "null", 'waterLevel': "null", 'moisMin': 20, \
        'moisMax': 50, 'tempMin': 5, 'tempMax': 35, \
        'lightMax': 1000, 'lightMin':5, 'wateringTime': 60,'pictureFrequency': 60}, title="Dashboard")
    if history is not None and setting is None:
        return render_template("index.html", data={'moisture': history.moisture, 'temperature': history.temperature, \
        'light': history.light, 'updateTime': history.timestamp.timestamp(), 'waterLevel': int(history.waterLevel), 'moisMin': 20, \
        'moisMax': 50, 'tempMin': 5, 'tempMax': 35, \
        'lightMax': 1000, 'lightMin':5, 'wateringTime': 60,'pictureFrequency': 60}, title="Dashboard")
    if history is None and setting is not None:
        return render_template("index.html", data={'moisture': "null", 'temperature': "null", \
        'light': "null", 'updateTime': "null", 'waterLevel': "null", 'moisMin': setting.moisMin, \
        'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
        'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime, 'pictureFrequency': setting.pictureFrequency}, title="Dashboard")

    return render_template("index.html", data={'moisture': history.moisture, 'temperature': history.temperature, \
    'light': history.light, 'updateTime': history.timestamp.timestamp(),'waterLevel': int(history.waterLevel), 'moisMin': setting.moisMin, \
    'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
    'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime, 'pictureFrequency': setting.pictureFrequency}, title="Dashboard")


@app.route('/historical/')
def historical():
    moisData = []
    tempData = []
    lightData = []
    entries = History.query.order_by(History.timestamp).all()
    if entries is None:
        return render_template("historical.html", data={'moisData': moisData, 'tempData': tempData, \
        'lightData': lightData}, title="Historical Data")
    for entry in entries:
        moisData.append(entry.moisture)
        tempData.append(entry.temperature)
        lightData.append(entry.light)
    return render_template("historical.html", data={'moisData': moisData, 'tempData': tempData, \
    'lightData': lightData}, title="Historical Data")

@app.route('/advance', methods=['GET', 'POST'])
def advance():
    setting = Setting.query.first()
    if setting is None:
        return render_template('advance.html', data={'moisMin': 20, \
        'moisMax': 50, 'tempMin': 5, 'tempMax': 35, \
        'lightMax': 1000, 'lightMin':5, 'wateringTime': 60,'pictureFrequency': 60}, Title="Default Settings")

    return render_template('advance.html', data={'moisMin': setting.moisMin, \
    'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
    'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime, 'pictureFrequency': setting.pictureFrequency}, Title="Advanced Settings")

@app.route('/Setting', methods=["POST"])
def store_Setting():
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
        # add defalut setting
        setting = Setting(
        id = 1,
        moisMin = 20,
        moisMax = 50,
        tempMin  = 5,
        tempMax = 35,
        lightMax = 1000,
        lightMin = 0,
        wateringTime = 60,
        pictureFrequency = 60)
        db.session.add(setting)
        db.session.commit()
    else:
        db.session.commit()
        setting.moisMin = moisMin
        setting.moisMax = moisMax
        setting.tempMin = tempMin
        setting.tempmax = tempMax
        setting.lightMin = lightMin
        setting.lightMax = lightMax
        setting.wateringTime = wateringTime
        setting.pictureFrequency = pictureFrequency
        db.session.commit()

    camera_schedule_job.reschedule(trigger="interval", hours=pictureFrequency)
    return setting.to_dict()

@app.route('/latest_picture/', methods=["GET"])
def get_latest_picture():
    return {'image_path': "/" + collect_sensors.camera.latest_image.split("app/")[1]}, 200

@app.route('/take_picture/', methods=["GET"])
def take_picture():
    collect_sensors.camera.save_picture()
    return get_latest_picture()

@app.route('/water_plant/', methods=["GET"])
def water_plant_fixed():
    pump.on()
    time.sleep(3)
    pump.off()
    return {'success': True}, 200