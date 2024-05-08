select yelp_business.city, avg(stars), avg(avg_temp), avg(diff_precipitation)
from yelp_business, weather_data
where yelp_business.city = weather_data.city
Group by city
order by avg(stars) DESC;

