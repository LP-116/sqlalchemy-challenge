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

#### Climate Analysis and Exploration
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
* __/api/v1.0/start__ and __/api/v1.0/start/end__ - That returns a list of the minimum, average and maximum temperature rate for a given start or start-end range.

#### Bonus section 1 - Temperature Analysis I

In this first bonus section we are tasked with determining the average temperature for the months of June and December.
We then need to perform a ttest on temperature observations for each month.

#### Bonus section 2 - Temperature Analysis II

For the final section we are required to analyse temperature data for the 1st August to the 8th of August.
We need to calculate the minimum, average and maximum temperature for the date range and then complete a bar graph with an error bar to visulise the results.

Then we are required to complete an analysis on the rainfall and finally we need to complete some historical analysis for each day of the holiday.
Once the results are calculated the min, max and average temperatures are plotted as an area graph.

---
### Method

#### Climate Analysis and Exploration
The climate analysis and exploration starts by creating the engine to the hawaii.sqlite database.
The Base is then defined and the tables are reflected. 
Then Base.classes.keys() is used to view all of the tables in the database.

2 tables were identified - a measurement table and a station table. Each table was saved as a reference.
The session link from Python to the database was then created.

The inspector is then used on each table to identify the column types and data type of each column.


#### Precipitation Analysis

To start the precipitation analysis we use func.max on the date column in the measurement table and take the first result.
We then use datetime to get the date 1 year before the max date.

max date = 2017/08/23
previous year date = 2016/08/23

Once the dates are determined, a session.query is used to view the date and prcp columns in the Measurement table. 
A filter is applied to give all data from the 2016/08/23.
The results are then turned into a dataframe and the index is set as the date. 
This dataframe is then sorted by the index (the date).

The precipitation results for the year are then plotted in Pandas.
This plot was a challenge to get the plot as per the homework example. To complete this graph "matplotlib.ticker as ticker" is imported which enables the use of the "set_major_locator" parameter to define how many tick points are on the x_axis. As there are 2230 lines and 9 ticks present, the locator is set to appear every 250 entries.
![Prcp plot](https://user-images.githubusercontent.com/82348616/126107202-6afa4d79-6018-4ee6-af04-57609970e63b.PNG)

The final part of this section involved using .describe to calculate the summary statistic for the precipitation data.


#### Station Analysis



#### Climate App

This section involved designing a Flask API based on the queries in the previous analysis.
Routes to be created include:
* __/__ - A homepage that lists all routes available
* __/api/v1.0/precipitation__ - That displays the data date and prcp value as a dictionary
* __/api/v1.0/stations__ - That returns a list of stations.
* __/api/v1.0/tobs__ - That queries the date and TOBS of the most avtive station for the last year of data.
* __/api/v1.0/start__ and __/api/v1.0/start/end__ - That returns a list of the minimum, average and maximum temperature rate for a given start or start-end range.


#### Bonus section 1 - Temperature Analysis I



#### Bonus section 2 - Temperature Analysis II






---
### Results




---
### Files


