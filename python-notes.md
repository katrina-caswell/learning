Python as a calculator

```
print(5 + 5)
  10
print(5 - 5)
  0
print(3 * 5)
  15
print(10 / 7)
  1.4285714285714286
# Modulo: returns the remainder of the division of the number to the left by the number on the right
print(18 % 7)
  4
# Exponentiation: raises the number to its left to the power of the number to its right
print(4 ** 2)
  16
```

```
# You have £100, which you can invest with a 10% return each year. How much is £100 worth after 7 years?
print(100 * 1.1 ** 7)
  194.87171000000012
```

Calculations with variables

```
savings = 100
growth_multiplier = 1.1
year = 7
result = savings * growth_multiplier ** year
print (result)
  194.87171000000012
```

Determine data type of variable

```
print(type(growth_multiplier))
  <class 'float'>
```

Converting data types to concatenate a string

```
savings = 100
result = 100 * 1.10 ** 7
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")
```

Slicing Lists

```
# Remember how 0 indexing works, and that slicing this way [a:b] is inclusive of a and exclusive of b
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
downstairs = areas[0:6]
upstairs = areas[6:10]
bwords = areas[-4:]
print(downstairs)
print(upstairs)
  ['hallway', 11.25, 'kitchen', 18.0, 'living room', 20.0]
  ['bedroom', 10.75, 'bathroom', 9.5]
  ['bedroom', 10.75, 'bathroom', 9.5]
```

Deleting list items

```
areas = ["hallway", 11.25, "kitchen", 18.0,
        "chill zone", 20.0, "bedroom", 10.75,
         "bathroom", 10.50, "poolhouse", 24.5,
         "garage", 15.45]
del(areas[-4,-2])
# This code will remove poolhouse and 24.5 from the above list
```

Explicit list copying

```
areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = list(areas)
# If the above copy said areas_copy = areas, then any changes made to areas_copy would also change areas
areas_copy[0] = 5.0
print(areas)
```

Builtin functions:
* print
* str, int, bool, float
* type
* max
* round
* help
* len (length)
* pow (x to power of y)
* sorted (defaults ascending)
* index
* append
* remove
* reverse


```
list = [4, 56, 67, 9]
list_sorted = (sorted((list),reverse=True))
```

Example of count method
```
# string to experiment with: place
place = "poolhouse"
# Use upper() on place: place_up
place_up = str.upper(place)
# Print out place and place_up
print(place, place_up)
# Print out the number of o's in place
print(place.count('o'))
```

Testing math package to use pi
```
# Import the math package
import math as m
# Calculate C
C = (2*m.pi*r)
# Calculate A
A = (m.pi*(pow(r,2)))
# Build printout
print("Circumference: " + str(C))
print("Area: " + str(A))
```

Using numpy to check which parts of a list fall under certain conditions
```
# height_in and weight_lb are available as a regular lists

# Import numpy
import numpy as np

# Calculate the BMI: bmi
np_height_m = np.array(height_in) * 0.0254
np_weight_kg = np.array(weight_lb) * 0.453592
bmi = np_weight_kg / np_height_m ** 2

# Create the light array
light = bmi < 21

# Print out light
print(light)

# Print out BMIs of all baseball players whose BMI is below 21
print(bmi[light])
```

Generating data

```
#To generate data you can use np.random.normal(), its arguments are distribution mean, distribution standard deviation, and number of samples
height = np.round(np.random.normal(1.75, 0.20, 5000), 2)
weight = np.round(np.random.normal(60.32, 15, 5000), 2)
np_city = np.column_stack((height, weight))
```

Text files
```
file = open('moby_dick.txt', mode='r')
print(file.read())
file.close()
print(file.closed)

with open('moby_dick.txt') as file:
    print(file.readline())
    print(file.readline())
    print(file.readline())
```

