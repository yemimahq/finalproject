# patient_data.py

import pandas as pd
from tkinter import simpledialog
import uuid

class PatientDatabase:
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = pd.read_csv(filepath)

    def retrieve_patient(self, patient_id):
        visits = self.data[self.data['Patient_ID'] == patient_id]
        if visits.empty:
            return None
        latest = visits.sort_values("Visit_time", ascending=False).iloc[0]
        return latest.to_string()

    def remove_patient(self, patient_id):
        initial_len = len(self.data)
        self.data = self.data[self.data['Patient_ID'] != patient_id]
        self.data.to_csv("output/updated_patients.csv", index=False)
        return len(self.data) < initial_len

    def add_patient_ui(self, root):
        pid = simpledialog.askstring("Patient ID", "Enter Patient ID")
        visit_time = simpledialog.askstring("Visit Date", "Enter Visit Time")
        visit_id = str(uuid.uuid4())[:8]
        gender = simpledialog.askstring("Gender", "Gender")
        race = simpledialog.askstring("Race", "Race")
        age = simpledialog.askinteger("Age", "Age")
        ethnicity = simpledialog.askstring("Ethnicity", "Ethnicity")
        insurance = simpledialog.askstring("Insurance", "Insurance")
        zip_code = simpledialog.askstring("Zip", "Zip Code")
        complaint = simpledialog.askstring("Complaint", "Chief Complaint")
        new_row = {
            'Patient_ID': pid,
            'Visit_ID': visit_id,
            'Visit_time': visit_time,
            'Visit_department': 'General',
            'Gender': gender,
            'Race': race,
            'Age': age,
            'Ethnicity': ethnicity,
            'Insurance': insurance,
            'Zip code': zip_code,
            'Chief complaint': complaint
        }
        self.data = self.data.append(new_row, ignore_index=True)
        self.data.to_csv("output/updated_patients.csv", index=False)
