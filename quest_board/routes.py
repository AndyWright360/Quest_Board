from flask import (
    render_template, request, redirect,
    flash, session, url_for, abort)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from quest_board import app, db
from quest_board.models import User, Event


@app.route("/")
def home():
    """
    Render home page
    """
    return render_template("index.html")


@app.route("/sign_up", methods=["GET", "POST"])
def sign_up():
    """
    Prevent logged in users from accessing the page,
    Retrieves data from user inputs,
    Checks if both password inputs match,
    Checks if username already exists in the database,
    On unsuccessful validation reload page with flash message,
    Stores user details in database if validations pass,
    Stores username in session cookie,
    Redirects user to profile page
    """
    if "user" in session:  # Checks if user is logged in
        flash("You're already logged in")
        return redirect(url_for("profile", username=session["user"]))

    if request.method == "POST":
        username = request.form.get("username").lower()
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        # Check if passwords match
        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect(url_for("sign_up"))

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
        session["user"] = username
        flash("Registration Successful!")
        return redirect(url_for("profile", username=username))

    else:
        return render_template("sign_up.html")


@app.route("/log_in", methods=["GET", "POST"])
def log_in():
    """
    Prevent logged in users from accessing the page,
    Retrieves data from user inputs,
    Search database for matching username,
    Checks password input against stored data,
    On successful validation redirect user to profile page,
    On unsuccessful validation reload login page with flash message
    """
    if "user" in session:  # Checks if user is logged in
        flash("You're already logged in")
        return redirect(url_for("profile", username=session["user"]))

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

    else:
        return render_template("log_in.html")


@app.route("/profile/<username>")
def profile(username):
    """
    Prevent logged out users from accessing the page,
    Search database for user object that matches the username,
    Retrive all events associated with the user and pass them
    through to the profile page
    """
    if "user" in session:  # Checks if user is logged in
        # Retrieve the user object from the database
        user = User.query.filter_by(username=session["user"]).first()

        # Retrieve events created by the user
        created_events = Event.query.filter_by(
            created_by=user.username).order_by(Event.date).all()

        # Retrieve events joined by the user
        joined_events = user.events

        return render_template("profile.html", username=username,
                               created_events=created_events,
                               joined_events=joined_events)

    else:
        flash("You need to be logged in to access this page")
        return redirect(url_for("log_in"))


@app.route("/logout")
def logout():
    """
    Prevent users who aren't logged in from accessing the function,
    Removes the username from the session cookie
    """
    if "user" in session:  # Check if user is logged in
        # Remove user from session cookies
        flash("You have been logged out")
        session.pop("user")
        return redirect(url_for("log_in"))
    else:
        flash("You need to be logged in to log out")
        return redirect(url_for("log_in"))


@app.route("/create_event", methods=["GET", "POST"])
def create_event():
    """
    Prevent logged out users from accessing the page,
    Prevent date input from being in the past,
    Checks text inputs contain valid data,
    Posts event data to relevant database table
    """
    if "user" in session:  # Check if user is logged in
        if request.method == "POST":
            event_date = datetime.strptime(request.form.get(
                "date"), "%d %b, %Y").date()
            event_name = request.form.get("event_name")
            description = request.form.get("description")

            # Check event date against current date
            if event_date < datetime.today().date():
                flash("Event date can't be in the past")
                return redirect(url_for("create_event"))

            # Check if text inputs are only white spaces
            if event_name.strip() == "" or description.strip() == "":
                flash("Inputs must not be empty")
                return redirect(url_for("create_event"))

            # Check if text inputs start or end with spaces
            if (event_name != event_name.strip() or
                    description != description.strip()):
                flash("Inputs must not start or end with spaces")
                return redirect(url_for("create_event"))

            event = Event(
                event_name=event_name,
                location=request.form.get("location"),
                time=request.form.get("time"),
                date=event_date,
                created_by=session["user"],
                party_size=request.form.get("party_size"),
                description=description,
                exp_level=request.form.get("exp_level")
            )
            db.session.add(event)
            db.session.commit()
            flash((f"Event '{event.event_name}' created"))
            return redirect(url_for("events"))

        else:
            return render_template("create_event.html")

    else:
        flash("You need to be logged in to create an event")
        return redirect(url_for("log_in"))


