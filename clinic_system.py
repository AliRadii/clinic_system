from datetime import datetime, timedelta
class Doctor:
    def __init__(self, doctor_id, name, specialty, available_slots):
        self.__doctor_id=doctor_id
        self.__name=name
        self.__specialty=specialty
        self.__available_slots=available_slots


    @property
    def doctor_id(self):
        return self.__doctor_id
    
    @doctor_id.setter
    def doctor_id(self,id):
        
        self.__doctor_id = id

    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,n):
        self.__name=n

    
    @property
    def specialty(self):
        return self.__specialty
    
    @specialty.setter
    def specialty(self,n):
        self.__specialty=n

    
    @property
    def available_slots(self):
        return self.__available_slots
    
    @available_slots.setter
    def available_slots(self,slots):
        self.__available_slots = slots


    def display_info(self):
        print(f"Doctor name is {self.__name}") 
        print(f"Doctor ID is {self.__doctor_id}") 
        print(f"Doctor specialty is {self.__specialty}") 
        print("Available Slots:")
        for slot in self.__available_slots:
            print(f" - {slot}")

    
    def book_slot(self, slot_time):
        if slot_time not in self.__available_slots:
            print("❌ The selected time slot is not available.")
            return False
        else:
            self.__available_slots.remove(slot_time)
            print(f"✅ Appointment successfully booked at {slot_time}.")
            return True

    def cancle_slot(self,slot_time):
        if slot_time in self.__available_slots:
            print("❌ Slot is already available ")
        else:
            self.__available_slots.append(slot_time)
            self.__available_slots.sort()
            print(f"✅ Slot is cancled  successfully ")

    def is_available(self,slot_time):
        if slot_time in self.__available_slots:
            print(f'✅ {slot_time} is available')
        
        else:
            print(f"❌ {slot_time} is not available")

    def add_slot(self, slot_time):
        if slot_time in self.__available_slots:
            print(f"⚠️ {slot_time} already exists in the available slots.")
        else:
            self.__available_slots.append(slot_time)
            self.__available_slots.sort()
            print(f"✅ {slot_time} was successfully added to available slots.")

    def __str__(self):
        info = f"👨‍⚕️ Doctor ID: {self.__doctor_id}\n"
        info += f"🧑‍⚕️ Name: {self.__name}\n"
        info += f"🔬 Specialty: {self.__specialty}\n"
        info += "🕑 Available Slots:\n"
        for slot in self.__available_slots:
            info += f"   - {slot}\n"
        return info




# patient.py


class Patient:
    def __init__(self, patient_id, name, age, phone,gender):
        self.__patient_id=patient_id
        self.__name=name
        self.__age=age
        self.__gender=gender
        self.__phone=phone
        self.__appointments=[]



    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,n):
        self.__name=n
    
    @property
    def patient_id(self):
        return self.__patient_id
    @patient_id.setter
    def patient_id(self,n):
        self.__patient_id=n
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,n):
        self.__age=n
    
    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self,n):
        self.__gender=n
   
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self,n):
        self.__phone=n

    
    def display(self):
        print(f"Patient Name is {self.__name}")
        print(f"Patient Age is {self.__age}")
        print(f"Patient ID is {self.__patient_id}")
        print(f"Patient Gender is {self.__gender}")
        print(f"Patient Phone is {self.__phone}")


    def book_appointment(self,d1,time_slot):
        if  time_slot in d1.available_slots:
            print(f"✅appointment {time_slot} is booked successfully with doctor {d1.name}")
            d1.book_slot(time_slot)
            self.__appointments.append((d1.name, time_slot))

        else:
            print(f"❌appointment {time_slot} is not available")

            
    
    def view_appointments(self):
        if not self.__appointments:
            print("No appointments booked.")
        else:
            for doc_name, slot in self.__appointments:
                print(f"📅 Appointment with Doctor {doc_name} at {slot}")


    def cancel_appointment(self, d1, time_slot):
        appointment = (d1.name, time_slot)

        if appointment in self.__appointments:
            if time_slot not in d1.available_slots:  # means it was booked
                self.__appointments.remove(appointment)
                d1.cancle_slot(time_slot)
                print(f"❌ Appointment at {time_slot} with Dr. {d1.name} has been cancelled.")
            else:
                print("⚠️ This slot is already available in doctor's schedule.")
        else:
            print("🚫 You have no such appointment to cancel.")

    def __str__(self):
        appointment_details = ""
        if self.__appointments:
            for idx, (doctor_name, time_slot) in enumerate(self.__appointments, 1):
                appointment_details += f"\n  {idx}. Dr. {doctor_name} at {time_slot}"
        else:
            appointment_details = "\n  No appointments booked."

        return (
            f"🧑‍⚕️ Patient ID: {self.__patient_id}\n"
            f"👤 Name: {self.__name}\n"
            f"📞 Phone: {self.__phone}\n"
            f"🔢 Age: {self.__age}\n"
            f"⚧️ Gender: {self.__gender}\n"
            f"📅 Appointments:{appointment_details}"
        )
    
    






