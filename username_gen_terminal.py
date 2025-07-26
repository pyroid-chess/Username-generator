import random
import string

def generate_username(length):
    if length <= 0:
        return "Length must be positive."
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Ask user for desired username length
try:
    user_length = int(input("Enter the username length: "))
    username = generate_username(user_length)
    print("Generated Username:", username)
except ValueError:
    print("Please enter a valid number.")