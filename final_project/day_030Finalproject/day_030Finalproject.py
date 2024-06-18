from tkinter import messagebox
from PIL import Image
import random
from customtkinter import *
import pyperclip
import json


# ---------------------------- SEARCH WEBSITE ----------------------------------- #
def search_website():
    # get the website need to search
    website_name = website_entry.get()
    try:
        with open("password_save.json", "r") as data_file:
            # load file data into memory (variable `data`)
            data = json.load(data_file)

    # if it can't find the find
    except FileNotFoundError:
        # so create a new file with an object in it
        with open("password_save.json", "w") as data_file:
            json.dump(dict(), data_file)
            # then say that no details for the website exists
            messagebox.showinfo(title='No data file found', message='No details for the website exists')

    # if it can open and load the file the show the username and password to the user
    else:
        try:
            # try to show the username and the password of that website ( can use > if website in data: < )
            messagebox.showinfo(title=website_name, message=f"Username: {data[website_name]["Username"]}\n"
                                                            f"Password: {data[website_name]["Password"]}")
        # it might cause an error because the user this website didn't exist
        except KeyError:
            messagebox.showinfo(title='No data file found', message='No details for the website exists')


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_generator():
    # all possible letters, numbers and symbols
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # make the length of the password randomly
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # then pick the letters, numbers and symbols random
    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    # add all the characters into as string
    password_list = password_letters + password_symbols + password_numbers

    # unscramble the string to make it random
    random.shuffle(password_list)
    password = "".join(password_list)

    # clear all the old user's password
    password_entry.delete(0, END)
    # insert the new password from the beginning
    password_entry.insert(index=0, string=password)
    # and finally auto copy the password that just generate
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def new_password():
    # get hold all the website, username and pass word that the user input
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    # use the data just get and turn it into a dictionary
    new_data = {
        website: {
            "Username": username,
            "Password": password
        }
    }
    # but if one of the username or website or password, the user didn't input, so it will show a message
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please enter all the entry")

    # else it will show a confirmation message
    elif messagebox.askokcancel('confirm information', f'This is the entered:\n'
                                                       f'Website: {website}\n'
                                                       f'Username: {username}\n'
                                                       f'Password: {password}'):
        # create an opening file mode (read).
        try:
            with open("password_save.json", "r") as data_file:
                # load file data into memory (variable `data`)
                data = json.load(data_file)

        except FileNotFoundError:
            with open("password_save.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            # append new data into variable `data`.
            data.update(new_data)
            # try to close data file instance
            data_file.close()

            # create another opening file mode (write).
            with open("password_save.json", "w") as data_file:
                # Dump/Save the content of `data` into stream (Opened file instance)
                json.dump(data, data_file, indent=4)
                # try to close data file instance
                data_file.close()

        finally:
            # after save the password delete the old website name and password that the user input
            password_entry.delete(0, END)
            website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = CTk()
window.title('Password Manager')
window.config(padx=50,
              pady=50,
              height=800,
              width=700, )

logo_image = CTkImage(light_image=Image.open("logo.png"),
                      dark_image=Image.open("logo.png"),
                      size=(200, 189))

# ---------------------------- FRAME ---------------------------------- #
username_frame = CTkFrame(window)
username_frame.grid(column=1, row=3)

website_frame = CTkFrame(window)
website_frame.grid(column=1, row=1)

# ---------------------------- LABEL ---------------------------------- #
image_label = CTkLabel(window, image=logo_image, text="")
image_label.grid(column=0, row=0, columnspan=2)

website_label = CTkLabel(window, text="Website")
website_label.grid(column=0, row=1)

username_label = CTkLabel(window, text="Email/Username")
username_label.grid(column=0, row=2)

password_label = CTkLabel(window, text="Password")
password_label.grid(column=0, row=3)

# ---------------------------- ENTRY AND BUTTON ----------------------- #
website_entry = CTkEntry(website_frame, width=200, placeholder_text="Amazon")
# set a default website for easier to test the new_password and search_website function
website_entry.insert(0, "Amazon")
website_entry.grid(column=0, row=0, padx=6, pady=4)
# make the cursor focus on the website_entry
website_entry.focus()

website_search_button = CTkButton(website_frame, text="Search", width=140, command=search_website)
website_search_button.grid(column=1, row=0, padx=6, pady=4)

username_entry = CTkEntry(window, width=352, placeholder_text="example@gmail.com")
# you can insert your email to this string vvv for multiple times use
username_entry.insert(0, "example@gmail.com")
username_entry.grid(column=1, row=2, padx=6, pady=4)

password_entry = CTkEntry(username_frame, width=200)
password_entry.grid(column=0, row=0, padx=6, pady=4)
# set a default password for easier to test the new_password and search_website function
password_entry.insert(0, "123456")

password_generate_button = CTkButton(username_frame, text="Generate Password", width=140, command=password_generator)
password_generate_button.grid(column=1, row=0, padx=6, pady=4)

add_button = CTkButton(window, text="Add", width=350, command=new_password)
add_button.grid(column=1, row=4, padx=6, pady=4)

window.mainloop()
