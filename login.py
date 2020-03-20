from tkinter import *
import json
import hashlib

# File init
with open('db.json', 'w') as db:
    json.dump({'admin': '123'}, db)


# Clears entry on click
def clear(event):
    caller = event.widget
    caller.delete('0', 'end')


def register():
    username = register_username.get()
    user = {username: hashlib.sha256(register_password.get().encode()).hexdigest()}

    with open('db.json') as db:
        database = json.load(db)

    if username in database.keys():
        return register_error.configure(text='Username already registered')

    if not username or not register_password.get():
        return register_error.configure(text='Error occurred please try again.')

    with open('db.json', 'w') as db:
        database.update(user)
        json.dump(database, db)

    registerframe.pack_forget()
    main_page()
    return error.configure(text='Registered successfully')


def login():
    username = login_username.get()
    user = {username: hashlib.sha256(login_password.get().encode()).hexdigest()}

    if not username or not login_password.get():
        return login_error.configure(text='Error occurred please try again.')

    with open('db.json') as db:
        database = json.load(db)

    if username not in database.keys():
        return login_error.configure(text='Username not registered!')

    if user[username] == database[username]:
        loginframe.pack_forget()
        main_page()
        return error.configure(text='Successfully logged in!')

    return login_error.configure(text='Wrong Password! Try again!')


def main_page():
    loginframe.pack_forget()
    registerframe.pack_forget()
    mainframe.pack(padx=10, pady=10)
    lbl.grid(row=0, column=0, pady=10)
    login_btn.grid(row=1, column=0, pady=5)
    register_btn.grid(row=2, column=0, pady=5)
    error.grid(row=3, column=0)


def login_page():
    mainframe.pack_forget()
    loginframe.pack(padx=10, pady=10)
    login_back.grid(row=0, column=0)
    login_lbl.grid(row=0, columnspan=2, pady=10)
    login_lbl_username.grid(row=1, column=0)
    login_username.grid(row=1, column=1, padx=(0, 10))
    login_lbl_password.grid(row=2, column=0)
    login_password.grid(row=2, column=1, padx=(0, 10))
    login_login.grid(row=4, columnspan=2, pady=10)
    login_error.grid(row=5, columnspan=2)


def register_page():
    mainframe.pack_forget()
    registerframe.pack(padx=10, pady=10)
    register_back.grid(row=0, column=0, padx=(0, 15))
    register_lbl.grid(row=0, columnspan=2, pady=10)
    register_lbl_username.grid(row=1, column=0)
    register_username.grid(row=1, column=1, padx=(0, 10))
    register_lbl_password.grid(row=2, column=0)
    register_password.grid(row=2, column=1, padx=(0, 10))
    register_register.grid(row=4, columnspan=2, pady=10)
    register_error.grid(row=5, columnspan=2)


window = Tk()
window.title('Login')
window.resizable(width=False, height=False)
window.geometry('220x180')
window.configure(bg='lightblue')

mainframe = LabelFrame(window)
loginframe = LabelFrame(window)
registerframe = LabelFrame(window)

# main frame
lbl = Label(mainframe, text='Welcome', font=('impact', 20), width=15)
login_btn = Button(mainframe, text='Login', bg='gray', command=login_page, width=10)
register_btn = Button(mainframe, text='register', bg='gray', command=register_page, width=10)
error = Label(mainframe, text='', font=('impact', 10))

# login frame
login_back = Button(loginframe, text='Back', bg='gray', command=main_page)
login_lbl = Label(loginframe, text='login', font=('impact', 20))
login_lbl_username = Label(loginframe, text='Username:')
login_username = Entry(loginframe)
login_username.bind('<FocusIn>', clear)
login_lbl_password = Label(loginframe, text='Password:')
login_password = Entry(loginframe, show="*")
login_password.bind('<FocusIn>', clear)
login_login = Button(loginframe, text='Login', bg='gray', command=login)
login_error = Label(loginframe, text='', font=('impact', 10))

# register frame
register_back = Button(registerframe, text='Back', bg='gray', command=main_page)
register_lbl = Label(registerframe, text='register', font=('impact', 20))
register_lbl_username = Label(registerframe, text='Username:')
register_username = Entry(registerframe)
register_username.bind('<FocusIn>', clear)
register_lbl_password = Label(registerframe, text='Password:')
register_password = Entry(registerframe, show="*")
register_password.bind('<FocusIn>', clear)
register_register = Button(registerframe, text='register', bg='gray', command=register)
register_error = Label(registerframe, text='', font=('impact', 10))

main_page()

window.mainloop()
