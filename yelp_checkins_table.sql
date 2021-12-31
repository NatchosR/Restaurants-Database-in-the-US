use yelp_db;

drop table if exists yelp_checkin;

-- create the table for yelp_checkin
create table yelp_checkin (		
business_id	varchar(30)	,
weekday		char(3)	,
hours	time,
checkins	integer(3)
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/yelp_checkin.csv'
into table yelp_checkin
fields terminated by ','
optionally enclosed by """"
ignore 1 lines
;

select * from yelp_checkin limit 1000;
