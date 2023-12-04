Welcome to my high school Python project, created as a part of the CBSE syllabus.

Project Overview
This project is coded in Python and utilizes Tkinter for the graphical user interface and mysql.connector for database interactions.

Setup Instructions
To run this project on your computer, follow these steps:

Ensure that the Python file is in the same folder as the 'media' folder.
Make sure you have MySQL-essential 5.5 installed on your system.
Set the MySQL password to '1234'.
Create a database named 'adis'.
Paste the following SQL command to create the necessary table:

CREATE TABLE AMAS (
    Sno INT AUTO_INCREMENT PRIMARY KEY,
    Passengers INT,
    Distance FLOAT,
    Cargo CHAR(1),
    Aircraft VARCHAR(255)
);
Ensure that the required Python packages are installed.
Running the Project
This project allows you to insert values into a MySQL table. The details represent available aircraft at an airport, including the number of passengers, the flying range in kilometers, and the model of the plane.

By providing on-demand details, the program can determine which plane to allot to a particular flight.

Feel free to explore the functionalities and modify the code as needed for your use case.

Happy coding!
