import tkinter as tk
import random

def password_generator():
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ~!@#$%^&*()_+><?|0123456789abcdefghijklmnopqrstuvwxyz"
    length = int(length_entry.get())
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    password_var.set(password)
    if length < 4:
        strength_var.set("Short length password")
    elif length < 7:
        strength_var.set("Medium length password")
    else:
        strength_var.set("High length password")

def on_enter(e):
    generate_button['background'] = '#0000CD' # change color when mouse is over the button

def on_leave(e):
    generate_button['background'] = '#0000FF' # change color back when mouse leaves the button

root = tk.Tk()
root.geometry("400x450")
root.title("My Enhanced Password Generator")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="My Enhanced Password Generator", font=("Arial", 20), bg="#f0f0f0", fg="#333")
title_label.pack(pady=10)

length_frame = tk.Frame(root, bg="#f0f0f0")
length_frame.pack()

length_label = tk.Label(length_frame, text="Password Length:", font=("Arial", 14), bg="#f0f0f0", fg="#333")
length_label.pack(side=tk.LEFT, padx=5)

length_entry = tk.Entry(length_frame, bd=2, font=("Arial", 14))
length_entry.pack(side=tk.LEFT, padx=5)

generate_button = tk.Button(root, text="Generate Password", command=password_generator, bg="#0000FF", fg="#fff", bd=2, font=("Arial", 12), padx=20, pady=10) # Change button color to blue
generate_button.pack(pady=10)
generate_button.bind("<Enter>", on_enter)
generate_button.bind("<Leave>", on_leave)

password_var = tk.StringVar()
password_label = tk.Label(root, textvariable=password_var, font=("Arial", 12), bg="#f0f0f0", fg="#333")
password_label.pack()

strength_var = tk.StringVar()
strength_label = tk.Label(root, textvariable=strength_var, font=("Arial", 12), bg="#f0f0f0", fg="#333")
strength_label.pack()

root.mainloop()
