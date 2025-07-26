import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_username(length):
    if length <= 0:
        return "Length must be positive."
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def on_click():
    try:
        user_in = int(entry.get())  # Try converting to int
        username = generate_username(user_in)
        result_label.config(text=f"Username: {username}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number")

# GUI setup
window = tk.Tk()
window.title("Username Generator")
window.geometry("500x600")

lab = tk.Label(window, text="Enter username length:")
lab.pack(pady=5)

entry = tk.Entry(window)
entry.pack(pady=5)

result_label = tk.Label(window, text="", wraplength=280, font=("Arial", 12))
result_label.pack(pady=10)

generate_btn = tk.Button(window, text="Generate Username", command=on_click)
generate_btn.pack(pady=5)

window.mainloop()