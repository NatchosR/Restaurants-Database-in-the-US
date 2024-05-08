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
        y.insert(2,'diff_precipitation',diff_precip)
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

# avg temperature (we will work with Cleveland data set)
x=CLE_2015['date']
y1=CLE_2015['temp_max']
y2=CLE_2015['temp_min']
yy1=CLE_2015['temp_normal_max']
yy2=CLE_2015['temp_normal_min']
plt.fill_between(x, y1, y2, label='effective temperature', color='blue', alpha=0.7)
plt.fill_between(x, yy1, yy2, label='normal temperature', color='lightblue', alpha=0.5)
plt.legend()

def avg_temperature(df):
    avg_temp=(df['temp_max']+df['temp_min'])/2
    df.insert(5,'avg_temp',avg_temp)
    avg_temp_normal=(df['temp_normal_max']+df['temp_normal_min'])/2
    df.insert(6,'avg_temp_normal',avg_temp_normal)
    return df


CLE_data1=avg_temperature(CLE_diff)
CLE_2015=avg_temperature(CLE_2015)

x=CLE_2015['date']
y1=CLE_2015['temp_max']
y2=CLE_2015['temp_min']
yy1=CLE_2015['temp_normal_max']
yy2=CLE_2015['temp_normal_min']
y_avg1=CLE_2015['avg_temp']
y_avg2=CLE_2015['avg_temp_normal']
plt.fill_between(x, y1, y2, label='effective temperature', color='blue', alpha=0.7)
plt.fill_between(x, yy1, yy2, label='normal temperature', color='lightblue', alpha=0.5)
plt.plot(x,y_avg1, label='average temperature', color='red', alpha=0.6)
plt.plot(x,y_avg2, label='average normal temperature', color='orange', alpha=0.5)
plt.legend()

# include season


def season_of_date(date):
    year = str(date.year)
    seasons = {'spring': pd.date_range(start='21/03/'+year, end='20/06/'+year),
               'summer': pd.date_range(start='21/06/'+year, end='22/09/'+year),
               'autumn': pd.date_range(start='23/09/'+year, end='20/12/'+year)}
    if date in seasons['spring']:
        return 'spring'
    if date in seasons['summer']:
        return 'summer'
    if date in seasons['autumn']:
        return 'autumn'
    else:
        return 'winter'


season=CLE_data1.date.map(season_of_date)
CLE_data1.insert(1,'season',season)








