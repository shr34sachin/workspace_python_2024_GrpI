# simple login form
import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title('LOGIN FORM')

def login():
    un = textbox_UN.get()
    pw = textbox_PASS.get()
    
    if un == 'admin' and pw == '12345':
        messagebox.showinfo('Login Success', 'Welcome Prabhat!')
    else:
        messagebox.showerror('Login Failed', 'Invalid Username or Password')

label_UN = tk.Label(win,text='USERNAME')
label_UN.grid(row=0, column=0, padx=20, pady=10)
textbox_UN =tk.Entry(win)
textbox_UN.grid(row=0, column=1, padx=20, pady=10)
label_PASS = tk.Label(win,text='PASSWORD')
label_PASS.grid(row=1, column=0, padx=20, pady=10)
textbox_PASS =tk.Entry(win, show='*')
textbox_PASS.grid(row=1, column=1, padx=20, pady=10)
btnLogin = tk.Button(win, text='Login', command=login)
btnLogin.grid(row=2, column=1, padx=20, pady=10)

def change_color():
    colorVal = radio_var.get()
    if colorVal == 1:
        win.config(bg='blue')
    if colorVal ==2:
        win.config(bg='red')
        
radio_var = tk.IntVar()
radioBtn = tk.Radiobutton(win, text='blue', 
                          variable = radio_var, value =1,
                          command=change_color)
radioBtn.grid(row=3, column=1, padx=20, pady =10)
radioBtn = tk.Radiobutton(win, text='red', 
                          variable = radio_var, value =2,
                          command=change_color)
radioBtn.grid(row=4, column=1, padx=20, pady =10)
win.mainloop()