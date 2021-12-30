"""
This script connects SQL Server to PyCharm, to generate dataset
"""

import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
 host = "db-vm-25.el.eee.intern",database='yelp_db',
 user = "admin", passwd = "Theteam")

sql_query_1=("""
        SELECT yelp_review.date,yelp_business.city, count(yelp_review.review_id), AVG(yelp_review.stars), 
        weather_data.diff_precipitation, weather_data.avg_temp
        FROM weather_data, yelp_business, yelp_review
        WHERE weather_data.date = yelp_review.date
        AND yelp_review.business_id = yelp_business.business_id
        AND yelp_business.city=weather_data.city
        AND yelp_business.city = 'Charlotte'
        AND weather_data.date >= '2015-01-01'
        GROUP BY weather_data.date
        ORDER BY date
        """)

sql_query_2=("""
        SELECT yelp_review.date,yelp_business.city, yelp_business.name, AVG(yelp_review.stars), 
        weather_data.diff_precipitation,weather_data.avg_temp
        FROM weather_data, yelp_business, yelp_review
        WHERE weather_data.date = yelp_review.date
        AND yelp_review.business_id = yelp_business.business_id
        AND yelp_business.city = 'Las Vegas'
        AND yelp_business.name like '%Starbucks%'
        AND weather_data.date >= '2015-01-01'
        group by weather_data.date
        order by date
""")

mydata = pd.read_sql(sql=sql_query_1, con=mydb)
mydata_df = pd.DataFrame(mydata)
mydata_df.columns = ['date','city','count_review','avg_stars',
                     'diff_precip','avg_temp']
mydata_df.to_csv("generated_data/daily_CHA.csv", index=False)
print(mydata_df)

