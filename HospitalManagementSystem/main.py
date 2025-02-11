from users import auth
from scripts.util import execute_command
from controller import sql_connect
from scripts import display_data

def main():
    print("Running System Now...")
    
    # Authenticate user and retrieve their role
    user_role = auth.authenticate_user()
    
    if user_role:
        print("Welcome to the system.")

        # Establish database connection
        connection = sql_connect.create_connection()
        
        if connection:
            display_data.show_menu(user_role);

            while True:
                command = input("\nEnter a command: ").strip()
                if command.lower() == "exit":
                    print("Exiting system...")
                    break
                execute_command(command, connection)

            sql_connect.close_connection()
        else:
            print("Database connection failed. Some features may not be available.")

    else:
        print("Access denied.")

if __name__ == "__main__":
    main()
