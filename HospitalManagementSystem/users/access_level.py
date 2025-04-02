class TemplateF:
    def __init__(self):

class Employee:
    def __init__(self, emp_id, dob, gender):
        self.emp_id = emp_id
        self.dob = dob
        self.gender = gender

    def login(self):
        print(f"Employee {self.emp_id} logged in.")

    def view_session_history(self):
        print("Viewing session history...")

    def change_authentication(self):
        print("Changing authentication details...")


class Administrator(Employee):
    def __init__(self, emp_id, dob, gender, admin_id, auth_level):
        super().__init__(emp_id, dob, gender)
        self.admin_id = admin_id
        self.auth_level = auth_level

    def start_server(self):
        print("Starting server...")

    def update_system(self):
        print("Updating system...")


class Doctor(Employee):
    def __init__(self, emp_id, dob, gender, doctor_id, hours):
        super().__init__(emp_id, dob, gender)
        self.doctor_id = doctor_id
        self.hours = hours

    def view_appointments(self):
        print("Viewing appointments...")

    def update_record(self):
        print("Updating patient record...")

    def discharge_patient(self):
        print("Discharging patient...")


class Nurse(Employee):
    def __init__(self, emp_id, dob, gender, nurse_id, hours):
        super().__init__(emp_id, dob, gender)
        self.nurse_id = nurse_id
        self.hours = hours

    def view_appointments(self):
        print("Viewing appointments...")

    def update_record(self):
        print("Updating record...")


class ITOfficer(Employee):
    def __init__(self, emp_id, dob, gender, auth_active):
        super().__init__(emp_id, dob, gender)
        self.auth_active = auth_active

    def debug_system(self):
        print("Debugging system...")

    def run_template(self):
        print("Running template...")

    def restart_system(self):
        print("Restarting system...")


class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def book_appointment(self):
        print("Booking appointment...")

    def cancel_appointment(self):
        print("Canceling appointment...")


def load_user_context():
    user_details = authenticate_user()
    if not user_details:
        print("Authentication failed.")
        return None

    user_type = user_details.get("role")
    if user_type == "Administrator":
        return Administrator(
            emp_id=user_details["id"],
            dob=user_details["dob"],
            gender=user_details["gender"],
            admin_id=user_details["admin_id"],
            auth_level=user_details["auth_level"],
        )
    elif user_type == "Doctor":
        return Doctor(
            emp_id=user_details["id"],
            dob=user_details["dob"],
            gender=user_details["gender"],
            doctor_id=user_details["doctor_id"],
            hours=user_details["hours"],
        )
    elif user_type == "Nurse":
        return Nurse(
            emp_id=user_details["id"],
            dob=user_details["dob"],
            gender=user_details["gender"],
            nurse_id=user_details["nurse_id"],
            hours=user_details["hours"],
        )
    elif user_type == "ITOfficer":
        return ITOfficer(
            emp_id=user_details["id"],
            dob=user_details["dob"],
            gender=user_details["gender"],
            auth_active=user_details["auth_active"],
        )
    elif user_type == "Patient":
        return Patient(
            patient_id=user_details["id"],
            name=user_details["name"],
        )
    else:
        print("Unknown role.")
        return None

