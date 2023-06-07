from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

def clear_placeholder(event, entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, END)

def login_button_clicked():
    username = user_name_entry.get()
    password = user_password_entry.get()
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Completed", "Login Successful!")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

def login_button_hover(event):
    login_button.config(bg="#FFD700", fg="#333333")

def login_button_leave(event):
    login_button.config(bg="#FFDF00", fg="#000000")

def create_user_clicked():
    create_user_window = Toplevel(window)
    create_user_window.geometry("400x400")
    create_user_window.config(bg="#F0F0F0", padx=20, pady=20)
    create_user_window.title("Create AkkiHub Account")

    # Username
    username_label = Label(create_user_window, text="Username:", font=("Arial", 12))
    username_label.grid(row=0, column=0, sticky="e")
    username_entry = Entry(create_user_window, width=30)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Name
    name_label = Label(create_user_window, text="Name:", font=("Arial", 12))
    name_label.grid(row=1, column=0, sticky="e")
    name_entry = Entry(create_user_window, width=30)
    name_entry.grid(row=1, column=1, padx=10, pady=10)

    # Password
    password_label = Label(create_user_window, text="Password:", font=("Arial", 12))
    password_label.grid(row=2, column=0, sticky="e")
    password_entry = Entry(create_user_window, show="*", width=30)
    password_entry.grid(row=2, column=1, padx=10, pady=10)

    # Re-enter Password
    reenter_label = Label(create_user_window, text="Re-enter Password:", font=("Arial", 12))
    reenter_label.grid(row=3, column=0, sticky="e")
    reenter_entry = Entry(create_user_window, show="*", width=30)
    reenter_entry.grid(row=3, column=1, padx=10, pady=10)

    # Mobile Number
    mobile_label = Label(create_user_window, text="Mobile Number:", font=("Arial", 12))
    mobile_label.grid(row=4, column=0, sticky="e")
    mobile_entry = Entry(create_user_window, width=30)
    mobile_entry.grid(row=4, column=1, padx=10, pady=10)

    def create_account():
        username = username_entry.get()
        name = name_entry.get()
        password = password_entry.get()
        reenter_password = reenter_entry.get()
        mobile = mobile_entry.get()

        if not (username and name and password and reenter_password and mobile):
            messagebox.showerror("Error", "Please fill in all fields.")
        elif password != reenter_password:
            messagebox.showerror("Error", "Passwords do not match.")
        else:
            credentials[username] = password
            messagebox.showinfo("Account Created", "Account has been successfully created!")

            create_user_window.destroy()

    submit_button = Button(create_user_window, text="Submit", font=("Arial", 12), command=create_account)
    submit_button.grid(row=5, column=1, padx=10, pady=10)

window.mainloop()
