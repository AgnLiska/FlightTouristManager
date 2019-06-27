from flask import render_template, session, redirect, url_for, request, flash
from . import flights
from .form import FlightForm, TouristForm
from .. import database
from ..model import Flight, Tourist, reservations

@flights.route('/', methods = ['GET', 'POST'])
def index():
    flightform=FlightForm()
    if flightform.validate_on_submit():
        flight = Flight(departure=flightform.departure.data, arrival=flightform.arrival.data, seats=flightform.seats.data, price=flightform.price.data)
        database.session.add(flight)
        database.session.commit()
        return redirect(url_for('.index'))
    
    tform=TouristForm()
    if tform.validate_on_submit():
        t = Tourist(fstname=tform.fstname.data, lstname=tform.lstname.data, gender=tform.gender.data, country=tform.country.data, remarks=tform.remarks.data, birth=tform.birth.data)
        database.session.add(t)
        database.session.commit()
        return redirect(url_for('.index'))

    airtraffic = Flight.query.all()
    tlist = Tourist.query.all()

    return render_template('index.html', flightform=flightform, airtraffic=airtraffic, tform=tform, tlist=tlist)

@flights.route('/remove/flight/<id>')
def remove(id):
    flight = Flight.query.filter_by(id=id).first()
    for tourist in flight.tourists.all():
        tourist.lflights.remove(flight)
    database.session.delete(flight) 
    database.session.commit()
    return redirect(url_for('.index'))

@flights.route('/remove/tourist/<id>')
def removet(id):
    tourist = Tourist.query.filter_by(id=id).first()
    tourist.lflights = []
    database.session.delete(tourist) 
    database.session.commit()
    return redirect(url_for('.index'))

@flights.route('/add/flight/<id>', methods = ['POST'])
def addf(id):
    f = request.form
    flight = Flight.query.filter_by(id=f['flights']).first()
    if check(flight):
        tourist = Tourist.query.filter_by(id=id).first()
        tourist.lflights.append(flight)
        database.session.commit()
    else:
        flash('No more seats')
    return redirect(url_for('.index'))

@flights.route('/delete/flight/<id>', methods = ['POST'])
def deletef(id):
    f = request.form
    if f.get('flights') is None:
        return redirect(url_for('.index'))
    flight = Flight.query.filter_by(id=f['flights']).first()
    tourist = Tourist.query.filter_by(id=id).first()
    tourist.lflights.remove(flight)
    database.session.commit()
    return redirect(url_for('.index'))

@flights.route('/add/tourist/<id>', methods = ['POST'])
def addt(id):
    f = request.form
    tourist = Tourist.query.filter_by(id=f['tourists']).first()
    flight = Flight.query.filter_by(id=id).first()
    if check(flight):
        tourist.lflights.append(flight)
        database.session.commit()
    else:
        flash('No more seats')
    return redirect(url_for('.index'))

@flights.route('/delete/tourist/<id>', methods = ['POST'])
def deletet(id):
    f = request.form
    if f.get('tourists') is None:
        return redirect(url_for('.index'))
    tourist = Tourist.query.filter_by(id=f['tourists']).first()
    flight = Flight.query.filter_by(id=id).first()
    tourist.lflights.remove(flight)
    database.session.commit()
    return redirect(url_for('.index'))

def check(flight):
    seats = flight.seats
    taken = len(flight.tourists.all())
    if seats > taken:
        return True