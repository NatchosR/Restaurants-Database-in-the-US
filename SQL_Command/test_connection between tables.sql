SELECT weather_data.date, weather_data.city, yelp_business.name, yelp_review.stars
FROM yelp_review
JOIN yelp_business
ON yelp_review.business_id = yelp_business.business_id
JOIN weather_data
ON yelp_review.date = weather_data.date
WHERE
yelp_business.city=weather_data.city
;
