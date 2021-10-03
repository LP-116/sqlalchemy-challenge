# SQLAlchemy Challenge
## Surf's Up!

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
* __/api/v1.0/precipitation__ - Displays the data date and prcp value as a dictionary
* __/api/v1.0/stations__ - Returns a list of stations.
* __/api/v1.0/tobs__ - Queries the date and TOBS of the most avtive station for the last year of data.
* __/api/v1.0/start__ and __/api/v1.0/start/end__ - Returns a list of the minimum, average and maximum temperature rate for a given start or start-end range.

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
This plot was a challenge to get the plot as per the example. To complete this graph "matplotlib.ticker as ticker" is imported which enables the use of the "set_major_locator" parameter to define how many tick points are on the x_axis. As there are 2230 lines and 9 ticks present, the locator is set to appear every 250 entries.

![Prcp plot](https://user-images.githubusercontent.com/82348616/126107202-6afa4d79-6018-4ee6-af04-57609970e63b.PNG)

The final part of this section involved using .describe to calculate the summary statistic for the precipitation data.


#### Station Analysis

The station analysis starts by using the inspector to view the column names and types of the station table.
A count is then performed on the table to identify that there are 9 stations in the dataset.

A query is then completed using the Measurement table and the station columns. The station column is called twice. Once to get the station ID and once to get the count of the station results (i.e. how many times each station ID appears in the dataset).

It is determined the station USC00519281 is most active with 2772 lines in the dataset.

Using the most active station as a filter a query is done to find the minimum, maximum and average temperatures at the station.
In this case the filter matches the station column in the measurement table to the ID of the most active station.

Using the most active station as a filter, we then look at a years worth of observations. To do this we find the most recent date of the most active station and then get the date 1 year before. The date 1 year before is then used as another filter for the query.

As a final step for this section we use the results from the previous query and plot the results as a histogram.


#### Climate App

This section involved designing a Flask API based on the queries in the previous analysis.
The analysis started by importing the setup and dependencies and then setting up the database.
Again, the tables are reflected and references are saved.

The Flask is then setup and routes are created.

Routes created include:
* __/__ - A homepage that lists all routes available
* __/api/v1.0/precipitation__ - That displays the data date and prcp value as a dictionary
The precipitation results for the year are determined and stored in a dictionary.
A jsonify list of the results is returned.

* __/api/v1.0/stations__ - That returns a list of stations.
This is completed by simply running a squery on the station column in the station table and viewing all results is a jsonify list. 

* __/api/v1.0/tobs__ - That queries the date and TOBS of the most avtive station for the last year of data.
Using the climate calculation as a base, the most active station is identified and a years worth of data is determined. 
The results are then stored in a dictionary and returned as a jsonify list.

* __/api/v1.0/start__ and __/api/v1.0/start/end__ - That returns a list of the minimum, average and maximum temperature rate for a given start or start-end range.
This route is completed using one or two filters for the dates inputted.
The results are added to a dictionary which is then returned in jsonify format.


#### Bonus section 1 - Temperature Analysis I
This section starts by reading in the hawaii measurements csv.
The date is then converted from string to datetime using pd.to_datetime.
The date column is then set to the index of the dataframe.

Data from June and December is then calculated by matching the dataframe index month to either 6 (June) or 12 (December).
The average temperatures for June and December are determined using .mean()

Collections of temperature data is then created by storing the "tobs" column of each dataset.

A ttest is then performed on the June and December temps.


#### Bonus section 2 - Temperature Analysis II

The final section of the challenge is the section I found most difficult.

The analysis starts as per the others - the engine is created, the tables reflected, the references to each table saved and the session link is established.

Using the defined function we calculate the minimum, maximum and average temperatures for a historcal date range of our trip ( '2017-08-01' - '2017-08-07').
I then use the results to create a dataframe and add an extra column titled EBAR which is the max temp - min temp.
A bar graph is then generated. The average temperature is the height of the bar graph and EBAR is the calculation for the error bar.

The rainfall is then analysed by running a session query on both the measurement and station table.
The query includes a filter that essentially joins the tables on station ID. The filter states that the station column in the measurement table matches the station column in the station table. Another filter is applied to the query so that the results displayed is for the time period we want.
The results are also ordered_by prcp and displayed from highest to lowest.

The final part to this section involved calculating daily normal temperatures for the trip. A predefined function that calc the average, maximum and minimum temperatures is given and to start we need to get the dates in the correct formats so that we can use the function.

Based on the start and end date a range of dates is calculated and added to a list.

A "new_list" is then created by coverting the orginal list to the correct format using date.strftime.

We then create a new list titled 'normals' and use the predefined function on our new_list, appending each entry into the normals list.

A blank dataframe is then created and the normals list is added to the dataframe.
The dates are also added as the index for the dataframe.

For the final part in this challenge we plot the temperature data as a area graph.


---
### Results

We have learnt the below from completing the analysis:

* The majority of days have high temperatures around 75 degrees

![histo](https://user-images.githubusercontent.com/82348616/126110276-635be37c-7b3c-42f1-9aeb-d7621cb184d6.PNG)

* The p-value in the TTest is very low below 0 (e-187), this suggests that the test is statistically significant.
![TTest](https://user-images.githubusercontent.com/82348616/126110544-f27fe817-164c-49c6-9302-9ad8d369b69b.PNG)


* For 2017 the average temperature was just below 80

![bar](https://user-images.githubusercontent.com/82348616/126110491-582a9611-bc8c-450e-b102-58b0009cd51b.PNG)

* Historical data for the year 2017 for the trip dates show a maximum temperature of above 80 and a minimum of just below 70.

![area](https://user-images.githubusercontent.com/82348616/126110691-8916da50-c84e-43e2-b56c-ad9238771280.PNG)


---
### Files

Included in the main branch of this repository are the below key files:

* A resources folder which contains the sqlite database and the csv files.
* climate_starter.ipynb file which is the first part of the assignment.
* app.py file for the Flask analysis
* temp_analysis_bonus_1_starter.ipynb file which is the first part of the bonus section.
* temp_analysis_bonus_2_starter.ipynb file which is the second part of the bonus section.

Note: 
Please run the app.py in Python terminal.
Ensure a start date or state and end date is defined when running the date routes.
The "start" and "end" needs to be replaced with a date.

