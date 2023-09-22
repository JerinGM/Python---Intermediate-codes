from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    password_letters = [random.choice(letters) for char in range(nr_letters)]

    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]

    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers


    random.shuffle(password_list)
    #password = "".join(password_list)
    password = ""
    for char in password_list:
        password += char

    entryPass.insert(0, f"{password}")
    # print(f"Your password is: {password}")
    # copying my password to clipboard
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    passInput = entryPass.get()
    emailInput = entryEmail.get()
    webInput = entryWeb.get()
    if len(passInput) ==0 or len(webInput) == 0:
        messagebox.showinfo(message="Invalid Input")
    else:
        message = messagebox.askokcancel(title="Confirmation", message=f"Web: {webInput}\n Password: {passInput}\n Do you wish to continue")
        if message:
            with open("password.txt", mode="a") as file:
                file.write(f"{webInput} | {emailInput} | {passInput}\n")
            entryWeb.delete(0, END)
            entryPass.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=189)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 96, image=img)
canvas.grid(column=1, row=0)

labelWebsite = Label(text="Website:")
labelWebsite.grid(column=0, row=1)
labelEmailUsername = Label(text="Email/Username:")
labelEmailUsername.grid(column=0, row=2)
labelPassword = Label(text="Password:")
labelPassword.grid(column=0, row=3)

entryWeb = Entry(width=36)
entryWeb.grid(column=1, row=1, columnspan=2)
entryWeb.focus()

entryEmail = Entry(width=36)
entryEmail.insert(0, "jerin@xyz.com")
entryEmail.grid(column=1, row=2, columnspan=2)

entryPass = Entry(width=18)
entryPass.grid(column=1, row=3, columnspan=1)

buttonGenerate = Button(text="Generate Password", command=generate_password)
buttonGenerate.grid(column=2, row=3)
buttonAdd = Button(text="Add", width=31, command=add)
buttonAdd.grid(column=1, row=4, columnspan=2)

window.mainloop()