Plotting data
```
import numpy as np
file = 'digits.csv'
digits = np.loadtxt(file, delimiter=',')
print(type(digits))
# Select and reshape a row
im = digits[21, 1:]
im_sq = np.reshape(im, (28, 28))
# Plot reshaped data (matplotlib.pyplot already loaded as plt)
plt.imshow(im_sq, cmap='Greys', interpolation='nearest')
plt.show()

file = 'seaslug.txt'
data = np.loadtxt(file, delimiter='\t', dtype=str)
print(data[0])
data_float = np.loadtxt(file, delimiter='\t', dtype=float, skiprows=1)
print(data_float[9])
# Scatter plot
plt.scatter(data_float[:, 0], data_float[:, 1])
plt.xlabel('time (min.)')
plt.ylabel('percentage of larvae')
plt.show()
```

Pandas dataframes, missing data
```
# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Assign filename: file
file = 'titanic_corrupt.txt'

# Import file: data
data = pd.read_csv(file, sep='\t', comment='#', na_values='Nothing')

# Print the head of the DataFrame
print(data.head())

# Plot 'Age' variable in a histogram
pd.DataFrame.hist(data[['Age']])
plt.xlabel('Age (years)')
plt.ylabel('count')
plt.show()
```

Pickle
```
import pickle
with open('data.pkl', 'rb') as file:
  d = pickle.load(file)
print(d)
print(type(d))
```

Excel
```
import pandas as pd
file = 'battledeath.xlsx'
xls = pd.ExcelFile(file)
print(xls.sheet_names)
```

Loading sheets by name or index
```
df1 = xls.parse('2004')
print(df1.head())
df2 = xls.parse(0)
print(df2.head())
```

Assigning columns names
```
# Parse the first sheet and rename the columns: df1
df1 = xls.parse(0, skiprows=[0], names=['Country','AAM due to War (2002)'])

# Print the head of the DataFrame df1
print(df1.head())

# Parse the first column of the second sheet and rename the column: df2
df2 = xls.parse(1, usecols=[0], skiprows=[0], names=['Country'])

# Print the head of the DataFrame df2
print(df2.head())
```

Importing SAS files
```
# Import sas7bdat package
from sas7bdat import SAS7BDAT

# Save file to a DataFrame: df_sas
with SAS7BDAT('sales.sas7bdat') as file:
    df_sas = file.to_data_frame()

# Print head of DataFrame
print(df_sas.head())

# Plot histograms of a DataFrame feature (pandas and pyplot already imported)
pd.DataFrame.hist(df_sas[['P']])
plt.ylabel('count')
plt.show()
```

Importing Stata files
```
# Import pandas
import pandas as pd

# Load Stata file into a pandas DataFrame: df
df = pd.read_stata('disarea.dta')

# Print the head of the DataFrame df
print(df.head())

# Plot histogram of one column of the DataFrame
pd.DataFrame.hist(df[['disa10']])
plt.xlabel('Extent of disease')
plt.ylabel('Number of countries')
plt.show()
```

Importing HDF5 files
```
# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)
```

Importing matlab files
```
# Import package
import scipy.io

# Load MATLAB file: mat
mat = scipy.io.loadmat('albeck_gene_expression.mat')

# Print the datatype type of mat
print(type(mat))

# Print the keys of the MATLAB dictionary
print(mat.keys())

# Print the type of the value corresponding to the key 'CYratioCyt'
print(type(mat['CYratioCyt']))

# Print the shape of the value corresponding to the key 'CYratioCyt'
print(np.shape(mat['CYratioCyt']))

# Subset the array and plot it
data = mat['CYratioCyt'][25, 5:]
fig = plt.figure()
plt.plot(data)
plt.xlabel('time (min.)')
plt.ylabel('normalized fluorescence (measure of expression)')
plt.show()
```

Creating a database engine for sqlite/identifying tables
```
# Import necessary module
from sqlalchemy import create_engine

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Save the table names to a list: table_names
table_names = engine.table_names()

# Print the table names to the shell
print(table_names)
```

