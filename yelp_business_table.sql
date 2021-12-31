use yelp_db;

drop table if exists yelp_business;

-- create the table for yelp_business
create table yelp_business (		
business_id	varchar(30)	primary key,
name		varchar(50)	,
city	varchar(20),
state	char(2),
postal_code	varchar(10),
latitude	float,
longitude	float,
stars	float,
review_count integer(4),
is_open	integer(1),
categories	varchar(100),
address	varchar(50)
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/yelp_business.csv'
into table yelp_business
fields terminated by ','
lines terminated by '\r\n'
ignore 1 lines
;

select * from yelp_business limit 1000;
