from flask import render_template, flash, redirect, session, url_for
from app import app


@app.route('/')
@app.route('/index/')
def index():
    return render_template("index.html", title="Dashboard")

@app.route('/historical')
def historcial():
    return render_template("historical.html", title="Historical Data")