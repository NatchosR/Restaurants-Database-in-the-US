use yelp_db;

drop table if exists temperature;

-- create the table for movies_metadata
create table temperature (		
date	date	,
temperature_min		float	,
temperature_max	float,
normal_min	float,
normal_max	float
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/01_temperature-degreeF.csv'
into table temperature
fields terminated by ','
optionally enclosed by """"
ignore 1 lines
;

select * from temperature limit 1000;
