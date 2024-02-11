from quest_board import db


class User(db.Model):
    # schema for the User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Username: {1}".format(
            self.id, self.username
        )


class Event(db.Model):
    # schema for the Event model
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(24), nullable=False)
    created_by = db.Column(db.String(15), db.ForeignKey(
        "user.username"), nullable=True)
    location = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    exp_level = db.Column(db.String(50), nullable=False)
    party_size = db.Column(db.Integer, nullable=False)
    party_members = db.Column(db.String(15), db.ForeignKey(
        "user.username"), nullable=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return ("#{0} - Event: {1} | Location: {2} | Date: {3} | Time: {4}"
                .format(
                    self.id, self.event_name, self.location,
                    self.date, self.time
                ))