@app.route("/edit_event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    """
    Check that the event exists within the database,
    Prevent logged out users from accessing the page,
    Check user has the relevant authorisation to edit the event,
    Prevent user from reducing party size below number of
    currently joined party members,
    Prevent date input from being in the past,
    Checks text inputs contain valid data,
    Posts updated event data to relevant database table
    """
    event = Event.query.get_or_404(event_id)  # Check if the event exists
    if "user" in session:  # Check if user is logged in

        # Check user is authorised to edit the event
        if session["user"] == event.created_by or session["user"] == "admin":
            if request.method == "POST":
                new_party_size = int(request.form.get("party_size"))
                new_event_date = datetime.strptime(
                    request.form.get("date"), "%d %b, %Y").date()
                new_event_name = request.form.get("event_name")
                new_description = request.form.get("description")

                # Check if the new party size is greater than
                # or equal to the number of party members
                if new_party_size < len(event.party_members):
                    flash(
                        "Party size can't be less than current joined members"
                        )
                    return redirect(url_for("edit_event", event_id=event_id))

                # Check event date against current date
                if new_event_date < datetime.today().date():
                    flash("Event date can't be in the past")
                    return redirect(url_for("edit_event", event_id=event_id))

                # Check if text inputs are only white spaces
                if (new_event_name.strip() == "" or
                        new_description.strip() == ""):
                    flash("Inputs must not be empty")
                    return redirect(url_for("edit_event", event_id=event_id))

                # Check if text inputs start or end with spaces
                if (new_event_name != new_event_name.strip() or
                        new_description != new_description.strip()):
                    flash("Inputs must not start or end with spaces")
                    return redirect(url_for("edit_event", event_id=event_id))

                event.party_size = new_party_size
                event.event_name = new_event_name
                event.location = request.form.get("location")
                event.time = request.form.get("time")
                event.date = new_event_date
                event.description = new_description
                event.exp_level = request.form.get("exp_level")

                db.session.commit()
                flash("Event updated successfully")
                return redirect(url_for("events"))

            else:
                return render_template("edit_event.html", event=event)
        else:
            flash("You're not authorised to edit this event")
            abort(403)  # Forbidden access
    else:
        flash("You need to be logged in to edit an event")
        return redirect(url_for("log_in"))


@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    """
    Check that the event exists within the database,
    Prevent logged out users from accessing the page,
    Check user has the relevant authorisation to delete the event,
    Removes event data from database
    """
    event = Event.query.get_or_404(event_id)  # Check if the event exists
    if "user" in session:  # Check if user is logged in

        # Check user is authorised to delete the event
        if session["user"] == event.created_by or session["user"] == "admin":
            db.session.delete(event)
            db.session.commit()
            flash("Event deleted successfully")
            return redirect(url_for("events"))
        else:
            flash("You're not authorised to delete this event")
            abort(403)  # Forbidden access
    else:
        flash("You need to be logged in to delete an event")
        return redirect(url_for("log_in"))


@app.route("/events")
def events():
    """
    Prevent logged out users from accessing the page,
    Retrieve list of all events and pass them through to events page
    """
    if "user" in session:  # Check if user is logged in
        events = list(Event.query.order_by(Event.date).all())
        return render_template("events.html", events=events)
    else:
        flash("You need to be logged in to view events")
        return redirect(url_for("log_in"))


@app.route("/event/<int:event_id>")
def event(event_id):
    """
    Prevent logged out users from accessing the page,
    Retrieve event matching relevant id and pass it through to event page
    """
    if "user" in session:  # Check if user is logged in
        event = Event.query.get_or_404(event_id)
        return render_template("event.html", event=event)
    else:
        flash("You need to be logged in to view events")
        return redirect(url_for("log_in"))


@app.route("/join_event/<int:event_id>", methods=["POST"])
def join_event(event_id):
    """
    Prevent logged out users from accessing the page,
    Check if username exists within user table,
    Check if event has space available,
    Add relevant username to party_members table,
    Abort to 405 error page if not accessed by POST method
    """
    if request.method == "POST":
        if "user" in session:  # Check if user is logged in
            event = Event.query.get_or_404(event_id)
            user = User.query.filter_by(username=session["user"]).first()

            # Check if the event has available slots
            if len(event.party_members) < event.party_size:
                # Check username exists, if so add them to party member list
                if user:
                    event.party_members.append(user)
                    db.session.commit()
                    flash(f"You have joined '{event.event_name}'")
                    return redirect(url_for('event', event_id=event_id))
                else:
                    flash("User not found")
                    return redirect(url_for('event', event_id=event_id))
            else:
                flash("Sorry, this event is already full")
                return redirect(url_for("events"))
        else:
            flash("You need to be logged in to join an event")
            return redirect(url_for('log_in'))
    else:
        abort(405)  # Redirect to 405 error page if method is not POST


@app.route("/leave_event/<int:event_id>", methods=["POST"])
def leave_event(event_id):
    """
    Prevent logged out users from accessing the page,
    Check if username exists within party_members table,
    Remove relevant username from party_members table,
    Abort to 405 error page if not accessed by POST method
    """
    if request.method == "POST":
        if "user" in session:  # Check if user is logged in
            event = Event.query.get_or_404(event_id)
            user = User.query.filter_by(username=session["user"]).first()

            # Check username exists within list of party members
            if user in event.party_members:
                event.party_members.remove(user)
                db.session.commit()
                flash(f"You have left '{event.event_name}'")
                return redirect(url_for('event', event_id=event_id))
            else:
                flash("You are not currently a member of this event")
                return redirect(url_for('event', event_id=event_id))
        else:
            flash("You need to be logged in to leave an event")
            return redirect(url_for('log_in'))
    else:
        abort(405)  # Redirect to 405 error page if method is not POST


@app.errorhandler(400)
def bad_request(error):
    """
    Render custom error page when corresponding error detected
    """
    return render_template('400.html'), 400


@app.errorhandler(403)
def forbidden(error):
    """
    Render custom error page when corresponding error detected
    """
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(error):
    """
    Render custom error page when corresponding error detected
    """
    return render_template('404.html'), 404


@app.errorhandler(405)
def page_not_found(error):
    """
    Render custom error page when corresponding error detected
    """
    return render_template('405.html'), 405


@app.errorhandler(500)
def internal_server(error):
    """
    Render custom error page when corresponding error detected
    """
    return render_template('500.html'), 500
