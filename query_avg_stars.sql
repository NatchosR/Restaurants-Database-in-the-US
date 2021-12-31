SELECT table1.city, table1.year, table1.season, table1.AVG_stars_city, table1.AVG_precip_city, table1.AVG_temp_city
FROM ( SELECT weather_data.city, weather_data.year,weather_data.season, AVG(yelp_review.stars) as AVG_stars_city,
 AVG(weather_data.precipitation) as AVG_precip_city, AVG(weather_data.avg_temp) as AVG_temp_city
 FROM yelp_review, weather_data
 WHERE yelp_review.date=weather_data.date
 GROUP BY weather_data.city, weather_data.date) table1
GROUP BY table1.season
ORDER BY table1.year ASC