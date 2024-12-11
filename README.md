# TV-Broadcasting Satellite Database Application

## Introduction
This project is a database application designed to gather and organize information about TV-broadcasting satellites across Asia, Europe, the Atlantic, and the Americas. It provides detailed insights into satellites, their associated TV channels, networks, and the rockets used for their launches. The application offers enhanced filtering, querying, and aggregation functionalities that surpass the capabilities of existing resources such as Lyngsat.com.

The main features include:
- A user-friendly GUI application for satellite and channel exploration.
- Support for user registration and customization of favorite channel lists.
- Advanced queries to identify satellites in range based on user location and available channels.
- Insights on top TV networks, rockets, and satellite growth statistics.

## Features
### Database and Data Management
- Comprehensive storage for satellite details: name, launch date, position, region, launching rocket, etc.
- Detailed information on TV channels: name, beam, frequency, symbol rate, forward error correction (FEC), video encoding, language, encryption, and package affiliation.
- Support for associating channels with TV networks and their packages.
- User registration with information such as username, gender, birthdate, location, and region.
- Favorite channel management for registered users.

### Application Functionalities
- **User Registration**: Register and manage user profiles.
- **Favorite Channel Lists**: Create and maintain custom lists of favorite channels.
- **Satellite Coverage**: Display all channels viewable from a user-provided location (longitude).
- **Favorite Coverage**: Identify which favorite channels are accessible from the user's location and the associated satellite and frequency details.
- **Top Insights**:
  - Top 5 TV Networks/Providers by channel count and average satellite availability.
  - Top 5 rockets by number of satellites launched.
  - Top 5 growing satellites based on channel growth relative to their launch date.
  - Top 5 channels for each language by satellite count.
- **Filtered Channel Search**: Search channels by region, satellite, HD/SD, and language.

## Tools and Technologies
### **Database**
- **MySQL**: A reliable and widely-used relational database system, selected for its support of complex queries, indexing, and scalability.

### **Web Crawling**
- **Python**: The primary programming language for developing scripts and automation tasks.
- **BeautifulSoup**: A Python library for parsing HTML and XML documents, used for extracting structured data from web pages.

### **Application Development**
- **Python**: Used for backend logic and overall application integration.
- **Tkinter**: A Python library for creating the graphical user interface (GUI), offering simplicity and cross-platform compatibility.

### **Database Hosting**
- **Remote MySQL Server**: Services like [db4free.net](https://www.db4free.net) are used to host and manage the MySQL database for seamless remote access and data synchronization.

### **Development Environment**
- **Version Control**: Git and GitHub for version management and collaborative development.
- **IDE**: PyCharm, VS Code, or any Python-supported IDE for efficient coding and debugging.

## Project Deliverables
### Milestone I: Database Design and Implementation
- Entity-Relationship Diagram (ERD)
- Relational Model
- SQL scripts for database and schema creation

### Milestone II: Web Crawling and Data Population
- Web crawling script for extracting data from Lyngsat.com
- Populated MySQL database
- CSV files containing table data

### Milestone III: Application Layer
- GUI-based application
- Latest database dump
- Source code and executable

## Installation and Usage
### Prerequisites
- Python 3.x
- MySQL Server
- Required Python libraries:
  - BeautifulSoup
  - Tkinter
  - MySQL Connector

### Setup
1. Clone the repository.
   ```bash
   git clone https://github.com/FaridaBey/DB_Proj01.git
   cd your-repo-folder
   ```
2. Install required Python libraries.
   ```bash
   pip install -r requirements.txt
   ```
3. Import the database schema and data into your MySQL server.
   ```bash
   mysql -u <username> -p < database_name < database_dump.sql
   ```
4. Run the application.
   ```bash
   python main.py
   ```

## Demo
The application features a user-friendly GUI developed with Tkinter. Users can interact with various functionalities, such as viewing satellites in range, managing favorite channels, and generating insightful reports.

## Future Enhancements
- Support for additional filtering options.
- Real-time updates using live data feeds.
- Improved visualizations and reporting tools.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
Special thanks to [Lyngsat.com](https://www.lyngsat.com) for providing extensive data on TV-broadcasting satellites and channels.

