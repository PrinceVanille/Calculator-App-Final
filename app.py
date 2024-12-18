import tkinter as tk
from tkinter import messagebox
import math

# Function to evaluate the expression
def evaluate_expression():
    try:
        # Get the expression from the entry widget and evaluate it
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to clear the entry widget
def clear():
    entry.delete(0, tk.END)

# Function to append to the expression in the entry widget
def append_to_expression(symbol):
    entry.insert(tk.END, symbol)

# Function to handle operations using the math library (e.g., square root)
def handle_math_operation(operation):
    try:
        expression = entry.get()
        if operation == 'sqrt':
            result = math.sqrt(float(expression))
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

# Create the main window
root = tk.Tk()
root.title("Calculator")

# Create the input field for the expression
entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Button layout
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('C', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('sqrt', 5, 0)
]

# Create buttons dynamically
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=evaluate_expression)
    elif text == 'C':
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=clear)
    elif text == 'sqrt':
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda: handle_math_operation('sqrt'))
    else:
        button = tk.Button(root, text=text, width=10, height=3, font=("Arial", 18), command=lambda t=text: append_to_expression(t))
    button.grid(row=row, column=col)

# Start the application
root.mainloop()
