import csv

def check_credentials(username, password, filepath='users/login.csv'):
    """
    Check if the provided username and password match any row in the login CSV file.
    Returns the user role if credentials are valid, otherwise None.
    """
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Strip any whitespace from the CSV data to ensure a clean match
            stored_username = row[0].strip()
            stored_password = row[1].strip()
            stored_role = row[2].strip() if len(row) > 2 else None

            # Compare the trimmed/cleaned credentials
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

        # Ensure username and password are not longer than 8 characters
        username = username[:8].ljust(8)  # Pad with spaces if username is less than 8
        password = password[:8].ljust(8)  # Pad with spaces if password is less than 8

        # Check the credentials
        role = check_credentials(username, password)
        if role:
            print(f"Login successful! Your role is: {role}")
            return role
        else:
            attempts += 1
            print(f"Incorrect login. You have {3 - attempts} attempts left.")

    print("Too many failed attempts. You are locked out.")
    return None

