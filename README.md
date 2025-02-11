# SWEProject
Hospital Management System SWE Project Implementation

## Steps to set up the project locally

1. Confirm your local MySQL instance is updated to latest available instances offered on your software manager application
   
2. Configure new Database in MySQL as described in DatabaseGen.sql (use notepad for reading)
 
3. Set Up the python project with necessary external modules:
   
  - ``python3 -m pip install tabulate``
  - ``python3 -m pip install pymysql``
 
4. Create a database user to interact with the database as defined in ConfigureUser.sql, this user only needs access to this database

5. Run main.py from terminal with ``python3 main.py`` or equivalent

The Project is in its earliest development stage, most functionalities are absent, to be added later.
