from quest_board import db


"""
Code for association table and creating many-to-many relationship between User and Event
models was modified from https://medium.com/@warrenzhang17/many-to-many-relationships-in-sqlalchemy-ba08f8e9ccf7
Credit: Warren Zhang
"""
# Association table for many-to-many relationship between events and users
event_user = db.Table(
    'event_user',
    db.Column('event_id', db.Integer, db.ForeignKey('events.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True)
)


class User(db.Model):
    # schema for the User model
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    events = db.relationship(
        'Event',
        secondary=event_user,
        back_populates='party_members')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return "#{0} - Username: {1}".format(
            self.id, self.username
        )


class Event(db.Model):
    # schema for the Event model
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(24), nullable=False)
    created_by = db.Column(db.String(15), db.ForeignKey(
        "users.username"), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    exp_level = db.Column(db.String(50), nullable=False)
    party_size = db.Column(db.Integer, nullable=False)
    party_members = db.relationship(
        'User', 
        secondary=event_user, 
        back_populates='events')

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return ("#{0} - Event: {1} | Location: {2} | Date: {3} | Time: {4}"
                .format(
                    self.id, self.event_name, self.location,
                    self.date, self.time
                ))
