from scripts.commands import Commands
from scripts.display_data import display_table
from users.auth import create_user, delete_user

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


def cancel_appointment():
    print("Cancelling an appointment...")

def generate_reports():
    print("Generating reports...")

def access_schedules():
    print("Accessing schedules...")

def debug_system():
    print("Debugging system...")

def restart_system():
    print("Restarting system...")


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

