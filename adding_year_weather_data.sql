
Select * from weather_data

ALTER table yelp_db.weather_data
ADD year int AS (CASE
		when date <= "2008-12-31" then '2008'
		when date <= "2009-12-31" then '2009'
		when date <= "2010-12-31" then '2010'
		when date <= "2011-12-31" then '2011'
		when date <= "2012-12-31" then '2012'
		when date <= "2013-12-31" then '2013'
		when date <= "2014-12-31" then '2014'
		when date <= "2015-12-31" then '2015'
		when date <= "2016-12-31" then '2016'
		when date <= "2017-12-31" then '2017'
		END)