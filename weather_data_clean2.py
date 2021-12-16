"""
Some modifications about weather data. We will apply those modification only to Las Vegas dataframe as an example.
The real cleaning will be made in the cleaning_joining_csv_precip.py

1. precipitation cumulative -> daily
2. add avg temperature
3. add the seasons
"""

# IMPORT
import pandas as pd
import matplotlib.pyplot as plt

# EXTRACT
weather_data=pd.read_csv('data/weather_data.csv', header=0)
weather_data.head()

# CLEANING

# some manipulations first
weather_data['date']=pd.to_datetime(weather_data['date'], format='%Y-%m-%d').dt.normalize()
print(weather_data.dtypes)
# seems like there is an issue with the precipitation
weather_data['precipitation']=pd.to_numeric(weather_data['precipitation'], errors='coerce')
print(weather_data.head())

# 1. daily precipitation
# create a dataframe for Las Vegas
LV_data=weather_data[weather_data['city']=='Las Vegas']
print(LV_data.head())

# plot to understand the problem
plt.plot(LV_data['date'],LV_data['precipitation'])

# solve the problem
# first we got to differentiate the year as the data are cumulative on a yearly basis
year=[g for n,g in LV_data.groupby(pd.Grouper(key='date', freq='Y'))]
print(len(year))
year1=year[0]
year_2016=year[12]

# plot to see the before and the after
plt.plot(year_2016['date'],year_2016['precipitation'], label='cumulative precipitation')
plt.plot(year_2016['date'],year_2016['precipitation_normal'], label='cumulative precipitation normal')

# Now let's differentiate
year_2016['diff_precip']=year_2016['precipitation'].diff()
year_2016['diff_precip_normal']=year_2016['precipitation_normal'].diff()

print(year_2016.head())
plt.plot(year_2016['date'],year_2016['precipitation'], label='precipitation')
plt.plot(year_2016['date'],year_2016['precipitation_normal'], label='precipitation normal')
plt.plot(year_2016['date'],year_2016['diff_precip'], label='differentiate precipitation')
plt.plot(year_2016['date'],year_2016['diff_precip_normal'], label='differentiate precipitation normal')

plt.legend()

# Now we have the correct result, let's build a function to apply to all dataset.


def diff_cumulative_precip(df):
    year=[g for n,g in df.groupby(pd.Grouper(key='date', freq='Y'))]
    for y in year:
        diff_precip=y['precipitation'].diff()
        y.insert(3,'diff_precipitation',diff_precip)
        y['diff_precipitation_normal']=y['precipitation_normal'].diff()
    df_diff=pd.concat(year)
    df_diff.reset_index(drop=True, inplace=True)
    return df_diff


# Try the function on Cleveland
CLE_data=weather_data[weather_data['city']=='Cleveland']
CLE_diff=diff_cumulative_precip(CLE_data)
print(CLE_diff.dtypes)
CLE_2015=CLE_diff[CLE_diff.date.between('2015-01-01','2015-12-31')]
plt.plot(CLE_2015['date'], CLE_2015['precipitation'], label='precipitation')
plt.plot(CLE_2015['date'], CLE_2015['precipitation_normal'], label='normal precipitation')
plt.plot(CLE_2015['date'], CLE_2015['diff_precipitation'], label='differentiate precipitation')
plt.plot(CLE_2015['date'], CLE_2015['diff_precipitation_normal'], label='differentiate normal precipitation')
plt.legend()

# Try the function on Charlotte
CHA_data=weather_data[weather_data['city']=='Charlotte']
CHA_diff=diff_cumulative_precip(CHA_data)
print(CHA_diff.dtypes)
CHA_2015=CHA_diff[CLE_diff.date.between('2015-01-01','2015-12-31')]
plt.plot(CHA_2015['date'], CHA_2015['precipitation'], label='precipitation')
plt.plot(CHA_2015['date'], CHA_2015['precipitation_normal'], label='normal precipitation')
plt.plot(CHA_2015['date'], CHA_2015['diff_precipitation'], label='differentiate precipitation')
plt.plot(CHA_2015['date'], CHA_2015['diff_precipitation_normal'], label='differentiate normal precipitation')
plt.legend()


# avg temperature



# season


