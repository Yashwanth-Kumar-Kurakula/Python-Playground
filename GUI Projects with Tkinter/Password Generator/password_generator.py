import tkinter as tk
import ttkbootstrap as ttk
import random
import string

#Password Generator
def generate_password():
    global password_var
    password_length = 12
    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(password_characters) for _ in range(password_length)) 
    password_var.set(password)
    
#Add Passwords to a file
def add_to_file():
    global website_var, email_var, password_var
    if((website_var.get() is not None and website_var.get() != "") and (email_var.get() is not None and email_var.get() != "")):
        if (password_var.get() is not None and password_var.get() != ""):
            with open("passwords", "a") as f:
                f.writelines(f"{website_var.get()} | {email_var.get()} | {password_var.get()}\n")
        
        else:
            print("Invalid Password")

    else:
        print("Debug Successful")


# UI Setup
window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)


canvas = tk.Canvas(window, width=200, height=200)
logo = tk.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

website_label = ttk.Label(window, text="Website:")
website_label.grid(row=1, column=0, sticky="EW")

website_var = tk.StringVar(value="")
website_entry = ttk.Entry(window, width=35, textvariable=website_var, text=website_var)
website_entry.focus()
website_entry.grid(row=1, column=1, columnspan=2, sticky="EW", padx=3, pady=3)

email_username_label = ttk.Label(window, text="Email/Username:")
email_username_label.grid(row=2, column=0, sticky="EW", padx=3, pady=3)

email_var = tk.StringVar(value="")
email_username_entry = ttk.Entry(window, width=35, textvariable=email_var, text=email_var)
email_username_entry.grid(row=2, column=1, columnspan=2, sticky="EW", padx=3, pady=3)

password_label = ttk.Label(window, text="Password:")
password_label.grid(row=3, column=0, sticky="EW", padx=3, pady=3)

password_var = tk.StringVar(value="")
password_entry = ttk.Entry(window, width=21, textvariable=password_var, text=password_var)
password_entry.grid(row=3, column=1, sticky="EW", padx=3, pady=3)

generate_password_button = ttk.Button(window, text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2, sticky="EW", padx=3, pady=3)

add_button = ttk.Button(window, text="Add", command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW", padx=3, pady=3)

window.mainloop()
