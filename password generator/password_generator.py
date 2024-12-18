import streamlit as st
import random
import string

# Function to generate the password
def generate_password(length, use_uppercase, use_digits, use_special_chars):
    # Define character sets
    lowercase = string.ascii_lowercase  # a-z
    uppercase = string.ascii_uppercase  # A-Z
    digits = string.digits              # 0-9
    special_chars = string.punctuation  # Special characters (e.g., @, #, $, etc.)

    # Initialize the pool of characters
    characters = lowercase

    # Add character sets based on user input
    if use_uppercase:
        characters += uppercase
    if use_digits:
        characters += digits
    if use_special_chars:
        characters += special_chars

    # Ensure password length is valid
    if length < 6:
        length = 6
    
    # Generate password by randomly choosing characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Streamlit app UI
st.title('Password Generator')

# User inputs
length = st.slider('Password Length', 6, 32, 12)  # Length between 6 and 32
use_uppercase = st.checkbox('Include Uppercase Letters', True)
use_digits = st.checkbox('Include Digits', True)
use_special_chars = st.checkbox('Include Special Characters', True)

# Button to generate password
if st.button('Generate Password'):
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    st.success(f"Your generated password is: **{password}**")
