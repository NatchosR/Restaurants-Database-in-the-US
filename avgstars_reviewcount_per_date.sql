USE yelp_db;
select avg(yelp_review.stars), yelp_review.date, name, yelp_business.city, count(review_id) as review_count, avg_temp
From yelp_review, yelp_business, weather_data
where yelp_review.business_id = yelp_business.business_id
AND weather_data.city = yelp_business.city
AND weather_data.date = yelp_review.date
group by yelp_review.business_id
order by count(review_id) DESC