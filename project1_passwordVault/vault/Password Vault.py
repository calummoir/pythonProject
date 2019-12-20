from tkinter import *

def mainScreen():
    screen = Tk()
    screen.geometry("400x200")
    screen.title("Password Vault")

    global email
    global password
    global email_entry
    global password_entry
    
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
    Button(text = "Save", width = 15, height = 1, command = saveInfo).pack()

def saveInfo():
    email_info = email.get()
    password_info = password.get()

    file=open(email_info+".pwd", "w")
    file.write(email_info)
    file.write("\n")
    file.write(password_info)
    file.close()

    Label(text = "Info Saved", fg = "green", font=("calibri", 11)).pack()

    

mainScreen()
