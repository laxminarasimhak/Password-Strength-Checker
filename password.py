import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import re

# List of common passwords
COMMON_PASSWORDS = {
    "password", "123456", "12345678", "123456789", "qwerty",
    "abc123", "password1", "iloveyou", "111111", "admin", "welcome"
}

def check_consecutive(password):
    """Check for consecutive characters in the password."""
    deductions = 0
    # Check for consecutive letters (case insensitive)
    for i in range(len(password) - 2):
        if password[i].isalpha() and password[i + 1].isalpha() and password[i + 2].isalpha():
            if (ord(password[i].lower()) + 1 == ord(password[i + 1].lower()) and
                ord(password[i + 1].lower()) + 1 == ord(password[i + 2].lower())):
                deductions += 1

    # Check for consecutive digits
    for i in range(len(password) - 2):
        if password[i].isdigit() and password[i + 1].isdigit() and password[i + 2].isdigit():
            if (int(password[i]) + 1 == int(password[i + 1]) and
                int(password[i + 1]) + 1 == int(password[i + 2])):
                deductions += 1

    return deductions

def password_strength(password):
    """Evaluate the strength of the password."""
    # Check if the password is in the common passwords list
    if password.lower() in COMMON_PASSWORDS:
        return "Weak", "red"

    # Calculate length points
    length = len(password)
    if length >= 16:
        length_points = 3
    elif length >= 12:
        length_points = 2
    elif length >= 8:
        length_points = 1
    else:
        length_points = 0

    # Calculate character variety points
    has_lower = bool(re.search(r'[a-z]', password))
    has_upper = bool(re.search(r'[A-Z]', password))
    has_digit = bool(re.search(r'[0-9]', password))
    has_special = bool(re.search(r'[\W_]', password))  # Non-alphanumeric characters

    variety_points = sum([has_lower, has_upper, has_digit, has_special])

    # Calculate deductions for consecutive characters
    deductions = check_consecutive(password)

    # Total score
    total_score = length_points + variety_points - deductions

    # Determine strength based on total score
    if total_score <= 2:
        return "Weak", "red"
    elif total_score <= 4:
        return "Moderate", "orange"
    elif total_score <= 6:
        return "Strong", "yellow"
    else:
        return "Very Strong", "green"

def update_strength(event):
    """Update the password strength and indicator based on the current password."""
    password = password_entry.get()
    if password:  # Check if the password is not empty
        strength, color = password_strength(password)
        strength_label.config(text=f"Strength: {strength}", bg=color)
    else:
        strength_label.config(text="Strength: ", bg="#f5f5dc")  # Reset the strength label

def toggle_password():
    """Toggle the visibility of the password."""
    if password_entry.cget('show') == '':
        password_entry.config(show='*')
        toggle_button.config(text='Show')
    else:
        password_entry.config(show='')
        toggle_button.config(text='Hide')

# Create the main window
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("550x500")
root.configure(bg="#f5f5dc")  # Light beige background

# Create a title label
title_label = tk.Label(root, text="Password Strength Checker", font=("Times New Roman", 16, "bold"), bg="#f5f5dc", fg="#000080")
title_label.pack(pady=20)

# Create a label for instructions
label = tk.Label(root, text="Enter a password to check its strength:", font=("Times New Roman", 12), bg="#f5f5dc", fg="#0000FF")
label.pack(pady=10)

# Create a frame to hold the password entry and eye icon
entry_frame = tk.Frame(root, bg="#f5f5dc")
entry_frame.pack(pady=5)

# Create an entry widget
password_entry = tk.Entry(entry_frame, show='*', width=30, font=("Times New Roman", 12))
password_entry.pack(side=tk.LEFT)

# Create a button to toggle the password visibility
toggle_button = tk.Button(root, text='Show', command=toggle_password)
toggle_button.pack(pady=10)

# Bind the entry widget to update the strength automatically
password_entry.bind("<KeyRelease>", update_strength)

# Create a label to display the strength of the password
strength_label = tk.Label(root, text="Strength: ", font=("Times New Roman", 12), bg="#f5f5dc", fg="#000000", width=20)
strength_label.pack(pady=10)

# Create a label for password rules
rules_label = tk.Label(root, text="Password Creation Rules:\n"
                                   "- At least 8 characters long\n"
                                   "- Include both uppercase and lowercase letters\n"
                                   "- Include at least one digit\n"
                                   "- Include at least one special character (e.g., @, #, $, %)\n"
                                   "- Avoid common passwords", 
                       font=("Times New Roman", 10), bg="#f5f5dc", fg="#0000FF", justify="left")
rules_label.pack(pady=10)

# Run the application
root.mainloop()
