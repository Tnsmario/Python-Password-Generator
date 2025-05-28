import random
import string

def generate_function(length=12):
    characters = string.digits + string.ascii_letters + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("This is your password: ", generate_function())