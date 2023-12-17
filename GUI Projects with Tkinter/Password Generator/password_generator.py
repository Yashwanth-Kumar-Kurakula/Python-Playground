from PIL import Image
Image.CUBIC = Image.BICUBIC

import tkinter as tk
import ttkbootstrap as ttk
import random
import string
from tkinter import messagebox

def generate_password():
    global password_var, password_length_var, include_numbers_var, include_symbols_var, include_uppercase_var
    try:
        password_length = password_length_var.get()
    except ValueError:
        messagebox.showerror("Error", "Invalid Password Length given, please give integer values only.")
    else:
        password_characters = string.ascii_lowercase

        if include_uppercase_var.get() == 1:
            password_characters += string.ascii_uppercase
        if include_numbers_var.get() == 1:
            password_characters += string.digits
        if include_symbols_var.get() == 1:
            password_characters += string.punctuation

        password = "".join(random.choice(password_characters) for _ in range(password_length)) 
        password_var.set(password)
        
def add_to_file():
    global website_var, email_var, password_var
    if((website_var.get() is not None and website_var.get() != "") and (email_var.get() is not None and email_var.get() != "")):
        if (password_var.get() is not None and password_var.get() != ""):
            with open("passwords", "a") as f:
                f.writelines(f"{website_var.get()} | {email_var.get()} | {password_var.get()}\n")
        
        else:
            messagebox.showerror("Error", "Invalid Password Detected. Please enter a password or use the Generate Password button to create a new one")

    else:
        messagebox.showerror("Invalid Entries Detected", "Please check all the fields once again")


def apply_settings(amountused):
    global password_length_var
    amount_used_temp = amountused.get()
    password_length_var.set(amount_used_temp)

def additional_settings():
    global password_length_var, include_uppercase_var, include_numbers_var, include_symbols_var
    temp = password_length_var.get()
    top_level_window = tk.Toplevel(window)
    top_level_window.title("Additional Settings")

    password_length_label = ttk.Label(top_level_window, text="Password Length:")
    password_length_label.grid(row=1, column=0, sticky="W", padx=3, pady=3)

    password_length_entry = ttk.Meter(
        master=top_level_window,
        metertype="semi",
        amounttotal=30,
        amountused=temp,
        interactive=True,
        textright="characters",
    )
    password_length_entry.grid(row=0, column=1, rowspan=3)

    include_uppercase_cb = ttk.Checkbutton(top_level_window, 
                                           text="Include Uppercase", 
                                           offvalue=0, 
                                           onvalue=1, 
                                           variable=include_uppercase_var,
                                           bootstyle="round-toggle")
    include_uppercase_cb.grid(row=0, column=2, padx=3, pady=3, sticky="EW")

    include_numbers_cb = ttk.Checkbutton(top_level_window, 
                                           text="Include Numbers", 
                                           offvalue=0, 
                                           onvalue=1, 
                                           variable=include_numbers_var,
                                           bootstyle="round-toggle")
    include_numbers_cb.grid(row=1, column=2, padx=3, pady=3, sticky="EW")

    include_symbols_cb = ttk.Checkbutton(top_level_window, 
                                           text="Include Symbols", 
                                           offvalue=0, 
                                           onvalue=1, 
                                           variable=include_symbols_var,
                                           bootstyle="round-toggle"
                                           )
    include_symbols_cb.grid(row=2, column=2, padx=3, pady=3, sticky="EW")

    apply_settings_button = ttk.Button(top_level_window,text= "Apply Settings", command=lambda: apply_settings(password_length_entry.amountusedvar))
    apply_settings_button.grid(row=3, column=1, sticky="EW", padx=3, pady=3)



window = ttk.Window(themename="simplex")
window.title("Password Manager")
window.config(padx=20, pady=20)


password_length_var = tk.IntVar(value=12)
include_uppercase_var = tk.IntVar(value=1)
include_symbols_var = tk.IntVar(value=1)
include_numbers_var = tk.IntVar(value=1)

additional_settings_button = ttk.Button(window, text="≡", command=additional_settings, bootstyle="outline")
additional_settings_button.grid(row=0, column=2, sticky="E", padx=3, pady=3)

canvas = tk.Canvas(window, width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=1, column=1)

website_label = ttk.Label(window, text="Website:")
website_label.grid(row=2, column=0, sticky="EW")

website_var = tk.StringVar(value="")
website_entry = ttk.Entry(window, width=35, textvariable=website_var, text=website_var)
website_entry.focus()
website_entry.grid(row=2, column=1, columnspan=2, sticky="EW", padx=3, pady=3)

email_username_label = ttk.Label(window, text="Email/Username:")
email_username_label.grid(row=3, column=0, sticky="EW", padx=3, pady=3)

email_var = tk.StringVar(value="")
email_username_entry = ttk.Entry(window, width=35, textvariable=email_var, text=email_var)
email_username_entry.grid(row=3, column=1, columnspan=2, sticky="EW", padx=3, pady=3)

password_label = ttk.Label(window, text="Password:")
password_label.grid(row=4, column=0, sticky="EW", padx=3, pady=3)

password_var = tk.StringVar(value="")
password_entry = ttk.Entry(window, width=21, textvariable=password_var, text=password_var)
password_entry.grid(row=4, column=1, sticky="EW", padx=3, pady=3)

generate_password_button = ttk.Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(row=4, column=2, sticky="EW", padx=3, pady=3)

add_button = ttk.Button(window, text="Add", command=add_to_file)
add_button.grid(row=5, column=1, columnspan=2, sticky="EW", padx=3, pady=3)

window.mainloop()
