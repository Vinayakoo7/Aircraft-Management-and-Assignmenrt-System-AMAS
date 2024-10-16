
Aircraft Management System 
(High School Python Project)

Welcome to the Aircraft Management System, a Python project developed as part of the CBSE syllabus during high school. This project demonstrates how Python can be used to manage aircraft details at an airport, including handling passengers, cargo, and flight distances. The project employs Tkinter for the graphical user interface and MySQL for database operations.

Project Overview

The application allows users to input and manage data on available aircraft at an airport. Users can specify:
- The number of passengers the aircraft can carry
- The flight range (distance in kilometers)
- Cargo capacity
- Aircraft model

The system then assists in determining the best aircraft to assign to a particular flight based on the input criteria.

Technologies Used
- Python: Core programming language.
- Tkinter: For creating the graphical user interface (GUI).
- MySQL: Used for database management to store and retrieve aircraft data.
- mysql.connector: Python module to interact with the MySQL database.

Setup Instructions

To set up and run this project on your local machine, follow the steps below:

1. Prerequisites

- Install Python 3.x from python.org.
- Install MySQL 5.5 or higher. You can download MySQL from mysql.com.
- Make sure you have mysql.connector installed. To install the package, run:
  pip install mysql-connector-python

2. Project Setup

1. Clone this repository or download the project files.
2. Ensure the Python script is located in the same directory as the media folder.
3. MySQL Setup:
   - Install MySQL Essential 5.5 or higher on your system.
   - Set the MySQL root password to 1234 (you can modify the script to use a different password if required).
   - Open MySQL and create a new database named adis:
     CREATE DATABASE adis;
   - Use the following SQL command to create the required table:
     CREATE TABLE AMAS (
       Sno INT AUTO_INCREMENT PRIMARY KEY,
       Passengers INT,
       Distance FLOAT,
       Cargo CHAR(1),
       Aircraft VARCHAR(255)
     );

3. Running the Project

1. Open a terminal/command prompt and navigate to the project directory.
2. Run the Python script:
   python Project.py
3. The application window will launch. From there, you can input aircraft details and manage the database.

Features

- Add Aircraft Information: Insert new records into the MySQL database, including the number of passengers, flight range, cargo capacity, and aircraft model.
- Determine Best Aircraft: Based on input requirements, the program can suggest the best aircraft for a flight.
- Graphical User Interface (GUI): Interact with the application through a user-friendly interface designed using Tkinter.

Customization

You can modify the Python code to suit your specific needs. For instance, you can adjust the database schema, add new functionalities, or improve the GUI. 

Troubleshooting

- Ensure that your MySQL service is running.
- If you're using a different MySQL password, update the connection settings in the Python script accordingly.

Future Improvements

- Add additional fields for aircraft information, such as fuel capacity and maintenance schedules.
- Implement validation for user inputs in the GUI.
- Add support for more complex queries and reports on aircraft usage and availability.

License

This project is licensed under the MIT License. Feel free to explore, modify, and distribute the code.

Contact

For any questions or feedback, feel free to reach out to me through GitHub.

Happy coding!
