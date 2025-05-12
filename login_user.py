# login_user.py

import csv

def authenticate_user(username, password):
    with open("data/credentials.csv", newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['username'] == username and row['password'] == password:
                return row['role']
    return None
