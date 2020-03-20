from tkinter import *
import json
import hashlib

with open('db.json', 'w') as db:
    json.dump({'admin': '123'}, db)


def clear(event):
    caller = event.widget
    caller.delete('0', 'end')


def register():
    user = {username.get(): hashlib.sha256(password.get().encode()).hexdigest()}

    with open('db.json') as db:
        database = json.load(db)
    if username.get() in database.keys():
        return error.configure(text='Username already registered')
    if not username.get() or not password.get():
        return error.configure(text='Error occurred please try again.')
    with open('db.json', 'w') as db:
        database.update(user)
        json.dump(database, db)
    return error.configure(text='Registered successfully')


def login():
    user = {username.get(): hashlib.sha256(password.get().encode()).hexdigest()}
    if not username.get() or not password.get():
        return error.configure(text='Error occurred please try again.')
    with open('db.json') as db:
        database = json.load(db)
    if username.get() not in database.keys():
        return error.configure(text='Username not registered!')
    if user[username.get()] == database[username.get()]:
        return error.configure(text='Successfully logged in!')
    else:
        return error.configure(text='Wrong Password! Try again!')


window = Tk()
window.title('Login')
window.resizable(width=False, height=False)
window.configure(bg='lightblue')

lbl = Label(window, text='Welcome', font=('impact', 20), bg='lightblue')
lbl_username = Label(window, text='Username:')
username = Entry(window)
username.bind('<FocusIn>', clear)
lbl_password = Label(window, text='Password:')
password = Entry(window, show="*")
password.bind('<FocusIn>', clear)
login = Button(window, text='Login', bg='gray', command=login)
register = Button(window, text='register', bg='gray', command=register)
error = Label(window, text='', font=('impact', 10), bg='lightblue')

lbl.grid(row=0, columnspan=2)
lbl_username.grid(row=1, column=0)
username.grid(row=1, column=1, padx=(0, 10))
lbl_password.grid(row=2, column=0)
password.grid(row=2, column=1, padx=(0, 10))
login.grid(row=4, columnspan=2, padx=(0, 100), pady=(10, 10))
register.grid(row=4, columnspan=2, padx=(100, 0))
error.grid(row=5, columnspan=2)

window.mainloop()