class Functions:
    @staticmethod
    def set_id():
        count = 0
        while count < 3:
            try:
                id = int(input("Enter The ID: ").strip())
                print("✅ ID is set successfully.")
                return id
            except ValueError:
                count += 1
                print("❌ Invalid input.")
                print(f"You still have {3 - count} tries.")
                print("Please enter an integer.")
        print("⚠️ Too many failed attempts. Try again later.")
        return None

   
   
    @staticmethod
    def set_name():
        count = 0
        while count < 3:
            name = input("Enter your name: ").strip().title()
            if name.replace(" ", "").isalpha():
                print("✅ Name accepted.")
                return name
            else:
                count += 1
                print("❌ Invalid input. Only letters are allowed.")
                print(f"You still have {3 - count} tries.")
        print("⚠️ Too many failed attempts. Try again later.")
        return None

   
   
    @staticmethod
    def set_specialty():
        count = 0
        while count < 3:
            specialty = input("Enter your specialty: ").strip().title()
            if specialty.replace(" ", "").isalpha():
                print("✅ Specialty accepted.")
                return specialty
            else:
                count += 1
                print("❌ Invalid input. Only letters are allowed.")
                print(f"You still have {3 - count} tries.")
        print("⚠️ Too many failed attempts. Try again later.")
        return None
    
    
    @staticmethod
    def generate_fixed_slots(start="09:00", end="17:00", interval=30):
        time_format = "%H:%M"
        slots = []
        start_time = datetime.strptime(start, time_format)
        end_time = datetime.strptime(end, time_format)

        while start_time < end_time:
            slots.append(start_time.strftime("%H:%M"))
            start_time += timedelta(minutes=interval)

        return slots
    

    @staticmethod
    def set_age():
        count=0
        while count<3:
            try:
                age=int(input("Enter your age : ").strip())
                if age<=0:
                    print("Age must be grater than zero ")
                    count+=1
                    print(f"You still have {3 - count} tries.")
                    continue
                else:
                    return age


            except ValueError:
                print(f"You still have {3 - count} tries.")
                print("❌ Invalid input. Only integers are allowed.")

                count+=1
        else:
            print("⚠️ Too many failed attempts. Try again later.")
            return None
        



    @staticmethod
    def check_phone():
        count = 0
        while count < 3:
            phone = input("Enter your phone number: ").strip()
            
            if phone.isdigit() and len(phone) == 11:
                if phone.startswith(('010', '011', '012', '015')):
                    print("✅ Phone number is accepted")
                    return phone
                else:
                    print("❌ Invalid phone prefix.")
            else:
                print("❌ Phone number must be exactly 11 digits.")

            count += 1
            print(f"You still have {3 - count} tries.")
        
        print("⚠️ Too many failed attempts. Try again later.")
        return None


    @staticmethod
    def check_gender():
        count = 0
        while count < 3:
            gender = input("Enter your gender (Male/Female): ").strip().lower()
            if gender in ['male', 'm']:
                print("✅ Gender accepted: Male")
                return "Male"
            elif gender in ['female', 'f']:
                print("✅ Gender accepted: Female")
                return "Female"
            else:
                count += 1
                print("❌ Invalid gender input. Please enter 'Male' or 'Female'.")
                print(f"You still have {3 - count} tries.")
        else:
            print("⚠️ Too many failed attempts. Try again later.")
            return None
        



