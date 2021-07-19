# SQLAlchemy Challenge
## SQLAlchemy Homework - Surf's Up!

---
### Task

In this scenario we are planning a trip to Hawaii and are performing some analysis on the climate.
There are quite a few different sections to this challenge:

1. Climate Analysis and Exploration
2. Precipitation Analysis
3. Station Analysis
4. Climate App
5. Bonus section 1 - Temperature Analysis I
6. Bonus section 2 - Temperature Analysis II

The main aims of these tasks are outlined below:

# Climate Analysis and Exploration
For this section we need to complete some basic analysis and data exploration of the climate database.
The analysis should be completed using SQLAlchemy ORM queries, Pandas, and Matplotlib.
We need to connect to the sqlite database, reflect the tables into classes, save references to the tables and finally link Python to the database by creating an SQLAlchemy session.

#### Precipitation Analysis

The precipation analysis involves retrieving 12 months worth of precipitation data and turning it into a Pandas Dataframe.
We then need to plot the results using the DataFrame plot method.

#### Station Analysis

The station analysis involves designing queries to provide the below results:
Design a query to calculate the total number of stations in the dataset.
* Design a query to find the most active stations (i.e. which stations have the most rows?).
* List the stations and observation counts in descending order.
* Which station id has the highest number of observations?
* Using the most active station id, calculate the lowest, highest, and average temperature.
* Design a query to retrieve the last 12 months of temperature observation data (TOBS).
* Filter by the station with the highest number of observations.
* Query the last 12 months of temperature observation data for this station.
* Plot the results as a histogram with bins=12

#### Climate App

This section involved designing a Flask API based on the queries in the previous analysis.
Routes to be created include:
* __/__ - A homepage that lists all routes available
* __/api/v1.0/precipitation__ - That displays the data date and prcp value as a dictionary
* __/api/v1.0/stations__ - That returns a list of stations.
* __/api/v1.0/tobs__ - That queries the date and TOBS of the most avtive station for the last year of data.
* __/api/v1.0/start__ and __/api/v1.0/\<start>\*/\<end>*\__

---
### Method



---
### Results




---
### Files


