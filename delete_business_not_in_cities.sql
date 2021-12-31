SET sql_safe_updates=0;
Delete
FROM yelp_business
WHERE yelp_business.city  not in ('Las Vegas', 'Phoenix', 'Charlotte', 'Cleveland', 'Pittsburgh')
; 