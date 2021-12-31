SELECT avg(yelp_review.stars) , yelp_review.date, weather_data.city
FROM yelp_review
JOIN yelp_business
ON yelp_business.business_id = yelp_review.business_id
join weather_data
ON weather_data.date = yelp_review.date
group by yelp_review.date