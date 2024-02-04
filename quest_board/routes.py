from flask import render_template, request, redirect, url_for
from quest_board import app, db
from quest_board.models import User, Event


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/create_event", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        event = Event(
            event_name=request.form.get("event_name"),
            location=request.form.get("location"),
            time=request.form.get("time"),
            date=request.form.get("date"),
            party_size=request.form.get("party_size"),
            description=request.form.get("description"),
            exp_level=request.form.get("exp_level")
        )
        db.session.add(event)
        db.session.commit()
        return redirect(url_for("events"))
    return render_template("create_event.html")


@app.route("/events")
def events():
    return render_template("events.html")
