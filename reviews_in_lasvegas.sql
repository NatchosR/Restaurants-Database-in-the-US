select weather_data.date, yelp_review.stars, avg_temp, name, categories
from weather_data, yelp_business, yelp_review
where weather_data.date = yelp_review.date
AND yelp_review.business_id = yelp_business.business_id
AND yelp_business.city = 'Las Vegas'
AND weather_data.date >= '2017-01-01'
order by date
