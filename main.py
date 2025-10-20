from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', '  k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email, "password": password
    }}
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty.")
    else:
        #json.dump(new_data, data_file, indent =3)
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file) #load the data
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)  # upload the data
        else:
            data.update(new_data) #update the data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)  # upload the data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- Search SETUP ------------------------------- #
def search():
    website_to_read = website_entry.get()
    if len(website_to_read) == 0:
        messagebox.showinfo(title="Oops", message="Please key in the website to search.")
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)  # load the data
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="The file does not exist.")
        else:
            print("hello")
            email_to_read = (data.get(website_to_read)).get("email")
            password_to_read = (data.get(website_to_read)).get("password")
            messagebox.showinfo(title="Email & Password", message=f"Email: {email_to_read}\nPassword: {password_to_read}")



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

#Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

#Entries
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=60)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "angela@gmail.com")
password_entry = Entry(width=40)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password, width = 15)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=50, command=save)
add_button.grid(row=4, column=1, columnspan=2)
search_button = Button(text="Search", command=search, width = 15)
search_button.grid(row=1, column=2)

window.mainloop()