from market import db
from market import bcrypt


class User(db.Model):
    id = db.Column(db.String(length=50), primary_key=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)
    # bets = db.relationship('Bet',  db.ForeignKey('bet.id'))

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
    uuid = db.Column(db.String(length=50), primary_key=True, unique=True)
    public = db.Column(db.Boolean, nullable=False)
    numberOfParticipants = db.Column(db.Integer(), nullable=False)
    active = db.Column(db.Boolean, nullable=False)  # true before the game, false after the game
    # game info:
    date = db.Column(db.String(10), nullable=False)
    sportType = db.Column(db.String(length=50), nullable=False)
    teamA = db.Column(db.String(length=30), nullable=False)
    teamB = db.Column(db.String(length=30), nullable=False)
    # draw = db.Column(db.Boolean, nullable=False) // need to add it later
    # bet info:
    ratio = db.Column(db.Integer, nullable=False)
    maxParticipants = db.Column(db.Integer, nullable=False)
    minParticipants = db.Column(db.Integer, nullable=False)
    minVal = db.Column(db.Integer, nullable=False)
    maxVal = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Bet {self.id}'
