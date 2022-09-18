import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import pandas as pd
import numpy as np
from sqlalchemy import create_engine
from scipy import stats
import matplotlib.pyplot as plt # to create visualisations
%matplotlib inline
import seaborn as sns

df = pd.read_excel('/kaggle/input/campaign-data/Campaign Data.xlsx')

engine = create_engine('sqlite://', echo=False)
df.to_sql("customers", con=engine)

df.head()

print("df shape:",df.shape)
df.info()
# There are 33,964 rows with missing sight test date and spend data - I need to clean this
# This indicates that 33,964 customers did not have a sight test after they received our campaign
df.describe()
# This is not that helpful as lots of these fields are strings. The averages for spend may be useful
# Off the back of this campaign, customers spent a total of £2,124.00
# The average customer spend was £106.02. Some customers spent £0 and one customer spent £628.00

print('Values in Customer ID:', df['Customer ID'].unique())
print('Values in Mailing Date:',df['Mailing Date'].unique())
print('Values in Campaign Test Group:',df['Campaign Test Group'].unique())
print('Values in Gender:',df.Gender.unique())
print('Values in Ageband:',df.Ageband.unique())
print('Values in Segment:',df.Segment.unique())
print('Values in Sight Tests:',df['Sight Tests'].unique())
print('Values in Sight Test Date:',df['Sight Test Date'].unique())
print('Values in Spend:', df.Spend.unique())

# This helps me see that the ageband data is not all by age so may be difficult to create a model
# What are the segments? Are they equal?

sight_test = df['Sight Tests'].tolist() # make the sight test column a list

had_st = sight_test.count(1) # there were 2124 sight tests booked
print(had_st)

test_grp = df['Campaign Test Group'].tolist()

live = test_grp.count('Live')
print(live) # there were 32,479 customers sent the email

control = test_grp.count('Control')
print(control) # 3609 customers were not sent the email

# Of customers sent email, what % had a sight test?

pd.DataFrame(df.groupby(['Campaign Test Group','Sight Tests'])['Customer ID'].count()).apply(lambda x : x / sum(x) * 100)
# pd.DataFrame(df.groupby(['Campaign Test Group','Sight Tests'])['Customer ID'].count())
# all of these add up to 100 I want to split this by % of ctrl and % of live

cnt_sent_email = engine.execute("SELECT COUNT([Customer ID]) FROM customers WHERE [Campaign Test Group] = 'Live' AND [Sight Tests] = 1 AND [Sight Test Date] IS NOT NULL")

result1 = pd.DataFrame(cnt_sent_email.fetchall())
result1.columns = result1.keys()

print(result1) # 707 customers booked sight tests from Live campaign between 27th and 28th Feb

print(result1 / live * 100) # 2.18% of customers who were sent the campaign booked between 27th and 28th Feb

cnt_no_email = engine.execute("SELECT COUNT([Customer ID]) FROM customers WHERE [Campaign Test Group] = 'Control' AND [Sight Tests] = 1 AND [Sight Test Date] IS NOT NULL")

result2 = pd.DataFrame(cnt_no_email.fetchall())
result2.columns = result2.keys()

print(result2) # 58 customers booked sight tests from Control campaign between 27th and 28th Feb

print(result2 / live * 100) # 0.18% of customers who were NOT sent the campaign booked between 27th and 28th Feb

# Null hypothesis: the campaign has no effect on sight test booking
# Alternative hypothesis: customers sent the campaign are more likely to book a sight test than customers not sent the campaign
# the lower the p value the less likely it is that results are due to chance
# if the p value is under .05 we will reject the null hypothesis

# to think about - the columns with missing sight test date. assuming this means the cx did not attend in the period 27th jan and 28th feb

# can't work out roi
# conversion rate is what i've worked out above

# average spend

c_liv_av_sd = engine.execute("SELECT AVG([Spend]) FROM customers WHERE [Campaign Test Group] = 'Live' AND [Sight Tests] = 1 AND [Sight Test Date] IS NOT NULL")

c_ctl_av_sd = engine.execute("SELECT AVG([Spend]) FROM customers WHERE [Campaign Test Group] = 'Control' AND [Sight Tests] = 1 AND [Sight Test Date] IS NOT NULL")

liv_av_sd = pd.DataFrame(c_liv_av_sd.fetchall())
liv_av_sd.columns = liv_av_sd.keys()


ctl_av_sd = pd.DataFrame(c_ctl_av_sd.fetchall())
ctl_av_sd.columns = ctl_av_sd.keys()

print(liv_av_sd) # Live customers spent avg of £109.63
print(ctl_av_sd) # Control customers spent avg £116.36 on avg

# types of cus with best response - overall (no relation to ctrl or live)

print(df)
df.drop

gender = df.groupby('Gender')['Sight Tests'].value_counts(normalize=True).unstack().plot(kind='bar', figsize=(5,10))
gender.set_title("count appts made/not by gender")
plt.show()

# very slightly, females were the most likely to respond to this campaign by having a sight test

# age = 

# segment = 
