use yelp_db;

drop table if exists yelp_review;

-- create the table for yelp_business
create table yelp_review (		
review_id	varchar(30),
user_id		varchar(30),
business_id	varchar(30),
stars	int(1), 
date	date,
useful	int(2),
funny	int(2),
cool	int(2)
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/yelp_review.csv'
into table yelp_review
fields terminated by ','
optionally enclosed by """"
lines terminated by '\r\n'
ignore 1 lines
;

select * from yelp_review limit 1000;
