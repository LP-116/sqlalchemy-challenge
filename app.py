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
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end><br/>"
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

    station_year_data = dt.date(2017, 8, 18) - dt.timedelta(days=365)
    temp_data = session.query(Measurement.date, Measurement.tobs).filter((Measurement.date >= station_year_data), Measurement.station == "USC00519281").all()

    session.close

    year_tobs = {date: tobs for date, tobs in temp_data}
    return jsonify(year_tobs)







    







if __name__ == "__main__":
    app.run(debug=True)



