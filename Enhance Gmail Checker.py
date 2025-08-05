import customtkinter as ctk
import re
from tkinter import messagebox

ctk.set_appearance_mode("System")   # Auto light/dark based on OS
ctk.set_default_color_theme("blue") # You can change theme colors

def validate_email_logic(email):
    # simplified translation of your original validation:
    k = d = j = 0
    if len(email) < 6:
        return False, "Email less than 6 characters"
    if not email[0].isalpha():
        return False, "First character must be a letter"
    if email.count('@') != 1:
        return False, "Must contain exactly one @"
    if not (email.lower().endswith('.com') or email.lower().endswith('.in')):
        return False, "Email must end with .com or .in"
    for ch in email:
        if ch.isspace():
            k = 1
        elif ch.isalpha() and ch.isupper():
            d = 1
        elif not (ch.isalnum() or ch in '._@'):
            j = 1
    if k or d or j:
        return False, "Contains uppercase, space, or invalid character"
    return True, "Email is valid"

def on_validate():
    email = entry.get().strip()
    ok, msg = validate_email_logic(email)
    if ok:
        messagebox.showinfo("✅ Success", msg)
    else:
        messagebox.showerror("❌ Error", msg)

# Build the polished UI
root = ctk.CTk()
root.title("Email Validator")
root.geometry("450x200")

frame = ctk.CTkFrame(master=root, corner_radius=12, fg_color="#f0f0f0")
frame.pack(padx=20, pady=20, fill="both", expand=True)

ctk.CTkLabel(master=frame, text="Enter your email:", font=("Roboto", 14)).pack(pady=(10,5))
entry = ctk.CTkEntry(master=frame, width=360, placeholder_text="your.email@example.com")
entry.pack(pady=(0,15))

validate_btn = ctk.CTkButton(master=frame, text="Validate Email", command=on_validate, width=160, corner_radius=8)
validate_btn.pack(pady=(0,10))

root.mainloop()
