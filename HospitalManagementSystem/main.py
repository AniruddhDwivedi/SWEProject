from users import auth
from controller import sql_connect
from scripts import display_data

def main():
    # Begin system
    print("Running System Now...")
    
    # Authenticate user and retrieve their role
    user_role = auth.authenticate_user()
    
    if user_role:
        print("Welcome to the system.")

        # Establish database connection
        connection = sql_connect.create_connection()
        
        if connection:
            sql_connect.close_connection(connection)
        else:
            print("Database connection failed. Some features may not be available.")

    else:
        print("Access denied.")

if __name__ == "__main__":
    main()