def book_patient_appointment(patient, doctors):
    if not doctors:
        print("⚠️ No doctors available.")
        return
    doc_id = input("Enter Doctor ID: ")
    doctor = next((doc for doc in doctors if str(doc.doctor_id) == doc_id), None)
    if doctor:
        print("Available slots:")
        for slot in doctor.available_slots:
            print(f" - {slot}")
        slot_time = input("Enter slot time to book (HH:MM): ").strip()
        patient.book_appointment(doctor, slot_time)
    else:
        print("❌ Doctor not found.")

def cancel_patient_appointment(patient, doctors):
    doc_id = input("Enter Doctor ID: ")
    doctor = next((doc for doc in doctors if str(doc.doctor_id) == doc_id), None)
    if doctor:
        slot_time = input("Enter slot time to cancel (HH:MM): ").strip()
        patient.cancel_appointment(doctor, slot_time)
    else:
        print("❌ Doctor not found.")


def add_doctor(doctors):
    doc_id = Functions.set_id()
    name = Functions.set_name()
    specialty = Functions.set_specialty()
    slots = Functions.generate_fixed_slots()
    doctor = Doctor(doc_id, name, specialty, slots)
    doctors.append(doctor)
    print("✅ Doctor added successfully.")



def admin_menu(doctors):
    while True:
        print("\n--- Admin Menu ---")
        print("1. Add Doctor")
        print("2. View Doctors")
        print("3. Remove Doctor")
        print("4. Back to Main Menu")

        choice = input("Select an option: ").strip()

        if choice == '1':
            add_doctor(doctors)
        elif choice == '2':
            for doc in doctors:
                print(doc)
        elif choice == '3':
            doc_id = input("Enter Doctor ID to remove: ")
            doctors[:] = [doc for doc in doctors if str(doc.doctor_id) != doc_id]
            print("✅ Doctor removed (if ID was found).")
        elif choice == '4':
            break
        else:
            print("❌ Invalid option.")

def patient_menu(doctors, patients):
    print("\n--- Patient Registration ---")
    name = Functions.set_name()
    age = Functions.set_age()
    phone = Functions.check_phone()
    gender = Functions.check_gender()
    pid = Functions.set_id()

    patient = Patient(pid, name, age, phone, gender)
    patients.append(patient)

    while True:
        print("\n--- Patient Menu ---")
        print("1. View Doctors")
        print("2. Book Appointment")
        print("3. View My Appointments")
        print("4. Cancel Appointment")
        print("5. Back to Main Menu")

        choice = input("Select an option: ")

        if choice == '1':
            for doc in doctors:
                print(doc)
        elif choice == '2':
            book_patient_appointment(patient, doctors)
        elif choice == '3':
            patient.view_appointments()
        elif choice == '4':
            cancel_patient_appointment(patient, doctors)
        elif choice == '5':
            break
        else:
            print("❌ Invalid choice.")

        


def main_menu():
    doctors = []  
    patients = []  

    while True:
        print("\n" + "="*30)
        print("🏥 Welcome to the Clinic System")
        print("="*30)
        print("1. Admin")
        print("2. Patient")
        print("3. Exit")

        choice = input("Select an option (1-3): ").strip()

        if choice == '1':
            admin_menu(doctors)
        elif choice == '2':
            patient_menu(doctors, patients)
        elif choice == '3':
            print("👋 Exiting... Thank you!")
            break
        else:
            print("❌ Invalid option. Please try again.")



    

if __name__ == "__main__":
    main_menu()
