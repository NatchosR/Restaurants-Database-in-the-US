import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

mydb = mysql.connector.connect(
 host = "db-vm-25.el.eee.intern",database='yelp_db',
 user = "admin", passwd = "Theteam")

sql_q1=("""
        SELECT avg(yelp_review.stars), yelp_review.date, yelp_business.city, weather_data.precipitation,
        weather_data.temp_min, weather_data.temp_max
        FROM yelp_db.yelp_review , yelp_business, weather_data
        WHERE yelp_review.business_id=yelp_business.business_id 
        AND weather_data.date=yelp_review.date
        AND yelp_business.city='Las Vegas'
        GROUP BY yelp_review.date
        ORDER BY yelp_review.date
        """)

sql_q2=""

mydata = pd.read_sql(sql=sql_q1, con=mydb)
mydata_df = pd.DataFrame(mydata)
mydata_df.columns = ['avg_stars', 'date', 'city','precipitation','temp_min','temp_max']
mydata_df.to_csv("C:/Users/natr/Desktop/HSLU_S2/DBM/project/py_charm/generated_data/avg_stars_daily_LV.csv", index=False)
print(mydata_df)

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


#print(plotnine.ggplot(mydata_df)
# + plotnine.aes(x = 'name', y = 'n', fill = 'kpi')
# + plotnine.geom_col(position = "dodge")
# + plotnine.scale_y_continuous(limits = [0,13]) )