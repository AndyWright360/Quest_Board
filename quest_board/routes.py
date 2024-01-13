from flask import render_template
from quest_board import app, db
from quest_board.models import User, Event


@app.route("/")
def home():
    return render_template("base.html")
