from tkinter import *
import time
import re
import base64

def mainScreen():
    global screen
    screen = Tk()
    screen.geometry("400x300")
    screen.title("Password Vault")

    global email
    global password
    global button
    global encryptVar
    
    email = StringVar()
    password = StringVar()
    encryptVar = StringVar()
    
    Label(text = "Enter your email and password").pack()
    Label(text = "").pack()
    Label(text = "E Mail").pack()
    email_entry = Entry(textvariable = email)
    email_entry.pack()
    Label(text = "Password").pack()
    password_entry = Entry(textvariable = password)
    password_entry.pack()
    Label(text = "Encryption Key").pack()
    encrypt_entry = Entry(textvariable = encryptVar)
    encrypt_entry.pack()
    button = Button(text = "Save", width = 15, height = 1, command = checkInfo)
    button.pack()

def checkInfo():
    global email_info
    global password_info
    email_info = email.get()
    password_info = password.get()
    EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
    if not EMAIL_REGEX.fullmatch(email_info):
        failInfo()
    else:
        successInfo()
        

def failInfo():
    button.config(state="disabled")
    fail = Label(text = "email must be valid!", fg = "red", font=("calibri", 11))
    fail.pack()
    screen.update()
    time.sleep(2)
    fail.destroy()
    button.config(state="normal")


def successInfo():
    encrypt_info = encryptVar.get()
    if password_info == "":
        file=open(email_info+".txt", "r", encoding="utf-8")
        content = file.readlines()
        print (encode(encrypt_info, content[1], "d"))

    else:
        encrypted_password = encode(encrypt_info, password_info, "e")
        file=open(email_info+".txt", "w", encoding="utf-8")
        file.write(email_info)
        file.write("\n")
        file.write(encrypted_password)
        file.close()
        button.config(state="disabled")
        done = Label(text = "Info Saved", fg = "green", font=("calibri", 11))
        done.pack()
        screen.update()
        time.sleep(2)
        done.destroy()
        button.config(state="normal")

def encode(key, string, act='d'):
    encoded_chars = []
    for i in range(len(string)):
        key_c = key[i % len(key)]
        if act!='d':
            encoded_c = chr(ord(string[i]) + ord(key_c) % 256)
        else:
            encoded_c = chr((ord(string[i]) - ord(key_c) + 256) % 256)
        encoded_chars.append(encoded_c)
    encoded_string = ''.join(encoded_chars)
    return encoded_string

mainScreen()


























