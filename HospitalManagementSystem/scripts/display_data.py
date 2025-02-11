import sys
import os
from tabulate import tabulate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def describe_table(table_name):
    connection = create_connection()
    if not connection:
        print("Failed to connect to the database.")
        return

    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DESC {table_name}")
            results = cursor.fetchall()

            # Format output like MySQL
            table_headers = ["Field", "Type", "Null", "Key", "Default", "Extra"]
            table_rows = [tuple(row.values()) for row in results]

            print(f"Table structure for `{table_name}`:\n")
            print(tabulate(table_rows, headers=table_headers, tablefmt="grid"))

    except pymysql.MySQLError as e:
        print(f"Error retrieving table structure: {e}")
    
    finally:
        close_connection(connection)

def show_menu(role):
    role_menus = {
        "Patient": [
            ("Book Appointment", "APPLY"),
            ("Cancel Appointment", "CANCEL")
        ],
        "Employee": [
            ("Generate Reports", "REPORTS"),
            ("Access Schedules", "TODO")
        ],
        "IT_Officer": [
            ("Debug System", "DEBUG"),
            ("Restart System", "RESTART"),
            ("Manage Authentication", "AUTH")
        ],
        "Contractor": [
            ("Access Schedules", "TODO"),
            ("Register User", "AUTH")
        ],
        "Administrator": [
            ("Register User", "AUTH"),
            ("Access Schedules", "TODO"),
            ("Generate Reports", "REPORTS")
        ]
    }

    if role in role_menus:
        for action, command in role_menus[role]:
            print(f"{action} : {command}")
        print("Exit System : EXIT")
    else:
        print("Invalid role. No menu available.")

def display_table(connection, table_name, custom_query=None):
    try:
        with connection.cursor() as cursor:
            if custom_query:
                cursor.execute(custom_query)  # Use the provided query
            else:
                cursor.execute(f"SELECT * FROM {table_name}")  # Default query

            results = cursor.fetchall()

            if not results:
                print(f"No records found in {table_name}.")
                return

            headers = results[0].keys()  # Get column names
            rows = [list(row.values()) for row in results]

            print(tabulate(rows, headers=headers, tablefmt="psql"))  # Display as a formatted table

    except Exception as e:
        print(f"Error displaying table '{table_name}': {e}")
