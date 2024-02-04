from flask import render_template
from quest_board import app, db
from quest_board.models import User, Event


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create_event", methods=["GET", "POST"])
def create_event():
    return render_template("create_event.html")


@app.route("/events")
def events():
    return render_template("events.html")
