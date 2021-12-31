SET sql_safe_updates=0;
DELETE FROM yelp_db.yelp_business
WHERE yelp_business.categories not like '%Restaurants%'
and yelp_business.categories not like '%Bars%'
and yelp_business.categories not like '%Food%'
and yelp_business.categories not like '%Cafes%'
;