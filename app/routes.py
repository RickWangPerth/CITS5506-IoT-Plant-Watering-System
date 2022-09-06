from flask import render_template,request, flash, redirect, session, url_for
from app import app, db
from app.models import Setting


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", title="Dashboard")

@app.route('/historical/')
def historical():
    return render_template("historical.html", title="Historical Data")

@app.route('/advance', methods=['GET', 'POST'])
def advance():
    return render_template("advance.html", title="Advance Setting")

@app.route('/Setting', methods=["POST"])
def store_Setting():
    moisMin = request.json.get("moisMin")
    moisMax = request.json.get("moisMax")
    tempMin = request.json.get("tempMin")
    tempMax = request.json.get("tempMax")
    lightMax = request.json.get("lightMax")
    lightMin = request.json.get("lightMin")
    wateringTime = request.json.get("wateringTime")
    print(request.json, 'sss')

    setting = Setting(
        id = 1,
        moisMin = moisMin,
        moisMax = moisMax,
        tempMin  = tempMin,
        tempMax = tempMax,
        lightMax = lightMax,
        lightMin = lightMin,
        wateringTime = wateringTime
    )
    db.session.add(setting)
    db.session.commit()
    flash('Item created.')
    return setting.to_dict()