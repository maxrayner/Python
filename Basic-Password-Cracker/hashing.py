import hashlib
from getpass import getpass

database = {}

def load_password_file(path):
    db = {}
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            line = line.strip()
            if ":" in line:
                user, hash_val = line.split(":", 1)
                db[user] = hash_val
    return db

def username_checker():
    database = load_password_file("passwords.txt")
    username = input("Enter user: ")
    result = database.get(username)

    if result == None:
        print("This user does not exist")
        username_checker()
    else:
        password_checker(database, username)

def password_checker(database, username):
    password = getpass("Enter password: ")
    hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()

    if database.get(username) == hashed_password:
        checked(username)
    else:
        print("Wrong password")
        password_checker(database, username)

def register():
    username = input("Enter your desired username: ")
    confirm = input("Enter username again to confirm: ")
    with open("passwords.txt", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(username + ":"):
                print("Username already exists, choose another\n")
                register()

    if username == confirm:
        password = getpass("Enter your desired password: ")
        confirm = getpass("Enter your password: ")
        if password == confirm:
            print("Thank you for registering")
            print("Sign in below")
            print("")
            with open("passwords.txt", "r",encoding="utf-8") as f:
                lines = f.readlines()
            with open("passwords.txt", "w",encoding="utf-8") as f:
                password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                new_line = f"{username}:{password}\n"
                lines.insert(0, new_line)
                f.writelines(lines)
            username_checker()
        else:
            print(f"Passwords did not match ({password} + {confirm})")
            print("")
            register()
    else:
        print(f"Usernames did not match ({username} + {confirm})")
        print("")
        register()

def main():
    if __name__ == "__main__":
        print("Welcome to your workspace")
        print("To enter, you must register or have an account")
        print("")
        register_choice = input("Do you have an account (yes/no): ").lower()
        if register_choice == "yes":
            username_checker()
        else:
            register()

def checked(username):
    print(f"Welcome {username} to your database")
main()


