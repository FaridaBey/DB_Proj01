set global local_infile = 1;
show global variables like 'local_infile';
set sql_safe_updates = 0;
LOAD DATA LOCAL INFILE '/Users/faridabey/Documents/Database/project_satellite_tv/milestone2_scrapping/Satellite.csv'
INTO TABLE Satellite
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;




