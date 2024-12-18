import streamlit as st

# Title for the app
st.title("Calculator App")

# Input fields for numbers
num1 = st.number_input("Enter the first number", format="%.2f")
num2 = st.number_input("Enter the second number", format="%.2f")

# Dropdown to select operation
operation = st.selectbox("Select an operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Button to perform the calculation
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
            st.success(f"The result of addition is: {result:.2f}")
        elif operation == "Subtraction":
            result = num1 - num2
            st.success(f"The result of subtraction is: {result:.2f}")
        elif operation == "Multiplication":
            result = num1 * num2
            st.success(f"The result of multiplication is: {result:.2f}")
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
                st.success(f"The result of division is: {result:.2f}")
            else:
                st.error("Division by zero is not allowed.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