Querying sqlite
```
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine connection
con = engine.connect()

# Perform query: rs
rs = con.execute("SELECT * FROM Album")

# Save results of the query to DataFrame: df
df = pd.DataFrame(rs.fetchall())

# Close connection
con.close()

# Print head of DataFrame df
print(df.head())
```

Fetchmany
```
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT LastName, Title FROM Employee")
    df = pd.DataFrame(rs.fetchmany(size=3))
    df.columns = rs.keys()

# Print the length of the DataFrame df
print(len(df))

# Print the head of the DataFrame df
print(df.head())
```

Easier sql execution with pandas
```
# Import packages
from sqlalchemy import create_engine
import pandas as pd

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM Album", engine)
```

Inner joins
```
# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute("SELECT Title, Name FROM Album INNER JOIN Artist ON Album.ArtistID = Artist.ArtistID")
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print head of DataFrame df
print(df.head())
```
```
# Execute query and store records in DataFrame: df
df = pd.read_sql_query("SELECT * FROM PlaylistTrack INNER JOIN Track on PlaylistTrack.TrackId = Track.TrackId WHERE Milliseconds < 250000", engine)

# Print head of DataFrame
print(df.head())
```

Checking tables with pandas
```
# What are the headers and data in the table
print(table.head())
# Show me 4 rows of data with headers
print(table.head(4))
# How many rows and columns are there
print(table.shape)
# Just show me the headers with no data
print(table.columns)
```

Joining tables with pandas
 ```
 # This will only return rows where values match in both tables
 wards_census = wards.merge(census, on='ward', suffixes=('_ward','_cen'))
 print(wards_census.head())
 ```
 ```
 # Merge the taxi_owners and taxi_veh tables setting a suffix
taxi_own_veh = taxi_owners.merge(taxi_veh, on='vid', suffixes=('_own','_veh'))

# Print the value_counts to find the most popular fuel_type
print(taxi_own_veh['fuel_type'].value_counts())
```
```
# Merge the licenses and biz_owners table on account
licenses_owners = licenses.merge(biz_owners, on='account')

# Group the results by title then count the number of accounts
counted_df = licenses_owners.groupby('title').agg({'account':'count'})

# Sort the counted_df in desending order
sorted_df = counted_df.sort_values(by='account', ascending=False)

# Use .head() method to print the first few rows of sorted_df
print(sorted_df.head())
```

Joining multiple tables (pandas)
```
# Merge the ridership, cal, and stations tables
ridership_cal_stations = ridership.merge(cal, on=['year','month','day']) \
# A backslash makes python read these two as one line of code
							.merge(stations, on='station_id')

# Create a filter to filter ridership_cal_stations
filter_criteria = ((ridership_cal_stations['month'] == 7) 
                   & (ridership_cal_stations['day_type'] == 'Weekday') 
                   & (ridership_cal_stations['station_name'] == 'Wilson'))

# Use .loc and the filter to select for rides
print(ridership_cal_stations.loc[filter_criteria, 'rides'].sum())
```

Left, right, outer joins
```
movies_financials = movies.merge(financials, on='id', how='left')
#Count missing rows in budget column
number_of_missing_fin = movies_financials['budget'].isnull().sum()
```

```
action_scifi = action_movies.merge(scifi_movies, on='movie_id', how='right',
                                   suffixes=('_act','_sci'))
scifi_only = action_scifi[action_scifi['genre_act'].isnull()]
movies_and_scifi_only = movies.merge(scifi_only, left_on='id', right_on='movie_id')
```

```
# Merge iron_1_actors to iron_2_actors on id with outer join using suffixes
iron_1_and_2 = iron_1_actors.merge(iron_2_actors,
                                     how='outer',
                                     on='id',
                                     suffixes=('_1','_2'))

# Create an index that returns true if name_1 or name_2 are null
m = ((iron_1_and_2['name_1'].isnull()) | 
     (iron_1_and_2['name_2'].isnull()))

# Print the first few rows of iron_1_and_2
print(iron_1_and_2[m].head())
```

