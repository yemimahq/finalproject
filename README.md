# 💼 Clinical Data Warehouse UI – Final Project (HI 741)

This Python-based desktop application supports the management of patient records and clinical notes using a simple Tkinter interface. Built with a soft **pink UI theme** for visual clarity and comfort, the program enables role-based access to patient data, allowing different users to interact with the system according to their permissions.

---

## 🌸 Key Features

- 🔐 **Role-based login** with credential verification  
- 📋 **Retrieve**, **add**, and **remove** patient records  
- 📝 **View clinical notes** by patient ID and date  
- 📆 **Count patient visits** for a specific date  
- 📊 **Generate summary statistics** with charts  
- 🧾 **Log all user actions** for auditing purposes

---

## 🔐 User Roles & Access

| **Role**       | **Access Level**                                              |
|----------------|---------------------------------------------------------------|
| `Clinician`    | Full access to patient data and all system features           |
| `Nurse`        | Same as Clinician                                             |
| `Admin`        | Can only count total visits (no access to PHI)                |
| `Management`   | Can generate system statistics (no access to patient records) |

---

## 📁 Project Structure

Yemimah_Ndoyi_FinalProject/
├── main_entry.py
├── clinical_ui.py
├── patient_data.py
├── login_user.py
├── helper_utils.py
├── README.md
├── requirements.txt
├── UML_Diagram.png
├── data/
│ ├── credentials.csv
│ ├── patients.csv
│ └── notes.csv
└── output/
├── usage_log.csv
└── updated_patients.csv

yaml
Copy
Edit

---

## ⚙️ How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt
2. Launch the application
bash
Copy
Edit
python main_entry.py
The UI will open in a soft pink theme. Enter credentials from credentials.csv to begin.

📦 Requirements
txt
Copy
Edit
pandas
matplotlib
Note: tkinter is built-in with most standard Python installations.

👩‍💻 Developer Info
Name: Yemimah Ndoyi
Course: HI 741 – Programming for Health Informatics
Instructor: Dr. Lu He
Semester: Spring 2025

