SELECT yelp_review.date, yelp_business.city, count(yelp_review.review_id), AVG(yelp_review.stars), AVG(weather_data.diff_precipitation), AVG(weather_data.avg_temp)
FROM yelp_business, yelp_review, weather_data
WHERE yelp_business.business_id=yelp_review.business_id
AND yelp_review.date=weather_data.date
AND yelp_business.city='Phoenix'
GROUP BY yelp_review.date
ORDER BY yelp_review.date, yelp_business.city