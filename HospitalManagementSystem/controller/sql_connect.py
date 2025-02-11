import pymysql.cursors

# Global connection variable
_connection = None

def create_connection():
    """
    Establishes and returns a single shared connection to the MySQL database.
    """
    global _connection
    if _connection is None:
        try:
            _connection = pymysql.connect(
                host='localhost',
                user='hospital_user',
                password='secure_password',
                database='Hospital',
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Database connection established.")
        except pymysql.MySQLError as e:
            print(f"Database connection error: {e}")
            _connection = None
    return _connection

def get_connection():
    """
    Returns the existing database connection.
    If not connected, attempts to create a new connection.
    """
    return create_connection()

def close_connection():
    """
    Closes the database connection if it exists.
    """
    global _connection
    if _connection:
        _connection.close()
        _connection = None
        print("Database connection closed.")

