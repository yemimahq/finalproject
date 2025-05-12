# helper_utils.py

import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import csv


def log_usage(username, role, action):
    with open("output/usage_log.csv", "a", newline='') as f:
        writer = csv.writer(f)
        writer.writerow([datetime.now(), username, role, action])


def count_visits(date, df):
    return len(df[df['Visit_time'] == date])


def generate_statistics(df):
    plt.figure()
    df['Gender'].value_counts().plot(kind='bar')
    plt.title("Patient Gender Distribution")
    plt.ylabel("Count")
    plt.savefig("output/gender_stats.png")


def view_note(pid, date):
    notes = pd.read_csv("data/notes.csv")
    notes_filtered = notes[(notes['Patient_ID'] == pid) & (notes['Visit_time'] == date)]
    if notes_filtered.empty:
        return None
    return notes_filtered.iloc[0]['Note_text']
