import tkinter as tk
class CounterApp:
    def __init__(self, win):
        self.win = win
        self.win.title('Counter App')
        self.win.geometry('500x200')
        
        self.counter = 0        
        self.label = tk.Label(win, text=f'Counter: {self.counter}')
        self.label.pack(pady=20)
        
        self.increment_btn = tk.Button(win, text='Increment', command=self.increment)
        self.increment_btn.pack(pady = 20)
        
        self.decrement_btn = tk.Button(win, text='Decrement', command=self.decrement)
        self.decrement_btn.pack(pady = 20)
        
    def increment(self):
        self.counter += 1
        self.label.config(text=f'Counter: {self.counter}')

    def decrement(self):
        self.counter -= 1
        self.label.config(text=f'Counter: {self.counter}')
        
window = tk.Tk()
app = CounterApp(window)

window.mainloop()