from flask import render_template,request, flash, redirect, session, url_for
from app import app, db
from app.models import Setting, History


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", title="Dashboard")

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
        'moisMax': 70, 'tempMin': 5, 'tempMax': 35, \
        'lightMax': 5, 'lightMin':2, 'wateringTime': 2}, Title="Default Settings")

    return render_template('advance.html', data={'moisMin': setting.moisMin, \
    'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
    'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime}, Title="Advanced Settings")

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
    print(request.json, 'sss')

    setting = Setting.query.first()
    if setting is None:
        # add defalut setting
        setting = Setting(
        id = 1,
        moisMin = 20,
        moisMax = 70,
        tempMin  = 5,
        tempMax = 35,
        lightMax = 5,
        lightMin = 2,
        wateringTime = 2)
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
        db.session.commit()
    return setting.to_dict()
