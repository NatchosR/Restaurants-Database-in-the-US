select avg(yelp_review.stars), yelp_review.date, count(*)
From yelp_review
where date < "2010-01-01"
group by yelp_review.date
order by count(*) DESC;