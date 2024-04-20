/*
	Project - Satellite TV 									Milestone 1
*/
/*
create db: 
*/
CREATE DATABASE IF NOT EXISTS project_satellite_db;
USE project_satellite_db;
/* 
create tables:
*/

Create Table Satellite (
sat_name varchar (100) primary key,
lauch_date date,
launching_rocket varchar (100), 
longitude_position float,
hemisphere_position char,
region varchar(100),
site varchar (100)
);

create table Network(
network_name varchar (100) primary key
);

create table Channel(
channel_name varchar (100) primary key,
website varchar (100)
);

create table language (
channel_name varchar (100),
language varchar (100),
primary key (channel_name),
foreign key (channel_name) references Channel(channel_name)
);

create table Country (
channel_name varchar (100),
country varchar (100),
primary key (channel_name),
foreign key (channel_name) references Channel(channel_name)
);

create table User (
email varchar(100) primary key, 
username varchar (100), 
gender char, 
birthdate date, 
region varchar (100), 
location varchar (100)
);

create table hosts (
sat_name varchar(100), 
network_name varchar (100),
primary key (sat_name,network_name),
foreign key (sat_name) references Satellite(sat_name),
foreign key (network_name) references Network(network_name)
);

create table broadcast (
Sat_name varchar (100), 
channel_name varchar (100),
beam varchar (100),
frequency_num int, 
frequency_polarisation char,
SR int,
FEC float,
video_encoding varchar (100),
encryption varchar (100),
primary key (sat_name,channel_name),
foreign key (sat_name) references Satellite(sat_name),
foreign key (channel_name) references Channel(channel_name)
);

create table Favourite (
user_email varchar (100), 
channel_name varchar (100),
primary key (user_email,channel_name),
foreign key (user_email) references User(email),
foreign key (channel_name) references Channel(channel_name)
);
/*
add foreign key to cahnnel, 
it doesnt like it when i put 
it while creating the tabel
*/
ALTER TABLE Channel
ADD COLUMN network_name VARCHAR(100),
ADD FOREIGN KEY (network_name) REFERENCES Network(network_name);

