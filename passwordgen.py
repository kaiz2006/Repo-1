# password generator project
import random
print("Welcome to the password generator project")
length = int(input("Enter the desired length of your password: "))
def generate_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+"
    password = ''.join(random.choice(characters) for i in range(length))
    return password
print("Your generated password is:", generate_password())