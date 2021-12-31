USE yelp_db;
select yelp_business.city, year, avg(yelp_review.stars), avg(diff_precipitation), avg(avg_temp), CASE
	when weather_data.date <= "2008-03-20" then 'Winter 2008'
    when weather_data.date <= "2008-06-20" then 'Spring 2008'
    when weather_data.date <= "2008-09-20" then 'Summer 2008'
    when weather_data.date <= "2008-12-20" then 'Autumn 2008'
    when weather_data.date <= "2009-03-20" then 'Winter 2009'
    when weather_data.date <= "2009-06-20" then 'Spring 2009'
    when weather_data.date <= "2009-09-20" then 'Summer 2009'
    when weather_data.date <= "2009-12-20" then 'Autumn 2009'
    when weather_data.date <= "2010-03-20" then 'Winter 2010'
    when weather_data.date <= "2010-06-20" then 'Spring 2010'
    when weather_data.date <= "2010-09-20" then 'Summer 2010'
    when weather_data.date <= "2010-12-20" then 'Autumn 2010'
    when weather_data.date <= "2011-03-20" then 'Winter 2011'
    when weather_data.date <= "2011-06-20" then 'Spring 2011'
    when weather_data.date <= "2011-09-20" then 'Summer 2011'
    when weather_data.date <= "2011-12-20" then 'Autumn 2011'
    when weather_data.date <= "2012-03-20" then 'Winter 2012'
    when weather_data.date <= "2012-06-20" then 'Spring 2012'
    when weather_data.date <= "2012-09-20" then 'Summer 2012'
    when weather_data.date <= "2012-12-20" then 'Autumn 2012'
    when weather_data.date <= "2013-03-20" then 'Winter 2013'
    when weather_data.date <= "2013-06-20" then 'Spring 2013'
    when weather_data.date <= "2013-09-20" then 'Summer 2013'
    when weather_data.date <= "2013-12-20" then 'Autumn 2013'
    when weather_data.date <= "2014-03-20" then 'Winter 2014'
    when weather_data.date <= "2014-06-20" then 'Spring 2014'
    when weather_data.date <= "2014-09-20" then 'Summer 2014'
    when weather_data.date <= "2014-12-20" then 'Autumn 2014'
    when weather_data.date <= "2015-03-20" then 'Winter 2015'
    when weather_data.date <= "2015-06-20" then 'Spring 2015'
    when weather_data.date <= "2015-09-20" then 'Summer 2015'
    when weather_data.date <= "2015-12-20" then 'Autumn 2015'
    when weather_data.date <= "2016-03-20" then 'Winter 2016'
    when weather_data.date <= "2016-06-20" then 'Spring 2016'
    when weather_data.date <= "2016-09-20" then 'Summer 2016'
    when weather_data.date <= "2016-12-20" then 'Autumn 2016'
    when weather_data.date <= "2017-03-20" then 'Winter 2017'
    when weather_data.date <= "2017-06-20" then 'Spring 2017'
    when weather_data.date <= "2017-09-20" then 'Summer 2017'
    when weather_data.date <= "2017-12-20" then 'Autumn 2017'
    END AS season_year
from yelp_business, yelp_review, weather_data
where yelp_review.business_id = yelp_business.business_id
And yelp_review.date = weather_data.date
AND yelp_business.city = weather_data.city
Group by city, season_year
Order by city, year