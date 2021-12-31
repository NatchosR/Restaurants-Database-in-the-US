SELECT yelp_user.name, AVG(yelp_review.stars) AS avg_rating_on_resturant,
 yelp_user.average_stars, yelp_user.review_count, yelp_review.review_id
FROM yelp_user, yelp_review, yelp_business
WHERE yelp_review.business_id = yelp_business.business_id
AND yelp_review.user_id = yelp_user.user_id
AND city = 'Las Vegas'
AND yelp_business.name = '"""Gordon Ramsay BurGR"""'
AND date >= '2017-01-01'
AND yelp_user.review_count>=100
GROUP BY yelp_user.name
ORDER BY AVG(yelp_review.stars) ASC