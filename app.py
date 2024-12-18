import streamlit as st
import math

# Functions for basic operations
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def square_root(x):
    if x < 0:
        return "Error! Negative number."
    return math.sqrt(x)

# Streamlit UI
st.title("Simple Calculator")

# User inputs
num1 = st.number_input("Enter first number", step=1.0)
num2 = st.number_input("Enter second number", step=1.0)
   
operation = st.radio(
    "Choose an operation",
    ("Add", "Subtract", "Multiply", "Divide", "Square Root")
)

if operation == "Add":
    result = add(num1, num2)
elif operation == "Subtract":
    result = subtract(num1, num2)
elif operation == "Multiply":
    result = multiply(num1, num2)
elif operation == "Divide":
    result = divide(num1, num2)
elif operation == "Square Root":
    result = square_root(num1)

# Display result
st.write(f"Result: {result}")
