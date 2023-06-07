from tkinter import *
from tkinter import messagebox
import webbrowser
from PIL import ImageTk, Image
from style import *

# Dictionary to store username-password pairs
credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

def clear_placeholder(event, entry_widget, placeholder):
    if entry_widget.get() == placeholder:
        entry_widget.delete(0, END)

window = Tk()
window.geometry("600x600")
window.anchor("center")
window.config(padx=2, pady=2)
window.title("Login screen")

# Open the image file
image = Image.open("image.jpg")

# Resize the image
new_size = (200, 200)  # Set the new size (width, height)
resized_image = image.resize(new_size)

# Create a PhotoImage object with the resized image
photo = ImageTk.PhotoImage(resized_image)

# Create a label and set the image
image_label = Label(window, image=photo)
image_label.grid(row=0, column=1)
title = Label(window, text="Sign in to AkkiHub", font=("Helvetica", 30, "bold"), fg="#333333")
title.grid(row=2, column=1)

user_name = Label(window, text="Username or email address:- ", font=("Arial", 25))
user_name.grid(row=3, column=1)
user_name_entry = Entry(window, text="Gmail", background="#FAEBD7", width=50)
placeholder_gmail = 'Gmail'
user_name_entry.insert(END, placeholder_gmail)  # Placeholder for Gmail field
user_name_entry.bind('<FocusIn>', lambda e: clear_placeholder(e, user_name_entry, placeholder_gmail))
user_name_entry.grid(row=4, column=1)

user_password = Label(window, text="Password: ", font=("Arial", 25))
user_password.grid(row=5, column=1)

user_password_entry = Entry(window, text="Password", background="#FAEBD7", width=50,show="*")
placeholder_password = 'Password'
user_password_entry.insert(END, placeholder_password)  # Placeholder for Password field
user_password_entry.bind('<FocusIn>', lambda e: clear_placeholder(e, user_password_entry, placeholder_password))
user_password_entry.grid(row=6, column=1)

def login_button_clicked():
    username = user_name_entry.get()
    password = user_password_entry.get()
    if username in credentials and credentials[username] == password:
        messagebox.showinfo("Login Completed", "Login Successful!")
        webbrowser.open("http://www.udemy.com")  # Redirect to your website
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password.")

def login_button_hover(event):
    login_button.config(bg="#5F9EA0", fg="#333333")

def login_button_leave(event):
    login_button.config(bg="#7AC5CD", fg="#000000")

# login_button = Button(window, text="Login", font=("Arial", 15), command=lambda: print("Login button clicked"))
# login_button.grid(row=7, column=1)
login_button = Button(
    window, text="Login", font=("Arial", 15), command=login_button_clicked,
    bg="#98F5FF", fg="#000000", activebackground="#FFD700", activeforeground="#333333"
)
login_button.grid(row=7, column=1)
login_button.bind("<Enter>", login_button_hover)
login_button.bind("<Leave>", login_button_leave)

# create_user = Button(window, text="New to AkkiHub? Create an account", font=("Arial", 12), command=lambda: print("create user"))
# create_user.grid(row=8, column=1)
def create_user_clicked():
    create_user_window = Toplevel(window)
    create_user_window.geometry("400x400")
    create_user_window.config(bg="#F0F0F0", padx=20, pady=20)
    create_user_window.title("Create AkkiHub Account")
    #will redirect to this screen

    # Username
    username_label = Label(create_user_window, text="Username:", font=("Arial", 12))
    username_label.grid(row=0, column=0, sticky="e")
    username_entry = Entry(create_user_window, width=30)
    username_entry.grid(row=0, column=1, padx=10, pady=10)

    # Name
    name_label = Label(create_user_window, text="Gmail:", font=("Arial", 12))
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

            # create_user_window.destroy()

    submit_button = Button(create_user_window, text="Submit", font=("Arial", 12), command=create_account)
    submit_button.grid(row=5, column=1, padx=10, pady=10)
    
    
    

def create_user_hover(event):
    create_user.config(fg="#0000FF")

def create_user_leave(event):
    create_user.config(fg="#000000")
    
create_user = Button(
    window, text="New to AkkiHub? Create an account", font=("Arial", 12), command=create_user_clicked,
    relief=FLAT, fg="#000000", activeforeground="#0000FF"
)
create_user.grid(row=8, column=1)
create_user.bind("<Enter>", create_user_hover)
create_user.bind("<Leave>", create_user_leave)

create_user.grid(row=8, column=1)
window.mainloop()
