"""
Clean and join all precipitation csv files
"""

# IMPORT
import pandas as pd
from datetime import datetime as dt

# EXTRACT
df_precip_PIT=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/precip_PIT.csv', header=0)
df_temp_PIT=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/temp_PIT.csv', header=0)
df_precip_CHA=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/precip_CHA.csv', header=0)
df_temp_CHA=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/temp_CHA.csv', header=0)
df_precip_CLE=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/precip_CLE.csv', header=0)
df_temp_CLE=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/temp_CLE.csv', header=0)
df_precip_PHO=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/precip_PHO.csv', header=0)
df_temp_PHO=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/temp_PHO.csv', header=0)
df_precip_LV=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/precip_LV.csv', header=0)
df_temp_LV=pd.read_csv('C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/data/temp_LV.csv', header=0)


# PART 1: Basic Cleaning

# 1.1 Format date
def format_df(df):
    df['date']=pd.to_datetime(df['date'], format='%Y%m%d', errors='raise').dt.normalize()
    for col in df.columns:
        if col=='date':
            pass
        else:
            df[col] = pd.to_numeric(df[col], errors='coerce')


format_df(df_precip_PIT)
format_df(df_precip_CHA)
format_df(df_precip_CLE)
format_df(df_precip_PHO)
format_df(df_precip_LV)
format_df(df_temp_PIT)
format_df(df_temp_CHA)
format_df(df_temp_CLE)
format_df(df_temp_PHO)
format_df(df_temp_LV)


# 1.2 Start in 2008, end in 2017
def filter_date(df):
    start_date=pd.to_datetime('2008-01-01')
    end_date=pd.to_datetime('2017-12-31')
    df=df[df.date.between(start_date,end_date)]
    return df


df_precip_PIT=filter_date(df_precip_PIT)
df_precip_CHA=filter_date(df_precip_CHA)
df_precip_CLE=filter_date(df_precip_CLE)
df_precip_PHO=filter_date(df_precip_PHO)
df_precip_LV=filter_date(df_precip_LV)
df_temp_PIT=filter_date(df_temp_PIT)
df_temp_CHA=filter_date(df_temp_CHA)
df_temp_CLE=filter_date(df_temp_CLE)
df_temp_PHO=filter_date(df_temp_PHO)
df_temp_LV=filter_date(df_temp_LV)

# 1.3 Add the city
def add_city(df, city):
    df['city']=city
    first_column=df.pop('city')
    df.insert(1,'city',first_column)


add_city(df_precip_PIT,'Pittsburgh')
add_city(df_temp_PIT,'Pittsburgh')
add_city(df_precip_CHA,'Charlotte')
add_city(df_temp_CHA,'Charlotte')
add_city(df_precip_CLE,'Cleveland')
add_city(df_temp_CLE,'Cleveland')
add_city(df_precip_PHO,'Phoenix')
add_city(df_temp_PHO,'Phoenix')
add_city(df_precip_LV, 'Las Vegas')
add_city(df_temp_LV, 'Las Vegas')

# 1.4 Change name of temperature data
def change_column_names(df):
    df.columns=['date','city','temp_min','temp_max','temp_normal_min','temp_normal_max']


change_column_names(df_temp_PIT)
change_column_names(df_temp_CHA)
change_column_names(df_temp_CLE)
change_column_names(df_temp_PHO)
change_column_names(df_temp_LV)

# Part 2: advanced cleaning (see weather_data_clean2.py for more details)

# 2.1 differentiate cumulative precipitation
def diff_cumulative_precip(df):
    year=[g for n,g in df.groupby(pd.Grouper(key='date',freq='Y'))]
    for y in year:
        diff_precip=y['precipitation'].diff()
        y.insert(2,'diff_precipitation',diff_precip)
    df_diff=pd.concat(year)
    df_diff.reset_index(drop=True, inplace=True)
    return df_diff

df_precip_PIT_diff=diff_cumulative_precip(df_precip_PIT)
df_precip_CHA_diff=diff_cumulative_precip(df_precip_CHA)
df_precip_ClE_diff=diff_cumulative_precip(df_precip_CLE)
df_precip_PHO_diff=diff_cumulative_precip(df_precip_PHO)
df_precip_LV_diff=diff_cumulative_precip(df_precip_LV)

# 2.2 average temperature
def avg_temperature(df):
    df['avg_temp']=(df['temp_max']+df['temp_min'])/2
    df['avg_temp_normal']=(df['temp_normal_max']+df['temp_normal_min'])/2
    return df

df_temp_PIT=avg_temperature(df_temp_PIT)
df_temp_CHA=avg_temperature(df_temp_CHA)
df_temp_CLE=avg_temperature(df_temp_CLE)
df_temp_PHO=avg_temperature(df_temp_PHO)
df_temp_LV=avg_temperature(df_temp_LV)


# Join data of same cities
df_PIT=pd.merge(df_precip_PIT_diff,df_temp_PIT, how='left', on=['date', 'city'])
df_CHA=pd.merge(df_precip_CHA_diff,df_temp_CHA, how='left', on=['date', 'city'])
df_CLE=pd.merge(df_precip_ClE_diff,df_temp_CLE, how='left', on=['date', 'city'])
df_PHO=pd.merge(df_precip_PHO_diff,df_temp_PHO, how='left', on=['date', 'city'])
df_LV=pd.merge(df_precip_LV_diff,df_temp_LV, how='left', on=['date', 'city'])

df_concat1=pd.concat([df_PIT,df_CHA])
df_concat2=pd.concat([df_CLE,df_PHO])
df_concat3=pd.concat([df_concat1,df_concat2])
df_weather=pd.concat([df_concat3,df_LV])


# 2.3 include season
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


season=df_weather.date.map(season_of_date)
df_weather.insert(1,'season',season)


# Export as csv
df_weather.to_csv('data/weather_data.csv', index=False)
