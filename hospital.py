class Patient:
    def __init__(self,patient_id , name,age,disease):
        self.patient_id  =patient_id
        self.name = name
        self.age = age
        self.disease = disease

    def display(self):
        print("============= Patient Ditails===================")
        print(f"Patient ID :{self.patient_id}")
        print(f"Name :{self.name}")
        print(f"Age : {self.age}")
        print(f"Disease: {self.disease}")

class Doctor:
    def __init__(self,doctor_id,name, specialization, available):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.available = available

    def display(self):
        print("========================== Doctor Detials ==============================")
        print(f"Docter ID: {self.doctor_id}")
        print(f"Name : {self.name}")
        print(f"Department : {self.specialization}")
        print(f"Available: {self.available}")

class Appointment:
    def __init__(self,patient ,doctor):
        self.patient = patient
        self.doctor = doctor

    def book_appointment(self):
        if self.doctor.available.lower() == "yes":
            print("Appointment Booked Successfully")
            print(f"Patient :{self.patient.name}")
            print(f"Doctor: {self.doctor.name}")
            print(f"Department: {self.doctor.specialization}")

        else:
            print(f"Sorry! , Dr {self.doctor.name}is not availble")

class Hospital:
    def __init__(self,hospital_name):
        self.hopital_name = hospital_name
        self.patients = []
        self.doctors = []
    
    def add_patients(self,patient):
        self.patients.append(patient)

    def add_doctors(self, doctor):
        self.doctors.append(doctor)

    def display_patient(self):
        for patient in self.patients:
            patient.display()
        
    def display_doctor(self):
        for doctor in self.doctors:
            doctor.display()

hospital = Hospital("City Health care")


doctor1 = Doctor(1 ,"Dr Ganapathi Powde","Cardiologist","yes")
doctor2 = Doctor(2,"DR jayashankar","Gynacologist", "no")
doctor3 = Doctor(3,"Dr Asha ani","rheumatologist", "yes")

hospital.add_doctors(doctor1)
hospital.add_doctors(doctor2)
hospital.add_doctors(doctor3)

patient1 = Patient(101, "Gagan Gowda KU",19, "RA")
patient2 = Patient(102 , "Karthik Gowda Mk",40, "cancer")
patient3 = Patient(103 , "Avinash", 36,"HIV")

hospital.add_patients(patient1)
hospital.add_patients(patient2)
hospital.add_patients(patient3)

hospital.display_patient()
hospital.display_doctor()

appoint = Appointment(patient1, doctor3)
appoint.book_appointment()