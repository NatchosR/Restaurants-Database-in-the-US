use yelp_db;

drop table if exists yelp_tip;

-- create the table for yelp_business
create table yelp_tip (		
text	text,
date		date,
likes	binary,
business_id	varchar(30),
user_id	varchar(30)
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/yelp_tip.csv'
into table yelp_tip
fields terminated by ','
optionally enclosed by '"'
lines terminated by '\r\n'
ignore 1 lines
;

select * from yelp_tip limit 1000;
load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/yelp_tip.csv' into table yelp_tip fields terminated by ',' optionally enclosed by '"' lines terminated by '\r\n' ignore 1 lines
