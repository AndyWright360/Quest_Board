from flask import render_template
from quest_board import app, db


@app.route("/")
def home():
    return render_template("index.html")