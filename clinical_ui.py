# clinical_ui.py

import tkinter as tk
from tkinter import messagebox, simpledialog
from login_user import authenticate_user
from patient_data import PatientDatabase
from helper_utils import log_usage, count_visits, generate_statistics, view_note

class ClinicalDataUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Clinical Data System - Yemimah")
        self.master.configure(bg="#ffc0cb")  
        self.username = None
        self.role = None
        self.patient_db = PatientDatabase("data/patients.csv")
        self.login_screen()

    def login_screen(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        tk.Label(self.master, text="Welcome to the Clinical Data Warehouse", font=("Segoe UI", 14, "bold")).pack(pady=10)
        tk.Label(self.master, text="Username").pack()
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack()
        tk.Label(self.master, text="Password").pack()
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack()
        tk.Button(self.master, text="Login", command=self.handle_login).pack()

    def handle_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = authenticate_user(username, password)
        if role:
            self.username = username
            self.role = role
            log_usage(username, role, "Login Successful")
            self.main_menu()
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")
            log_usage(username, "Unknown", "Login Failed")

    def main_menu(self):
        for widget in self.master.winfo_children():
            widget.destroy()
        actions = []
        if self.role in ["clinician", "nurse"]:
            actions = [
                ("Retrieve Patient", self.retrieve_patient),
                ("Add Patient", self.add_patient),
                ("Remove Patient", self.remove_patient),
                ("Count Visits", self.count_visits_ui),
                ("View Note", self.view_note_ui),
            ]
        elif self.role == "admin":
            actions = [("Count Visits", self.count_visits_ui)]
        elif self.role == "management":
            actions = [("Generate Statistics", self.generate_stats_ui)]
        actions.append(("Exit", self.master.quit))

        for (label, cmd) in actions:
            tk.Button(self.master, text=label, command=cmd).pack(pady=2)

    def retrieve_patient(self):
        pid = simpledialog.askstring("Retrieve", "Enter Patient ID")
        info = self.patient_db.retrieve_patient(pid)
        if info:
            messagebox.showinfo("Patient Info", info)
        else:
            messagebox.showwarning("Not Found", "Patient not found")

    def add_patient(self):
        self.patient_db.add_patient_ui(self.master)

    def remove_patient(self):
        pid = simpledialog.askstring("Remove", "Enter Patient ID")
        removed = self.patient_db.remove_patient(pid)
        if removed:
            messagebox.showinfo("Success", f"Patient {pid} removed")
        else:
            messagebox.showwarning("Not Found", "Patient not found")

    def count_visits_ui(self):
        date = simpledialog.askstring("Date", "Enter date (YYYY-MM-DD)")
        count = count_visits(date, self.patient_db.data)
        messagebox.showinfo("Visit Count", f"Visits on {date}: {count}")

    def view_note_ui(self):
        pid = simpledialog.askstring("Note", "Enter Patient ID")
        date = simpledialog.askstring("Note", "Enter Visit Date (YYYY-MM-DD)")
        note = view_note(pid, date)
        if note:
            messagebox.showinfo("Note", note)
        else:
            messagebox.showwarning("Not Found", "Note not found")

    def generate_stats_ui(self):
        generate_statistics(self.patient_db.data)
        messagebox.showinfo("Done", "Key statistics generated.")

