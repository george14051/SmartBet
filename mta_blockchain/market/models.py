from market import db
from market import bcrypt


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    budget = db.Column(db.Integer(), nullable=False, default=1000)

    @property
    def password(self):
        return self.password_hash

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def __repr__(self):
        return f'User {self.username}'


class Bet(db.Model):
    # contract info:
    uuid = db.Column(db.String(length=20), primary_key=True, nullable=False, unique=True)
    public = db.Column(db.Boolean, nullable=False)
    numberOfParticipants = db.Column(db.Integer(), nullable=False)
    active = db.Column(db.Boolean, nullable=False) #true before the game, false after the game
    # game info:
    date = db.Column(db.DateTime, nullable=False)
    hour = db.Column(db.String, nullable=False)
    sportType = db.Column(db.String, nullable=False)
    teamA = db.Column(db.String(length=30), nullable=False)
    teamB = db.Column(db.String(length=30), nullable=False)
    # draw = db.Column(db.Boolean, nullable=False) // need to add agter
    # bet info:
    ratio = db.Column(db.Integer, nullable=False, unique=True)
    maxParticipants = db.Column(db.Integer, nullable=False, unique=True)
    minParticipants = db.Column(db.Integer, nullable=False, unique=True)
    minVal = db.Column(db.Integer, nullable=False, unique=True)
    maxVal = db.Column(db.Integer, nullable=False, unique=True)

    def __repr__(self):
        return f'Bet {self.id}'
