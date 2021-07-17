# Import Setup and Dependencies
import datetime as dt 
import numpy as np 
import pandas as pd 

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect

from flask import Flask, jsonify


engine = create_engine("sqlite:///Resources/hawaii.sqlite")


# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask Setup

app = Flask(__name__)

# Flask Routes

@app.route("/")
def welcome():
    return (
        f"Hello, welcome to the Hawaii climate analysis API!<br/><br/>"
        f"The available routes are:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():

    session = Session(engine)

    one_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    year_data = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= one_year).all()

    session.close

    precip = {date: prcp for date, prcp in year_data}
    return jsonify(precip)


@app.route("/api/v1.0/stations") 
def stations():

    session = Session(engine)

    results = session.query(Station.station).all()

    session.close

    station_name = list(np.ravel(results))

    return jsonify(station_name)


@app.route("/api/v1.0/tobs")
def tobs():

    session = Session(engine)

    active_station = session.query(Measurement.station, func.count(Measurement.station)).group_by(Measurement.station).\
                order_by(func.count(Measurement.station).desc()).first()

    station_year_data = dt.date(2017, 8, 18) - dt.timedelta(days=365)
    temp_data = session.query(Measurement.date, Measurement.tobs).filter((Measurement.date >= station_year_data),\
                 Measurement.station == active_station[0]).all()

    session.close

    year_tobs = {date: tobs for date, tobs in temp_data}
    return jsonify(year_tobs)

@app.route("/api/v1.0/<start>")
def start_date(start):

    session = Session(engine)

    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    
    temp_results = session.query(*sel).filter(Measurement.date >= start).all()

    session.close

    all_tobs = []

    for min, max, avg in temp_results:
        start_dict = {}
        start_dict["Min"] = min
        start_dict["Max"] = max
        start_dict["Avg"] = avg
        all_tobs.append(start_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):

    session = Session(engine)

    sel = [func.min(Measurement.tobs), func.max(Measurement.tobs), func.avg(Measurement.tobs)]
    
    temp_results = session.query(*sel).filter(Measurement.date >= start).filter(Measurement.date <= end).all()
    
    session.close

    all_tobs_filtered = []

    for min, max, avg in temp_results:
        date_dict = {}
        date_dict["Min"] = min
        date_dict["Max"] = max
        date_dict["Avg"] = avg
        all_tobs_filtered.append(date_dict)

    return jsonify(all_tobs_filtered)


if __name__ == "__main__":
    app.run(debug=True)



