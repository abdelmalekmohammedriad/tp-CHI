import hashlib
import sys


def hash_pass(password):

    return hashlib.sha256(password.encode()).hexdigest()


def register():
    username = input("Enter new username: ").strip()
    password = input("Enter new password: ").strip()


    with open("users.txt", "r") as file:
        users =  file.readlines()

    if username in users:
        print("Username already exist chose another one.")
        return

    hashed_password = hash_pass(password)
    with open("users.txt", "a") as file:
        file.write(f"{username},{hashed_password}\n")


    with open("admin.txt", "a") as file:
        file.write(f"{username},{password}\n")

    print("Registration done")


def login():
    username = input("Enter your username: ").strip()
    password = input("Enter your password: " ).strip()
    hashed_password = hash_pass(password)

    with open("users.txt", "r") as file:
        users = file.readlines()

    for user in users:
        stored_username, stored_password = user.strip().split(",")
        if username == stored_username and hashed_password == stored_password:
            print(f"Welcome, {username}!")
            return True

    print("Invalid username or password.")
    ethent()
    return False


def ethent():
    print("Welcome! Please choose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    choice = input("Enter 1 or 2 or 3: ").strip()

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("see you next time!!")
        sys.exit()

    else:
        print("Invalid choice. Please restart the program.")














