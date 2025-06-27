import tkinter as tk
from tkinter import messagebox
import random
import string

# Function to generate password
def generate_password():
    length = length_var.get()

    if not length.isdigit() or int(length) < 4:
        messagebox.showerror("Invalid Input", "Password length must be a number ≥ 4")
        return

    length = int(length)
    charset = ""

    if var_upper.get():
        charset += string.ascii_uppercase
    if var_lower.get():
        charset += string.ascii_lowercase
    if var_digits.get():
        charset += string.digits
    if var_symbols.get():
        charset += string.punctuation

    if not charset:
        messagebox.showwarning("No Option Selected", "Please select at least one character type.")
        return

    password = ''.join(random.choice(charset) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Copy to clipboard function
def copy_password():
    password = result_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create main window
root = tk.Tk()
root.title("Password Generator App")
root.geometry("400x400")
root.resizable(False, False)
root.config(padx=20, pady=20)

# Title
tk.Label(root, text="Password Generator", font=("Helvetica", 18, "bold")).pack(pady=10)

# Password length
tk.Label(root, text="Enter Password Length:").pack()
length_var = tk.StringVar()
tk.Entry(root, textvariable=length_var).pack(pady=5)

# Character options
tk.Label(root, text="Select character types:").pack(pady=5)

var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_symbols = tk.BooleanVar()

tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_upper).pack(anchor='w')
tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lower).pack(anchor='w')
tk.Checkbutton(root, text="Digits (0-9)", variable=var_digits).pack(anchor='w')
tk.Checkbutton(root, text="Symbols (!@#$)", variable=var_symbols).pack(anchor='w')

# Generate button
tk.Button(root, text="Generate Password", command=generate_password, bg="green", fg="white").pack(pady=15)

# Result
tk.Label(root, text="Generated Password:").pack()
result_entry = tk.Entry(root, font=("Helvetica", 12), justify="center")
result_entry.pack(pady=5)

# Copy button
tk.Button(root, text="Copy to Clipboard", command=copy_password, bg="blue", fg="white").pack(pady=10)

# Run the app
root.mainloop()
