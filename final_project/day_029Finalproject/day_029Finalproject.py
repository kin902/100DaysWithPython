from tkinter import messagebox
from PIL import Image
import random
from customtkinter import *
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, END)
    password_entry.insert(index=0, string=password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def new_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(username) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please enter all the entry")
    elif messagebox.askokcancel('confirm information', f'This is the entered:\n'
                                                       f'Website: {website}\n'
                                                       f'Username: {username}\n'
                                                       f'Password: {password}'):
        with open("./password_save.txt", "a") as data:
            new_line = f"{website} | {username} | {password}"
            data.write(f"{new_line}\n")
            data.close()

        password_entry.delete(0, END)
        website_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = CTk()
window.title('Password Manager')
window.config(padx=50,
              pady=50,
              height=800,
              width=700, )

logo_image = CTkImage(light_image=Image.open("./logo.png"),
                      dark_image=Image.open("./logo.png"),
                      size=(200, 189))

image_label = CTkLabel(window, image=logo_image, text="")
image_label.grid(column=0, row=0, columnspan=2)

website_label = CTkLabel(window, text="Website")
website_label.grid(column=0, row=1)

username_label = CTkLabel(window, text="Email/Username")
username_label.grid(column=0, row=2)

password_label = CTkLabel(window, text="Password")
password_label.grid(column=0, row=3)

website_entry = CTkEntry(window, width=352, placeholder_text="Amazon")
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

username_entry = CTkEntry(window, width=352, placeholder_text="example@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2, padx=6, pady=4)

frame = CTkFrame(window)
frame.grid(column=1, row=3)

password_entry = CTkEntry(frame, width=200)
password_entry.grid(column=0, row=0, columnspan=1, padx=6, pady=4)

password_generate_button = CTkButton(frame, text="Generate Password", width=140, command=password_generator)
password_generate_button.grid(column=1, row=0, columnspan=1, padx=6, pady=4)

add_button = CTkButton(window, text="Add", width=350, command=new_password)
add_button.grid(column=1, row=4, padx=6, pady=4)

window.mainloop()
