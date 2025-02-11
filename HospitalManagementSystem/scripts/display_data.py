import sys
import os
from tabulate import tabulate

# Ensure we can import from the controller directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def describe_table(table_name):
    """
    Retrieves and displays the structure of a given table using MySQL-style formatting.
    """
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


