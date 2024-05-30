import tkinter as tk
from tkinter import messagebox
import time

def messageboxspam():
    root = tk.Tk()
    root.withdraw()
    while True:
        messagebox.showinfo("Rat", "Ratted")
        time.sleep(0.1)

if __name__ == "__main__":
    messageboxspam()
