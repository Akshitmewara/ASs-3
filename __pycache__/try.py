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
    print("Create user")

def create_user_hover(event):
    create_user.config(fg="#0000FF")

def create_user_leave(event):
    create_user.config(fg="#000000")

window = Tk()
window.geometry("600x600")
window.config(bg="#F0F0F0", padx=20, pady=20)
window.title("AkkiHub Login")
# window.iconbitmap("download.png")  # Replace "icon.ico" with the path to your desired icon file

# Open the image file
image = Image.open("image.jpg")

# Resize the image
new_size = (200, 200)  # Set the new size (width, height)
resized_image = image.resize(new_size)

# Create a PhotoImage object with the resized image
photo = ImageTk.PhotoImage(resized_image)

# Create a label and set the image
image_label = Label(window, image=photo)
image_label.grid(row=0, column=1, padx=20, pady=20)
title = Label(window, text="Sign in to AkkiHub", font=("Helvetica", 30, "bold"), fg="#333333")
title.grid(row=2, column=1)

entry_style = {
    "background": "#FAEBD7",
    "width": 50,
    "border": 0,
    "highlightthickness": 1,
    "highlightbackground": "#CCCCCC",
    "highlightcolor": "#999999",
    "font": ("Arial", 12)
}

user_name = Label(window, text="Username or email address:", font=("Arial", 25))
user_name.grid(row=3, column=1)
user_name_entry = Entry(window, **entry_style)
placeholder_gmail = 'Gmail'
user_name_entry.insert(END, placeholder_gmail)  # Placeholder for Gmail field
user_name_entry.bind('<FocusIn>', lambda e: clear_placeholder(e, user_name_entry, placeholder_gmail))
user_name_entry.grid(row=4, column=1)

user_password = Label(window, text="Password:", font=("Arial", 25))
user_password.grid(row=5, column=1)

user_password_entry = Entry(window, **entry_style)
placeholder_password = 'Password'
user_password_entry.insert(END, placeholder_password)  # Placeholder for Password field
user_password_entry.bind('<FocusIn>', lambda e: clear_placeholder(e, user_password_entry, placeholder_password))
user_password_entry.grid(row=6, column=1)

login_button = Button(
    window, text="Login", font=("Arial", 15), command=login_button_clicked,
    bg="#FFDF00", fg="#000000", activebackground="#FFD700", activeforeground="#333333"
)
login_button.grid(row=7, column=1)
login_button.bind("<Enter>", login_button_hover)
login_button.bind("<Leave>", login_button_leave)

create_user = Button(
    window, text="New to AkkiHub? Create an account", font=("Arial", 12), command=create_user_clicked,
    relief=FLAT, fg="#000000", activeforeground="#0000FF"
)
create_user.grid(row=8, column=1)
create_user.bind("<Enter>", create_user_hover)
create_user.bind("<Leave>", create_user_leave)

# Dictionary to store username-password pairs
credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

window.mainloop()
