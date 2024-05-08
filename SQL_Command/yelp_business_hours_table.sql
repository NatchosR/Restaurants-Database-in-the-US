use yelp_db;

drop table if exists yelp_business_hours;

-- create the table for yelp_business_hours
create table yelp_business_hours (		
business_id	varchar(30)	,
monday		varchar(15)	,
tuesday	varchar(15),
wednesday	varchar(15),
thursday	varchar(15),
friday	varchar(15),
saturday	varchar(15),
sunday	varchar(15)
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/yelp_business_hours.csv'
into table yelp_business_hours
fields terminated by ','
optionally enclosed by """"
ignore 1 lines
;

select * from yelp_business_hours limit 1000;
