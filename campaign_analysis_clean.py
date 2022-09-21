# Importing packages to use, reading data to dataframe, creating SQL engine for later

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import pandas as pd
import numpy as np

xls = pd.ExcelFile('/kaggle/input/campaign-data/Campaign Data.xlsx')

df = pd.read_excel('/kaggle/input/campaign-data/Campaign Data.xlsx')

df.head() # What does my data look like?


# Getting a basic overview of the data

print(print("df shape:",df.shape) # 33,370 rows, 8 columns
      
df.info() # There are 33,964 rows with missing sight test date and spend data

# What information do I have about customer type?
      
print('Values in Customer ID:', df['Customer ID'].unique())
print('Values in Mailing Date:',df['Mailing Date'].unique())
print('Values in Campaign Test Group:',df['Campaign Test Group'].unique())
print('Values in Gender:',df.Gender.unique())
print('Values in Ageband:',df.Ageband.unique())
print('Values in Segment:',df.Segment.unique())
print('Values in Sight Tests:',df['Sight Tests'].unique())

# Rename columns for consistency
      
df = xls.parse(0, names=['id','send_date','campaign_group','gender','ageband','segment','test_flag','test_date','spend'])
print(df.head())
      
df.drop(df[(df.test_flag == 0) & (df.test_date.notnull())].index,inplace=True)
# Drop rows where sight test is marked as no but there is a sight test date
      
df.drop(df[(df.test_flag == 1) & (df.test_date.isnull())].index,inplace=True)
# Drop rows where sight test is marked as yes but there is not a sight test date

# Add days_elapsed column and populate
      
df['days_elapsed'] = np.nan
df['days_elapsed'] = (df['test_date'] - df['send_date']).dt.days
      
# Make values for 'ageband' all strings
      
df.replace("Adults", 
           "Adult", 
           inplace=True)
df.replace("Kids", 
           "Child", 
           inplace=True)
df.replace("60+", 
           "Senior", 
           inplace=True)
print('Values in Ageband:',df.ageband.unique())
      
      
# Conversion rates
      
live_total_ids = df[df["campaign_group"] == "Live"]['id']
live_booked = df[(df["test_flag"] == 1) & (df["campaign_group"] == "Live")]['id']
l_conv_rate = (live_booked.nunique())/(live_total_ids.nunique()) 
print(round(l_conv_rate*100, 2), "%") # Conversion rate for Live group is 2.36%
      
ctrl_total_ids = df[df["campaign_group"] == "Control"]['id']
ctrl_booked = df[(df["test_flag"] == 1) & (df["campaign_group"] == "Control")]['id']
c_conv_rate = (ctrl_booked.nunique())/(ctrl_total_ids.nunique()) 
print(round(c_conv_rate*100, 2), "%") # Conversion rate for Control group is 1.71%   
    
      
# Average spends
      
live_spends = df[df["campaign_group"] == "Live"]['spend'] # Total spend from Live
sum_l_spend = live_spends.sum()
print(sum_l_spend)
no_l_spends = live_spends.count()
print(no_l_spends)
print(sum__spend/no_l_spends) # The average spend for live campaign was £109.63
      
ctrl_spends = df[df["campaign_group"] == "Control"]['spend'] # Total spend from Control
sum_c_spend = ctrl_spends.sum()
print(sum_c_spend)
no_c_spends = ctrl_spends.count()
print(no_c_spends)
print(sum_c_spend/no_c_spends) # The average spend for control was £116.36
      

# Days to book
      
# Calculate average days to book - live
live_days = df[(df["test_flag"] == 1) & (df["campaign_group"] == "Live")]['days_elapsed']
avg_l_days = live_days.mean()
print(avg_l_days) # Live bookers took an average of 16.99 days after send to book a st 
      
# Calculate average days to book - control
ctrl_days = df[(df["test_flag"] == 1) & (df["campaign_group"] == "Control")]['days_elapsed']
avg_c_days = ctrl_days.mean()
print(avg_c_days) # Control bookers booked an average of 18.48 days after the send
      
      
# Customer breakdown pivot tables
      
st_by_demographic = df.pivot_table(index=['campaign_group','gender','ageband','segment'], values=['test_flag'], aggfunc='sum')
# Number of sight tests by live/control, gender, age, and group
print(st_by_demographic)
st_by_demographic.plot(type='pie')
      
# Bar Charts of bookings by segment
      
df.pivot_table(index=['campaign_group'],columns='segment',values=['test_flag'], aggfunc='sum').plot(kind='bar')
# Create a bar chart showing count of sight tests by customer segment, for control and live campaign groups
# Can see by a significant amount that Group A has most bookings
df.pivot_table(index=['campaign_group'],columns='gender',values=['test_flag'], aggfunc='sum').plot(kind='bar')
df.pivot_table(index=['campaign_group'],columns='ageband',values=['test_flag'], aggfunc='sum').plot(kind='bar')