Inner joins
```
original_sequels = sequels.merge(sequels, left_on='sequel', right_on='id', suffixes=('_org','_seq'))
print(original_sequels.head())
```

```
# Create a Boolean index, named boolean_filter, that selects rows from the left table with the job of 'Director' and avoids rows with the job of 'Director' in the right table
crews_self_merged = crews.merge(crews, on='id', how='inner',
                                suffixes=('_dir','_crew'))
boolean_filter = ((crews_self_merged['job_dir'] == 'Director') & 
                  (crews_self_merged['job_crew'] != 'Director'))
direct_crews = crews_self_merged[boolean_filter]
```

```
# Merging on indexes
orig_seq = sequels_fin.merge(sequels_fin, how='inner', left_on='sequel', 
                             right_on='id', right_index=True,
                             suffixes=('_org','_seq'))
orig_seq['diff'] = orig_seq['revenue_seq'] - orig_seq['revenue_org']
titles_diff = orig_seq[['title_org','title_seq','diff']]
```

Filtering + anti joins (isin, indicator=, .loc)

```
# Anti join
empl_cust = employees.merge(top_cust, on='srid', 
                            how='left', indicator=True)
srid_list = empl_cust.loc[empl_cust['_merge'] == 'left_only', 'srid']
print(employees[employees['srid'].isin(srid_list)])
```

```
# Merge the non_mus_tck and top_invoices tables on tid
tracks_invoices = non_mus_tcks.merge(top_invoices, on='tid')

# Use .isin() to subset non_mus_tcsk to rows with tid in tracks_invoices
top_tracks = non_mus_tcks[non_mus_tcks['tid'].isin(tracks_invoices['tid'])]

# Group the top_tracks by gid and count the tid rows
cnt_by_gid = top_tracks.groupby(['gid'], as_index=False).agg({'tid':'count'})

# Merge the genres table to cnt_by_gid on gid and print
print(cnt_by_gid.merge(genres, on='gid'))
```

Vertical concatenation
```
# Concatenate the tracks
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                               sort=True)
print(tracks_from_albums)

# Concat tracks so index goes from 0 to n-1
tracks_from_albums = pd.concat([tracks_master,tracks_ride,tracks_st],
                               ignore_index=True,
                               sort=True)
print(tracks_from_albums)

# Concat showing column names in all tables
tracks_from_albums = pd.concat([tracks_master, tracks_ride, tracks_st],
                               join=('inner'),
                               sort=True)
print(tracks_from_albums)
```

```
# Concat with keys
inv_jul_thr_sep = pd.concat([inv_jul, inv_aug, inv_sep], 
                            keys=['7Jul','8Aug','9Sep'])
avg_inv_by_month = inv_jul_thr_sep.groupby(level=0).agg({'total':'mean'})
avg_inv_by_month.plot(kind='bar')
plt.show()
```

```
# Use the .append() method to combine the tracks tables
metallica_tracks = tracks_ride.append([tracks_master,tracks_st], sort=False)

# Merge metallica_tracks and invoice_items
tracks_invoices = metallica_tracks.merge(invoice_items, on='tid', how='inner')

# For each tid and name sum the quantity sold
tracks_sold = tracks_invoices.groupby(['tid','name']).agg({'quantity':'sum'})

# Sort in decending order by quantity and print the results
print(tracks_sold.sort_values(['quantity'],ascending=False))
```

Validate= and Verify_integrity=
```
# Concatenate the classic tables vertically
classic_18_19 = pd.concat([classic_18, classic_19], ignore_index=True)

# Concatenate the pop tables vertically
pop_18_19 = pd.concat([pop_18, pop_19], ignore_index=True)

# Merge classic_18_19 with pop_18_19
classic_pop = classic_18_19.merge(pop_18_19,on='tid',how='inner')

# Using .isin(), filter classic_18_19 rows where tid is in classic_pop
popular_classic = classic_18_19[classic_18_19['tid'].isin(classic_pop['tid'])]

# Print popular chart
print(popular_classic)
```
