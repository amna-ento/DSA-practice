class Patient:

    def __init__(self, patient_id, name, age, gender, disease, severity, arrival_time, emergency=False):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease
        self.severity = severity
        self.arrival_time = arrival_time
        self.emergency = emergency

    def display(self):
        print("-------------------------------------")
        print("Patient ID   :", self.patient_id)
        print("Name         :", self.name)
        print("Age          :", self.age)
        print("Gender       :", self.gender)
        print("Disease      :", self.disease)
        print("Severity     :", self.severity)
        print("Arrival Time :", self.arrival_time)
        print("Emergency    :", self.emergency)
        print("-------------------------------------")

class HospitalManagementSystem:

    def __init__(self):
        self.waiting_queue = []
        self.emergency_queue = []
        self.treated_patients = []

        self.available_slots = ["Room-1", "Room-2", "Room-3", "Ambulance-1"]
        self.occupied_slots = []





    def register_patient(self):

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        severity = input("Enter Severity (Low/Medium/High): ")
        arrival_time = input("Enter Arrival Time: ")

        emergency = input("Is this an emergency patient? (yes/no): ").strip().lower()

        emergency_status = (emergency == "yes")

        patient = Patient(
            patient_id,
            name,
            age,
            gender,
            disease,
            severity,
            arrival_time,
            emergency_status
        )

        if emergency_status:
            self.emergency_queue.append(patient)
        else:
            self.waiting_queue.append(patient)

        print("\nPatient Registered Successfully!")





    def register_emergency_patient(self):

        patient_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        gender = input("Enter Gender: ")
        disease = input("Enter Disease: ")
        severity = input("Enter Severity (High/Critical): ")
        arrival_time = input("Enter Arrival Time: ")

        patient = Patient(
            patient_id,
            name,
            age,
            gender,
            disease,
            severity,
            arrival_time,
            True
        )

        self.emergency_queue.append(patient)

        print("\nEmergency Patient Registered Successfully!")





    def search_patient(self):

        search_id = input("Enter Patient ID to Search: ")

        for patient in self.emergency_queue:
            if patient.patient_id == search_id:
                print("\nPatient Found in Emergency Queue")
                patient.display()
                return

        for patient in self.waiting_queue:
            if patient.patient_id == search_id:
                print("\nPatient Found in Waiting Queue")
                patient.display()
                return

        for patient in self.treated_patients:
            if patient.patient_id == search_id:
                print("\nPatient Found in Treated Patients")
                patient.display()
                return

        print("\nPatient Not Found.")



 

    def allocate_slot(self):

        if len(self.available_slots) == 0:
            print("No Treatment Rooms Available.")
            return

        slot = self.available_slots.pop(0)
        self.occupied_slots.append(slot)

        print(slot, "Allocated Successfully.")





    def display_waiting_patients(self):

        if len(self.waiting_queue) == 0:
            print("\nNo Waiting Patients.")
            return

        print("\nWaiting Patients ")

        for patient in self.waiting_queue:
            patient.display()





    def display_emergency_patients(self):

        if len(self.emergency_queue) == 0:
            print("\nNo Emergency Patients.")
            return

        print("\nEmergency Patients")

        for patient in self.emergency_queue:
            patient.display()





    def merge(self, left, right, key):

        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):

            if getattr(left[i], key) <= getattr(right[j], key):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        while i < len(left):
            result.append(left[i])
            i += 1

        while j < len(right):
            result.append(right[j])
            j += 1

        return result




    def merge_sort(self, array, key):

        if len(array) <= 1:
            return array

        mid = len(array) // 2

        left = self.merge_sort(array[:mid], key)
        right = self.merge_sort(array[mid:], key)

        return self.merge(left, right, key)





    def sort_by_patient_id(self):

        if len(self.waiting_queue) == 0:
            print("No Waiting Patients.")
            return

        self.waiting_queue = self.merge_sort(self.waiting_queue, "patient_id")

        print("\nPatients Sorted by Patient ID Successfully.")

        self.display_waiting_patients()




    def sort_by_arrival_time(self):

        if len(self.waiting_queue) == 0:
            print("No Waiting Patients.")
            return

        self.waiting_queue = self.merge_sort(self.waiting_queue, "arrival_time")

        print("\nPatients Sorted by Arrival Time Successfully.")

        self.display_waiting_patients()




    def generate_report(self):

        print("\n Hospital Report ")

        print("\nTotal Waiting Patients :", len(self.waiting_queue))
        print("Total Emergency Patients :", len(self.emergency_queue))
        print("Total Treated Patients :", len(self.treated_patients))

        print("\nAvailable Slots")
        if len(self.available_slots) == 0:
            print("None")
        else:
            for slot in self.available_slots:
                print(slot)

        print("\nOccupied Slots")
        if len(self.occupied_slots) == 0:
            print("None")
        else:
            for slot in self.occupied_slots:
                print(slot)

        print("\nWaiting Patients")
        if len(self.waiting_queue) == 0:
            print("No Waiting Patients")
        else:
            for patient in self.waiting_queue:
                patient.display()

        print("\nEmergency Patients")
        if len(self.emergency_queue) == 0:
            print("No Emergency Patients")
        else:
            for patient in self.emergency_queue:
                patient.display()

        print("\nTreated Patients")
        if len(self.treated_patients) == 0:
            print("No Treated Patients")
        else:
            for patient in self.treated_patients:
                patient.display()

        print("\n========== End of Report ==========")









hospital = HospitalManagementSystem()
while True:
        print("\n Hospital Emergency Management System ")
        print("1. Register New Patient")
        print("2. Search Patient")
        print("3. Allocate Treatment Room")
        print("4. Display Waiting Patients")
        print("5. Display Emergency Patients")
        print("6. Sort Patients by Patient ID")
        print("7. Sort Patients by Arrival Time")
        print("8. Generate Hospital Report")
        print("9. Exit")

        try:
            choice = int(input("\nEnter your choice: "))
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:
            hospital.register_patient()

        elif choice == 2:
            hospital.search_patient()

        elif choice == 3:
            hospital.allocate_slot()

        elif choice == 4:
            hospital.display_waiting_patients()

        elif choice == 5:
            hospital.display_emergency_patients()

        elif choice == 6:
            hospital.sort_by_patient_id()

        elif choice == 7:
            hospital.sort_by_arrival_time()

        elif choice == 8:
            hospital.generate_report()

        elif choice == 9:
            print("Thank you for using Hospital Emergency Management System.")
            break

        else:
            print("Invalid choice! Please try again.")