USE yelp_db;

DROP TABLE IF EXISTS yelp_review_text;

CREATE TABLE yelp_review_text (
review_id	varchar(30),
text	text
);

-- Allow loading files from the client ("local infiles") on both server and client
SET GLOBAL local_infile = true;
SET @@GLOBAL.local_infile = 1;
-- OPT_LOCAL_INFILE=1 <= set as connection parameter in advanced tab of the connection editor in MySQL Workbench 

LOAD DATA LOCAL INFILE 'C:/Users/natr/switchdrive/SyncVM (S2)/yelp_review_text.csv'
INTO TABLE yelp_review_text
FIELDS TERMINATED BY ','
optionally enclosed by '"'
ignore 1 lines
 
