"""
In this script, we will analyse the famous restaurants Starbucks,
so we can see if customers behavior change according to the cities.
"""

# IMPORT
import pandas as pd
import matplotlib.pyplot as plt

# EXTRACT
df_LV=pd.read_csv('generated_data/starbucks_LV.csv')
df_CHA=pd.read_csv('generated_data/starbucks_CHA.csv')

df_LV['date']=pd.to_datetime(df_LV['date'])
df_CHA['date']=pd.to_datetime(df_CHA['date'])

# PLOT Las Vegas
df_LV_1y=df_LV[df_LV.date.between('2017-01-01','2017-12-31')]
x=df_LV_1y['date']
avg_star_LV=df_LV_1y['avg_stars']
moving_avg_star=avg_star_LV.rolling(window=7).mean()
avg_precip_LV=df_LV_1y['diff_precip']
moving_avg_precip=avg_precip_LV.rolling(window=7).mean()


fig, ax1=plt.subplots()

color= 'tab:red'
ax1.set_xlabel('date')
ax1.set_ylabel('avg_stars', color=color)
ax1.plot(x, avg_star_LV, color=color, label='avg_stars', alpha=0.5)
ax1.plot(x, moving_avg_star, color=color, label='moving_avg_stars')
ax1.tick_params(axis='y', labelcolor=color)

ax2=ax1.twinx()

color='tab:blue'
ax2.set_ylabel('precipitation', color=color)
ax2.plot(x, avg_precip_LV, color=color, label='precipitation', alpha=0.5)
ax2.plot(x, moving_avg_precip, color=color, label='moving_avg_precipitation')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Average Stars, Precipitation in Las Vegas for Starbucks (2017)', fontsize=16)
fig.legend()

plt.show()


# PLOT Charlotte
df_CHA_1y=df_CHA[df_CHA.date.between('2017-01-01','2017-12-31')]
x=df_CHA_1y['date']
avg_star_CHA=df_CHA_1y['avg_stars']
moving_avg_star=avg_star_CHA.rolling(window=7).mean()
avg_precip_CHA=df_CHA_1y['diff_precip']
moving_avg_precip=avg_precip_CHA.rolling(window=7).mean()


fig, ax1=plt.subplots()

color= 'tab:red'
ax1.set_xlabel('date')
ax1.set_ylabel('avg_stars', color=color)
ax1.plot(x, avg_star_CHA, color=color, label='avg_stars', alpha=0.5)
ax1.plot(x, moving_avg_star, color=color, label='moving_avg_stars')
ax1.tick_params(axis='y', labelcolor=color)

ax2=ax1.twinx()

color='tab:blue'
ax2.set_ylabel('precipitation', color=color)
ax2.plot(x, avg_precip_CHA, color=color, label='precipitation', alpha=0.5)
ax2.plot(x, moving_avg_precip, color=color, label='moving_avg_precipitation')
ax2.tick_params(axis='y', labelcolor=color)

plt.title('Average Stars, Precipitation in Charlotte for Starbucks (2017)', fontsize=16)
fig.legend()

plt.show()


# DATA MANIPULATION
frames=[df_LV, df_CHA]
df_full=pd.concat(frames)
df_full.drop_duplicates(inplace=True)

df_full_index=df_full.reset_index()

# date
df_full_date=df_full
df_full_date['date']=pd.to_datetime(df_full_date['date'])
df_full_date=df_full_date.sort_values('date')

# ANALYSIS
df_boxplot=df_full[['city','avg_stars']]
df_boxplot.boxplot(by='city', fontsize=12)
plt.title('AVG stars for Starbucks', fontsize=14)
plt.show()





