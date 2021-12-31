SELECT 
TABLE_CATALOG,
TABLE_SCHEMA,
TABLE_NAME, 
COLUMN_NAME, 
DATA_TYPE 
FROM INFORMATION_SCHEMA.COLUMNS
where TABLE_NAME = 'weather_data';

ALTER TABLE weather_data CHANGE COLUMN season season varchar(7) AFTER year;
ALTER TABLE weather_data CHANGE COLUMN city city varchar (10) AFTER season;
ALTER TABLE weather_data CHANGE COLUMN diff_precipitation diff_precipitation float AFTER city;
ALTER TABLE weather_data CHANGE COLUMN precipitation precipitation float AFTER diff_precipitation;
ALTER TABLE weather_data CHANGE COLUMN precipitation_normal precipitation_normal float AFTER precipitation;
ALTER TABLE weather_data CHANGE COLUMN temp_min temp_min int AFTER precipitation_normal;
ALTER TABLE weather_data CHANGE COLUMN temp_max temp_max int AFTER temp_min;
ALTER TABLE weather_data CHANGE COLUMN temp_normal_min temp_normal_min float AFTER temp_max;
ALTER TABLE weather_data CHANGE COLUMN temp_normal_max temp_normal_max float AFTER temp_normal_min;
ALTER TABLE weather_data CHANGE COLUMN avg_temp avg_temp float AFTER temp_normal_max;
ALTER TABLE weather_data CHANGE COLUMN avg_temp_normal avg_temp_normal float AFTER avg_temp;