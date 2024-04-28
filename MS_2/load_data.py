import mysql.connector
import pandas as pd
import numpy as np

cnx = mysql.connector.connect(
    host="******",
    user="******",
    password="******",
    database="******",
    port=****
)

df = pd.read_csv('/Networks.csv')

cursor = cnx.cursor()
query = 'INSERT INTO Network (network_name) VALUES (%s)'
values = [(row[1],) for row in df.itertuples()]  # Ensure each value is a tuple

cursor.executemany(query, values)
cnx.commit()

cursor.close()


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="farida2004",
    database="project_satellite_db",
    port=3306
)

df = pd.read_csv('/users.csv')

cursor = cnx.cursor()

# Adjust the column names in the query to match the CSV file
query = 'INSERT INTO User (Email, Username, Gender, Birthdate, Region, Location) VALUES (%s, %s, %s, %s, %s, %s)'
values = [tuple(row[1:]) for row in df.itertuples()]  # Ensure each value is a tuple

cursor.executemany(query, values)
cnx.commit()

cursor.close()
cnx.close()

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="farida2004",
    database="project_satellite_db",
    port=3306
)

df = pd.read_csv('/Satellite.csv')

cursor = cnx.cursor()

# Adjust the column names in the query to match the CSV file
query = 'INSERT INTO Satellite (Satellite_Position_Longitude, Satellite_Position_Hemisphere, Satellite_Name, Region, Launch_Date, Launching_Rocket) VALUES (%s, %s, %s, %s, %s, %s)'
values = [tuple(row[1:]) for row in df.itertuples()]  # Ensure each value is a tuple

cursor.executemany(query, values)
cnx.commit()

cursor.close()
cnx.close()


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="farida2004",
    database="project_satellite_db",
    port=3306
)

df = pd.read_csv('/Channels_updated.csv')
df.replace(np.nan, None, inplace=True)
df_tst = df[df['Channel_Name'].str.lower().duplicated(keep='first') == False]
df.drop_duplicates(subset=['Channel_Name'])
cursor = cnx.cursor()

# Adjust the column names in the query to match the CSV file
query = 'INSERT INTO Channel (Channel_Name, Network_Name) VALUES (%s, %s)'
values = [tuple(row[1:]) for row in df_tst.itertuples()]  # Ensure each value is a tuple

cursor.executemany(query, values)

cnx.commit()

cursor.close()
cnx.close()

cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="farida2004",
    database="project_satellite_db",
    port=3306
)

df = pd.read_csv('/Channel_Encryptions.csv')

df.drop_duplicates()
cursor = cnx.cursor()

# Adjust the column names in the query to match the CSV file
query = 'INSERT INTO Encryption (Satellite_Name, Channel_Name, Encryption_Type) VALUES (%s, %s, %s)'
values = [tuple(row[1:]) for row in df.itertuples()]  # Ensure each value is a tuple

cursor.executemany(query, values)
cnx.commit()

cursor.close()
cnx.close()


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="farida2004",
    database="project_satellite_db",
    port=3306
)

df = pd.read_csv('/Channel_Languages.csv')


df.drop_duplicates()
cursor = cnx.cursor()

# Adjust the column names in the query to match the CSV file
query = 'INSERT INTO Language (Satellite_Name,Channel_Name,Language) VALUES (%s, %s, %s)'
values = [tuple(row[1:]) for row in df.itertuples()]  # Ensure each value is a tuple

cursor.executemany(query, values)

cnx.commit()

cursor.close()
cnx.close()


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="farida2004",
    database="project_satellite_db",
    port=3306
)

df = pd.read_csv('/Broadcast.csv')
df.replace(np.nan, None, inplace=True)

df.drop_duplicates()
cursor = cnx.cursor()

# Adjust the column names in the query to match the CSV file
# Adjust the column names in the query to match the CSV file
query = 'INSERT INTO Broadcast (Satellite_Name, Channel_Name, Beam, Freq_Num, Freq_Polarisation, SR, FEC, System_Standard, System_Modulation, Video_Compression, Video_Definition) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

values = [tuple(row[1:]) for row in df.itertuples()]  # Ensure each value is a tuple

cursor.executemany(query, values)

cnx.commit()

cursor.close()
cnx.close()
