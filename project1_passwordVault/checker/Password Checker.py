from tkinter import *
import time
from re import search

def mainScreen():
    global screen
    screen = Tk()
    screen.geometry("400x200")
    screen.title("Password Vault")

    global email
    global password
    global email_entry
    global password_entry
    global button
    
    email = StringVar()
    password = StringVar()
    
    Label(text = "Enter your email and password").pack()
    Label(text = "").pack()
    Label(text = "E Mail").pack()
    email_entry = Entry(textvariable = email)
    email_entry.pack()
    Label(text = "Password").pack()
    password_entry = Entry(textvariable = password)
    password_entry.pack()
    button = Button(text = "Save", width = 15, height = 1, command = checkInfo)
    button.pack()

def checkInfo():
    global email_info
    global password_info
    email_info = email.get()
    password_info = password.get()

    checkAt = "@"
    if search(checkAt, email_info):
        successInfo()
    else:
        failInfo()

def failInfo():
    button.config(state="disabled")
    fail = Label(text = "email must be valid!", fg = "red", font=("calibri", 11))
    fail.pack()
    screen.update()
    time.sleep(2)
    fail.destroy()
    button.config(state="normal")


def successInfo():
    file=open(email_info+".txt", "w")
    file.write(email_info)
    file.write("\n")
    file.write(password_info)
    file.close()

    button.config(state="disabled")
    done = Label(text = "Info Saved", fg = "green", font=("calibri", 11))
    done.pack()
    screen.update()
    time.sleep(2)
    done.destroy()
    button.config(state="normal")

mainScreen()
