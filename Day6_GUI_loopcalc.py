import tkinter as tk

win = tk.Tk()
win.title('calculator layout')

rowEntry = tk.Entry(win)
rowEntry.grid(row=0, column=0, padx = 20, pady = 20)
colEntry = tk.Entry(win)
colEntry.grid(row=1, column=0, padx=20, pady=20)

def generate():
    rows = int(rowEntry.get())
    columns = int(colEntry.get())
    
    # Create and place buttons in a grid
    for i in range(rows):
        for j in range(columns):
            button = tk.Button(win, text=f"Button {i+1},{j+1}")
            button.grid(row=i+3, column=j, padx=5, pady=5)
    
buttonGen = tk.Button(win, text='Generate', command=generate)
buttonGen.grid(row=2,column=0, padx=20, pady=20)
win.mainloop()