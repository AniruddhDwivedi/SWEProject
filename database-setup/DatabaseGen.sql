    CREATE DATABASE Hospital; --create the hospital database
    USE Hospital;
   
   -- Create the EmployeeRecords table

   CREATE TABLE EmployeeRecords (
    EmployeeNo  INT NOT NULL PRIMARY KEY,
    Name        VARCHAR(100) NULL,
    PhoneNo     BIGINT NULL,
    Gender      CHAR(1) NULL,
    Birthday    DATE NULL,
    Join_date   DATE NULL,
    Designation VARCHAR(25) NULL
);

  -- Create the AdminsitrationInfo table

  CREATE TABLE AdministrationInfo (
    EmployeeId INT NOT NULL,
    Name VARCHAR(255) NOT NULL,
    PhoneNo VARCHAR(20) DEFAULT NULL,
    AuthorizationLevel INT NOT NULL,
    PRIMARY KEY (EmployeeId),
    FOREIGN KEY (EmployeeId) REFERENCES Employee(EmployeeId)
);

 -- Create the patientRecords table

CREATE TABLE patientRecords (
    patientNo      INT NOT NULL PRIMARY KEY,
    Name           VARCHAR(100) NULL,
    PhoneNo        BIGINT NULL,
    Gender         CHAR(1) NULL,
    Birthday       DATE NULL,
    Account_number VARCHAR(15) NULL
);

-- Create the AdmissionEntry table

CREATE TABLE AdmissionEntry (
    LogEntry       INT NOT NULL PRIMARY KEY,
    PatientNo      INT NULL,
    RoomNo         INT NULL,
    DoctorAssigned VARCHAR(100) NULL,
    Booking_date   DATE NULL,
    FOREIGN KEY (PatientNo) REFERENCES patientRecords(patientNo)
);

-- Create the RoomPlan table

CREATE TABLE RoomPlan (
    RoomId        INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    bedCount      INT NOT NULL,
    OccupiedCount INT NOT NULL DEFAULT 0,
    roomType      VARCHAR(50) NOT NULL,
    PatientId     INT NULL,
    FOREIGN KEY (PatientId) REFERENCES patientRecords(patientNo)
);

-- Create the FloorPlan table

CREATE TABLE FloorPlan (
    FloorNumber INT NOT NULL PRIMARY KEY,
    RoomId      INT NULL,
    FloorWarden VARCHAR(255) NULL,
    WardenId    INT NULL,
    FOREIGN KEY (RoomId) REFERENCES RoomPlan(RoomId)
);

--Create the PrescriptionLog table

CREATE TABLE PrescriptionLog (
    TrackingNo             INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ItemNo                 INT NULL,
    PatientNo              INT NULL,
    PatientName            VARCHAR(255) NULL,
    PrescribingDoctorsName VARCHAR(255) NULL,
    PurchaseTime           DATETIME NULL,
    FOREIGN KEY (PatientNo) REFERENCES patientRecords(patientNo)
);

-- Create the Pharmacy table

CREATE TABLE Pharmacy (
    ItemNo             INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ProductName        VARCHAR(255) NOT NULL,
    SellerName         VARCHAR(255) NULL,
    PrescriptionSource INT NULL,
    Price              DECIMAL(10,2) NULL,
    FOREIGN KEY (PrescriptionSource) REFERENCES PrescriptionLog(TrackingNo)
);