import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.tasks_frame = tk.Frame(root)
        self.tasks_frame.pack()
        self.tasks_listbox = tk.Listbox(self.tasks_frame, height=10, width=50)
        self.tasks_listbox.pack(side=tk.LEFT)
        self.scrollbar = tk.Scrollbar(self.tasks_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tasks_listbox.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.tasks_listbox.yview)
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)
        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        if task != "":
            self.tasks.append(task)
            self.update_tasks()
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.tasks.pop(selected_task_index[0])
            self.update_tasks()

    def update_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.tasks_listbox.insert(tk.END, task)

root = tk.Tk()
app = ToDoApp(root)
root.mainloop()
