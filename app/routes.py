from flask import render_template,request, flash, redirect, session, url_for
from app import app, db
from app.models import Setting


@app.route('/')
@app.route('/index/',methods=['GET'])
def index():
    setting = Setting.query.first()
    return render_template("index.html", data={'moisMin': setting.moisMin, \
    'moisMax': setting.moisMax, 'tempMin': setting.tempMin, 'tempMax': setting.tempMax, \
    'lightMax': setting.lightMax, 'lightMin': setting.lightMin, 'wateringTime': setting.wateringTime}, title="Dashboard")


@app.route('/historical/')
def historical():
    return render_template("historical.html", title="Historical Data")

@app.route('/advance', methods=['GET', 'POST'])
def advance():
    setting = Setting.query.first()
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
    setting.moisMin = moisMin
    setting.moisMax = moisMax
    setting.tempMin = tempMin
    setting.tempmax = tempMax
    setting.lightMin = lightMin
    setting.lightMax = lightMax
    setting.wateringTime = wateringTime
    db.session.commit()

    # setting = Setting(
    #     id = id,
    #     moisMin = moisMin,
    #     moisMax = moisMax,
    #     tempMin  = tempMin,
    #     tempMax = tempMax,
    #     lightMax = lightMax,
    #     lightMin = lightMin,
    #     wateringTime = wateringTime
    # )
    # db.session.add(setting)
    # db.session.commit()

    flash('Item created.')
    return setting.to_dict()
