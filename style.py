from tkinter import *

class Style():
    def clear_placeholder(event, entry_widget, placeholder):
        if entry_widget.get() == placeholder:
            entry_widget.delete(0, END)

    def login_button_hover(event):
        login_button.config(bg="#5F9EA0", fg="#333333")

    def login_button_leave(event):
        login_button.config(bg="#7AC5CD", fg="#000000")

    def create_user_hover(event):
        create_user.config(fg="#0000FF")

    def create_user_leave(event):
        create_user.config(fg="#000000")
        
class Database:
    def __init__(self):
        self.data = {"Password": ("User","Akshit","Suresh",7014673434),
                     "Akki1234": ("akshit@gmail.com","Akki","suresh", 789465123)}
        
    
    def login_button_clicked(self,username_entry,password_entry):
        username = username_entry.get()
        password = password_entry.get()
        
        if password in self.data and username == self.data[password]:
            messagebox.showinfo("Login Successful", "Login successful!")
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")
        
    def create_user_clicked(self,username_entry,password_entry):
        username = username_entry.get()
        password = password_entry.get()

        if username == self.data[password]:
            messagebox.showerror("Username Exists", "Username already exists. Please try again.")
        elif password in self.data:
            messagebox.showerror("Username Exists", "Username already exists. Please try again.")
        else:
            users[username] = password
            messagebox.showinfo("Account Created", "Account created successfully!")


        