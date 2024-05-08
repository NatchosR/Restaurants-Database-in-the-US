use yelp_db;

drop table if exists weather_data;


create table weather_data (
date	date,
season	varchar(7),
city varchar(15),
diff_precipitation	float,
precipitation	float,
precipitation_normal	float,
temp_min	integer,
temp_max	integer,
temp_normal_min	float,
temp_normal_max	float,
avg_temp	float,
avg_temp_normal	float
)		
;

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

load data local infile 'C:/Users/natr/Hochschule Luzern/DBM - TM - General/data/weather_data.csv'
into table weather_data
fields terminated by ','
optionally enclosed by """"
ignore 1 lines
;

select * from weather_data limit 1000;
