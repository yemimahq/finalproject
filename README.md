# Clinical Data Warehouse UI – Final Project (HI 741)

This project is a Python-based desktop application developed for managing patient records and clinical notes in a clinical setting. The program provides a user interface using Tkinter and supports role-based access to ensure data security and compliance with privacy standards.

---

## Features

- Role-based login system with credential verification
- Retrieve, add, and remove patient records
- View clinical notes by patient ID and visit date
- Count total patient visits on a specific date
- Generate basic statistics and visual summaries
- Record all user actions in a usage log for audit tracking

---

## User Roles and Permissions

| Role        | Access Level                                             |
|-------------|----------------------------------------------------------|
| Clinician   | Full access to all features and patient data             |
| Nurse       | Same access as clinician                                 |
| Admin       | Can count patient visits only                            |
| Management  | Can generate system statistics (no access to PHI)        |

---

## Project Structure

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

## Installation and Usage

1. **Install dependencies**  
   Open a terminal in the project directory and run:
   ```bash
   pip install -r requirements.txt
Run the program

bash
Copy
Edit
python main_entry.py
Login
Use credentials found in data/credentials.csv.

Requirements
txt
Copy
Edit
pandas
matplotlib
Note: tkinter is included by default in most Python installations.

Author
Name: Yemimah Ndoyi
Course: HI 741 – Programming for Health Informatics
Instructor: Dr. Lu He
Semester: Spring 2025

yaml
Copy
Edit

---

Let me know if you'd like me to save this as a `README.md` file for you.





You said:
Make it look cool though still like make it color coded pink in some parts


ChatGPT said:
Perfect — here's a professional yet visually appealing README.md with subtle pink accents using markdown best practices. It’s clean, academic, and still has personality 🌸.

markdown
Copy
Edit
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

