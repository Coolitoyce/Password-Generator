# ==============================
import secrets
import string
import time
from tkinter import *

import pyperclip as pc

characters = string.ascii_letters + string.digits + string.punctuation


def generate_password():
    while True:
        password = "".join(secrets.choice(characters) for i in range(16))
        if (
            any(character.islower() for character in password)
            and any(character.isupper() for character in password)
            and sum(character in string.punctuation for character in password) == 2
            and sum(character.isdigit() for character in password) == 4
        ):
            text.config(state="normal")
            text.delete(1.0, END)
            text.insert(1.0, password)
            text.config(state="disabled")
            break


def copy():
    if text.compare("end-1c", "==", "1.0"):
        return

    else:
        pc.copy(str(text.get(1.0, END)))
        copiedLabel.pack(pady=2)
        window.update()
        time.sleep(1)
        copiedLabel.pack_forget()


window = Tk()
window.title("Password Generator")
window.geometry("500x300")
window.resizable(False, False)

keyImage = PhotoImage(file="assets\\key.png")
window.iconphoto(True, keyImage)

label = Label(
    window,
    text="Password Generator",
    font=("Consolas", 30),
    bg="black",
    fg="#00FF00",
    image=keyImage,
    compound="left",
)
label.pack(pady=5)

text = Text(window, font=("Consolas", 25), width=20, height=1, state="disabled")
text.pack(pady=5)

frame = Frame(window)
frame.pack(pady=5)

button = Button(
    frame,
    text="Generate",
    fg="blue",
    activeforeground="blue",
    font=("Consolas", 15),
    bd=1,
    relief="raised",
    command=generate_password,
)
button.pack(side=LEFT, padx=15)

copybutton = Button(
    frame,
    text="Copy",
    fg="blue",
    activeforeground="blue",
    font=("Consolas", 15),
    bd=1,
    relief="raised",
    command=copy,
)
copybutton.pack(side=RIGHT, padx=15)

copiedLabel = Label(
    window,
    text="Password Copied!",
    font=("Consolas", 30),
    bd=1,
    relief="raised",
    fg="cyan",
    bg="black",
)

window.mainloop()
# ==============================
