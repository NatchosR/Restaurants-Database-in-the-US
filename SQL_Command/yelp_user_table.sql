use yelp_db;

drop table if exists yelp_user;

-- create the table for yelp_business
create table yelp_user (		
user_id	varchar(30)	primary key,
name	varchar(15),
review_count	integer(4),
yelping_since	date,
average_stars	float
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/yelp_user.csv'
into table yelp_user
fields terminated by ','
optionally enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
(user_id, name, review_count, yelping_since, @ignore, @ignore, @ignore, @ignore, @ignore, @ignore, average_stars)
;

select * from yelp_user limit 1000;
