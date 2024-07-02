import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("My Calculator")

        self.expression = ""

        self.input_text = tk.StringVar()
        self.input_frame = tk.Frame(root)
        self.input_frame.pack()

        self.input_field = tk.Entry(self.input_frame, textvariable=self.input_text, font=('arial', 18, 'bold'), bd=10, insertwidth=4, width=14, justify='right')
        self.input_field.grid(row=0, column=0)
        self.input_field.pack(ipady=10)
        
        self.buttons_frame = tk.Frame(root)
        self.buttons_frame.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '(', 
            '1', '2', '3', '-', ')', 
            '0', '.', '=', '+', ' '
        ]
        row_val = 0
        col_val = 0
        for button in buttons:
            if button == ' ':
                continue
            button_command = lambda x=button: self.on_button_click(x)
            tk.Button(self.buttons_frame, text=button, width=10, height=3, command=button_command).grid(row=row_val, column=col_val, padx=1, pady=1)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1

    def on_button_click(self, button):
        if button == 'C':
            self.expression = ""
            self.input_text.set("")
        elif button == '=':
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("Error")
                self.expression = ""
        else:
            self.expression += str(button)
            self.input_text.set(self.expression)

root = tk.Tk()
app = Calculator(root)
root.mainloop()
