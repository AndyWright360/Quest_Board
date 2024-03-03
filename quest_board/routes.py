from flask import render_template, request, redirect, flash, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from quest_board import app, db
from quest_board.models import User, Event


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")

        # Check if username already exists in database
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Username already exists!")
            return redirect(url_for("sign_up"))

        # Add user to database
        user = User(
            username=username,
            password=generate_password_hash(password)
        )
        db.session.add(user)
        db.session.commit()

        # Put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")

        # Check if username exists in database
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            # Ensure hashed password matches user input
            if check_password_hash(existing_user.password, password):
                session["user"] = username
                flash("Welcome, {}".format(username.capitalize()))
                return redirect(
                    url_for("profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("log_in"))

        else:
            # Username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("log_in"))

    return render_template("log_in.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab the session user's username from the database
    username = User.query.filter_by(
        username=session["user"]).first().username
    
    if session["user"]:
        return render_template("profile.html", username=username)
    
    return redirect(url_for("log_in"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("log_in"))


@app.route("/create_event", methods=["GET", "POST"])
def create_event():
    if request.method == "POST":
        if "user" in session:  # Check if user is logged in
            event = Event(
                event_name=request.form.get("event_name"),
                location=request.form.get("location"),
                time=request.form.get("time"),
                date=request.form.get("date"),
                created_by=session["user"],
                party_size=request.form.get("party_size"),
                description=request.form.get("description"),
                exp_level=request.form.get("exp_level")
            )
            db.session.add(event)
            db.session.commit()
            return redirect(url_for("events"))
        else:
            flash("You need to be logged in to create an event")
            return redirect(url_for("log_in"))  # Redirect to login page if user is not logged in
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


@app.route("/event/<int:event_id>")
def event(event_id):
    event = Event.query.get_or_404(event_id)
    return render_template("event.html", event=event)


@app.route("/join_event/<int:event_id>", methods=["POST"])
def join_event(event_id):
    if "user" in session:
        username = session["user"]
        event = Event.query.get_or_404(event_id)
        user = User.query.filter_by(username=username).first()
        if user:
            event.party_members.append(user)
            db.session.commit()
            return redirect(url_for('event', event_id=event_id))
        else:
            flash("User not found")
    else:
        flash("You need to be logged in to join an event")
        return redirect(url_for('log_in'))