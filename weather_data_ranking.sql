USE yelp_db;
select city, avg(avg_temp), avg(diff_precipitation)
from weather_data
group by city
order by avg(avg_temp) DESC;