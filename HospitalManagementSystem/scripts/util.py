from scripts.commands import Commands
from scripts.display_data import display_table
from users.auth import create_user, delete_user
import os
import json

def apply_appointment(connection):
    cursor = connection.cursor()
    
    patient_name = input("Enter your name: ")
    
    cursor.execute("SELECT patientNo FROM patientRecords WHERE Name = %s", (patient_name,))
    patient = cursor.fetchone()
    
    if not patient:
        print("Patient not found. Registering new patient.")
        phone_no = input("Enter your phone number: ")
        gender = input("Enter your gender (M/F): ")
        birthday = input("Enter your birth date (YYYY-MM-DD): ")
        account_number = input("Enter your account number: ")
        
        cursor.execute(
            "INSERT INTO patientRecords (Name, PhoneNo, Gender, Birthday, Account_number) VALUES (%s, %s, %s, %s, %s)",
            (patient_name, phone_no, gender, birthday, account_number)
        )
        connection.commit()
        
        cursor.execute("SELECT patientNo FROM patientRecords WHERE Name = %s", (patient_name,))
        patient = cursor.fetchone()
    
    patient_no = patient["patientNo"]
    
    print("Available doctors:")
    display_table(connection, "EmployeeRecords", "SELECT Name FROM EmployeeRecords WHERE Designation = 'Doctor'")
    
    doctor_name = input("Enter the name of the doctor you want to book: ")
    room_no = input("Enter preferred room number: ")
    booking_date = input("Enter booking date (YYYY-MM-DD): ")
    
    cursor.execute(
        "INSERT INTO AdmissionEntry (PatientNo, RoomNo, DoctorAssigned, Booking_date) VALUES (%s, %s, %s, %s)",
        (patient_no, room_no, doctor_name, booking_date)
    )
    connection.commit()
    
    print("Appointment successfully booked!")
    cursor.close()


def cancel_appointment(connection):
    cursor = connection.cursor()
    
    patient_name = input("Enter your name: ")
    
    cursor.execute("SELECT patientNo FROM patientRecords WHERE Name = %s", (patient_name,))
    patient = cursor.fetchone()

    if not patient:
        print("Patient not found. Invalid command.")
        return

    display_table(connection, "AdmissionEntry", str("SELECT * FROM AdmissionEntry WHERE patientNo = %s", (patient)))
    ch = input("Are you sure you wish to cancel this appointment? (YES | NO) : ")
    print("Cancelling Patient Appointment")

    cursor.execute(
        "DROP FROM AdmissionEntry WHERE patientNo = %s",
        (patient_no)
    )
    connection.commit()
    

def generate_reports(connection):
    """
    Generates a report based on user input using an optimized lookup (dictionary).
    
    Parameters:
        connection (object): An active database connection.
    """
    # Dictionary mapping of user command (lowercase) to (table_name, SQL query)
    report_options = {
        "admission": ("AdmissionEntry", "SELECT * FROM AdmissionEntry;"),
        "patient": ("patientRecords", "SELECT * FROM patientRecords;"),
        "employees": ("EmployeeRecords", "SELECT * FROM EmployeeRecords;"),
        "drugs": ("Pharmacy", "SELECT * FROM Pharmacy;")
    }

    ch = input(
        "Which datastore would you like to see?\n"
        "AdmissionEntry - ADMISSION\n"
        "PatientRecords - PATIENT\n"
        "EmployeeRecords - EMPLOYEES\n"
        "Pharmacy - DRUGS\n"
        "Enter Command: "
    ).strip().lower()

    if ch in report_options:
        table_name, query = report_options[ch]
        display_table(connection, table_name, query)
    else:
        print("Invalid command.")

    exit()


def access_schedules(connection):
    """
    Displays the schedules of all doctors in a human-readable tabular format.
    """
    try:
        cursor = connection.cursor()
        query = """
        SELECT ER.Name, ER.Designation, ES.DailySchedules 
        FROM EmployeeRecords ER
        JOIN EmployeeSchedules ES ON ER.EmployeeNo = ES.EmployeeNo
        WHERE ER.Designation = 'Doctor';
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        if not rows:
            print("No schedules available for doctors.")
            return

        # Prepare data for display
        schedule_data = []
        for name, designation, schedules_json in rows:
            schedules = json.loads(schedules_json)  # Parse the JSON to extract schedules
            for schedule in schedules:
                schedule_data.append([name, designation, schedule['time'], schedule['detail']])

        # Display in a readable table format
        print(tabulate(schedule_data, headers=["Name", "Designation", "Time", "Activity"], tablefmt="pretty"))

    except Exception as e:
        print(f"Error accessing schedules: {e}")

def debug_system(connection):
    print("Debugging system...")
    exit();

def restart_system(connection):
    print("Restarting system...")
    return;


def manage_auth(connection):
    """
    Manages user authentication: registering new users, deleting existing ones, or exiting the system.
    """
    while True:
        command = input("\nRegister New User : NEW\nDelete Existing User : DEL\nExit system : EXIT\nEnter Command: ").strip().upper()

        if command == "NEW":
            username = input("Enter Username: ").strip()
            password = input("Enter Password: ").strip()
            role = input("Enter Role: ").strip()
            create_user(username, password, role)

        elif command == "DEL":
            username = input("Enter Username to Delete: ").strip()
            delete_user(username)

        elif command == "EXIT":
            print("Exiting authentication management.")
            break

        else:
            print("Invalid command. Please enter NEW, DEL, or EXIT.")



# Map commands to functions
COMMAND_MAP = {
    Commands.APPLY.value: apply_appointment,
    Commands.CANCEL.value: cancel_appointment,
    Commands.REPORTS.value: generate_reports,
    Commands.TODO.value: access_schedules,
    Commands.DEBUG.value: debug_system,
    Commands.RESTART.value: restart_system,
    Commands.AUTH.value: manage_auth
}

def execute_command(command, connection):
    command = command.upper()
    if command in COMMAND_MAP:
        COMMAND_MAP[command](connection) 
    else:
        print("Invalid command. Please try again.")

