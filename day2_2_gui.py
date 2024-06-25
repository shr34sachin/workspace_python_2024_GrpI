import tkinter as tk

win = tk.Tk()

# set geometry
win.geometry('500x500')
win.title('mero app')

button1 = tk.Button(win,text = 'close', width=20, command=win.destroy)
button1.pack(padx=20, pady=20)


win.mainloop()
