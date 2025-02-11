import csv

def check_credentials(username, password, filepath='users/login.csv'):
    """
    Check if the provided username and password match any row in the login CSV file.
    Returns the user role if credentials are valid, otherwise None.
    """
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) < 3:  # Ensure row has enough elements
                continue

            stored_username = row[0].strip()
            stored_password = row[1].strip()
            stored_role = row[2].strip()

            if stored_username == username.strip() and stored_password == password.strip():
                return stored_role
    return None

def authenticate_user():
    """
    Prompts the user to enter login details. User gets 3 attempts before being locked out.
    Returns the user role if login is successful, otherwise None.
    """
    attempts = 0
    while attempts < 3:
        username = input("Enter your username (max 8 characters): ")
        password = input("Enter your password (max 8 characters): ")

        username = username[:8].ljust(8)
        password = password[:8].ljust(8)

        role = check_credentials(username, password)
        if role:
            print(f"Login successful! Your role is: {role}")
            return role
        else:
            attempts += 1
            print(f"Incorrect login. You have {3 - attempts} attempts left.")

    print("Too many failed attempts. You are locked out.")
    return None

def create_user(username: str, password: str, role: str, filepath: str = 'users/login.csv') -> None:
    """
    Appends a new user entry to the login.csv file, ensuring proper row separation.
    """
    try:
        with open(filepath, mode='a', newline='') as file:  # 'newline=' ensures proper formatting
            writer = csv.writer(file)
            writer.writerow([username.strip(), password.strip(), role.strip()])  # No need for "\n"
        print(f"User '{username}' created successfully.")
    except Exception as e:
        print(f"Error creating user: {e}")


def delete_user(username: str, filepath: str = 'users/login.csv') -> None:
    """
    Removes a user from the login CSV file.
    """
    try:
        updated_users = []
        found = False

        with open(filepath, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0].strip() != username.strip():  # Keep all users except the one being deleted
                    updated_users.append(row)
                else:
                    found = True

        if found:
            with open(filepath, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(updated_users)  # Write updated content
            print(f"User '{username}' deleted successfully.")
        else:
            print(f"User '{username}' not found.")

    except Exception as e:
        print(f"Error deleting user: {e}")
