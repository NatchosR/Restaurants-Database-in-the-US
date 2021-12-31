SELECT yelp_business.name, yelp_business.review_count, yelp_business.stars,
AVG(yelp_review.stars) AS review_in_2017, yelp_business.city, yelp_business.categories
FROM yelp_business, yelp_review
WHERE yelp_business.business_id=yelp_review.business_id
AND yelp_business.categories LIKE '%Burger%'
AND yelp_business.categories NOT LIKE '%Fast Food%'
AND yelp_business.city = 'Las Vegas'
AND yelp_review.date>='2017-01-01'
AND yelp_business.review_count>=2000
GROUP BY yelp_business.business_id
ORDER BY AVG(yelp_review.stars) DESC