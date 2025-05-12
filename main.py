# main_entry.py

from clinical_ui import ClinicalDataUI
import tkinter as tk

if __name__ == "__main__":
    root = tk.Tk()
    app = ClinicalDataUI(root)
    root.mainloop()
