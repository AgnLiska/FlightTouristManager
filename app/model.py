from . import database
from werkzeug.security import generate_password_hash, check_password_hash

reservations = database.Table('reservations',
database.Column('tourist_id', database.Integer, database.ForeignKey('tourists.id')),
database.Column('flight_id', database.Integer, database.ForeignKey('flights.id'))
)

class Flight(database.Model):
    __tablename__ = 'flights'
    id = database.Column(database.Integer, primary_key=True)
    departure = database.Column(database.DateTime)
    arrival = database.Column(database.DateTime)
    seats = database.Column(database.Integer)
    price = database.Column(database.Float(precision=2))

    def __repr__(self):
        return '{}'.format(self.id)

class Tourist(database.Model):
    __tablename__ = 'tourists'
    id = database.Column(database.Integer, primary_key=True)
    fstname = database.Column(database.String(64))
    lstname = database.Column(database.String(64))
    gender = database.Column(database.String(64))
    country = database.Column(database.String(64))
    remarks = database.Column(database.String(500))
    birth = database.Column(database.DateTime)
    lflights = database.relationship('Flight', secondary=reservations, backref=database.backref('tourists', lazy='dynamic'), lazy='dynamic')
    
    def __repr__(self):
        return '{} {}'.format(self.fstname,self.lstname)