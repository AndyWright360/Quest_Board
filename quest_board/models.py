from quest_board import db


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.username


class Event(db.Model):
    # schema for the Event model
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(50), nullable=False)
    created_by = db.Column(db.String(50), db.ForeignKey(
        "user.username"), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    description = db.Column(db.Text, nullable=False)
    exp_level = db.Column(db.String(50), nullable=False)
    party_members = db.Column(db.String(50), db.ForeignKey(
        "user.username"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return self.event_name
