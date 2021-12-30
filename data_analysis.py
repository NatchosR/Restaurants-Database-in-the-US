"""
Analysis: Plot, Regression, ...
"""

# IMPORT
import pandas as pd
import matplotlib.pyplot as plt

# EXTRACT
df_LV=pd.read_csv('generated_data/daily_LV.csv', header=0)


# Regression




# PLOT
mydata_df['date']=pd.to_datetime(mydata_df['date'], format='%Y-%m-%d')

x=mydata_df['date']
y1=mydata['avg_stars']
y2=mydata['precipitation']

# PLOT
fig, ax1=plt.subplots()

color= 'tab:red'
ax1.set_xlabel('date')
ax1.set_ylabel('avg_stars', color=color)
ax1.plot(x, y1, color=color, label='avg_stars')
ax1.tick_params(axis='y', labelcolor=color)

ax2=ax1.twinx()

color='tab:blue'
ax2.set_ylabel('precipitation', color=color)
ax2.plot(x, y2, color=color, label='precipitation')
ax2.tick_params(axis='y', labelcolor=color)

fig.title='Average Stars, Precipitation in Las Vegas'
fig.legend()

plt.show()

