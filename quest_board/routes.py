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


@app.route("/edit_event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    event = Event.query.get_or_404(event_id)
    if request.method == "POST":
        event.event_name = request.form.get("event_name"),
        event.location = request.form.get("location"),
        event.time = request.form.get("time"),
        event.date = request.form.get("date"),
        event.party_size = request.form.get("party_size"),
        event.description = request.form.get("description"),
        event.exp_level = request.form.get("exp_level")
        db.session.commit()
        return redirect(url_for("events"))
    return render_template("edit_event.html", event=event)


@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    event = Event.query.get_or_404(event_id)
    db.session.delete(event)
    db.session.commit()
    return redirect(url_for("events"))


@app.route("/events")
def events():
    events = list(Event.query.order_by(Event.date).all())
    return render_template("events.html", events=events)
