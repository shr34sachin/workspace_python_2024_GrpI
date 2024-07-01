# To-Do List Application
import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")        
        self.tasks = []
        
        self.task_entry = tk.Entry(root)
        self.task_entry.pack(pady=10)        
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        
        self.listbox = tk.Listbox(root)
        self.listbox.pack(pady=10)
    
    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_listbox()
            self.task_entry.delete(0, tk.END)
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.tasks:
            self.listbox.insert(tk.END, task)

# Create the main window
root = tk.Tk()
# Create an instance of the ToDoApp
app = ToDoApp(root)
# Run the application
root.mainloop()

tk.Listbox.delete(0, tk.END)