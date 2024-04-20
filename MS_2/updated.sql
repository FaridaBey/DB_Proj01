drop DATABASE IF EXISTS project_satellite_db;


CREATE DATABASE IF NOT EXISTS project_satellite_db 
  CHARACTER SET utf32 
  COLLATE utf32_bin;

USE project_satellite_db;

CREATE TABLE Satellite (
    Satellite_Position_Longitude VARCHAR(100),
    Satellite_Position_Hemisphere CHAR(1),
    Satellite_Name VARCHAR(100) PRIMARY KEY,
    Region VARCHAR(100),
    Launch_Date DATE,
    Launching_Rocket VARCHAR(100)
);

CREATE TABLE Network (
    network_name VARCHAR(100) PRIMARY KEY
);

CREATE TABLE Channel (
    Channel_Name VARCHAR(100) PRIMARY KEY,
    Network_Name VARCHAR(100),
    FOREIGN KEY (Network_Name) REFERENCES Network(Network_Name)
);

CREATE TABLE Language (
    Satellite_Name VARCHAR(100),
    Channel_Name VARCHAR(100),
    Language VARCHAR(100),
    PRIMARY KEY (Satellite_Name, Channel_Name, Language),
    FOREIGN KEY (Satellite_Name) REFERENCES Satellite(Satellite_Name),
    FOREIGN KEY (Channel_Name) REFERENCES Channel(Channel_Name)
);

CREATE TABLE User (
    Email VARCHAR(100) PRIMARY KEY,
    Username VARCHAR(100),
    Gender CHAR(1),
    Birthdate DATE,
    Region VARCHAR(100),
    Location VARCHAR(100)
);

CREATE TABLE Encryption (
    Satellite_Name VARCHAR(100),
    Channel_Name VARCHAR(100),
    Encryption_Type VARCHAR(100),
    PRIMARY KEY (Satellite_Name, Channel_Name, Encryption_Type),
    FOREIGN KEY (Satellite_Name) REFERENCES Satellite(Satellite_Name),
    FOREIGN KEY (Channel_Name) REFERENCES Channel(Channel_Name)
);

CREATE TABLE Favourite (
    User_Email VARCHAR(100),
    Channel_Name VARCHAR(100),
    PRIMARY KEY (User_Email, Channel_Name),
    FOREIGN KEY (User_Email) REFERENCES User(Email),
    FOREIGN KEY (Channel_Name) REFERENCES Channel(Channel_Name)
);

CREATE TABLE Broadcast (
    Satellite_Name VARCHAR(100),
    Channel_Name VARCHAR(100),
    Beam VARCHAR(100),
    Freq_Num INT,
    Freq_Polarisation VARCHAR(100),
    SR VARCHAR(100),
    FEC VARCHAR(100),
    System_Standard VARCHAR(100),
    System_Modulation VARCHAR(100),
    Video_Compression VARCHAR(100),
    Video_Definition VARCHAR(100),
    PRIMARY KEY (Satellite_Name, Channel_Name),
    FOREIGN KEY (Satellite_Name) REFERENCES Satellite(Satellite_Name),
    FOREIGN KEY (Channel_Name) REFERENCES Channel(Channel_Name)
);
