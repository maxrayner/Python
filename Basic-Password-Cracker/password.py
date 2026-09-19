import hashlib

def common_passwords():
    print("Checking...")
    user_hash_dict = {}
    try:
        with open("common_passwords.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            for username, hash in user_hash_dict.items():
                if hashed_password == hash:
                    print(f"HASH FOUND\n{username} : {password}")
    except FileNotFoundError:
        print("ERROR: File not found")


def common_passwords2():
    print("Checking...")
    user_hash_dict = {}
    try:
        with open("common_passwords2.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()

        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
                hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
                for username, hash in user_hash_dict.items():
                    if hashed_password == hash:
                        print(f"HASH FOUND\n{username} : {password}")
    except FileNotFoundError:
        print("ERROR: File not found")
        

def common_passwords3():
    print("Checking...")
    user_hash_dict = {}
    try: 
        with open("common_passwords3.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            for username, hash in user_hash_dict.items():
                if hashed_password == hash:
                    print(f"HASH FOUND\n{username} : {password}")
    except FileNotFoundError:
        print("ERROR: File not found")

def books_lower():
    print("Checking...")
    user_hash_dict = {}
    try:
        with open("greatest_books_of_all_time_lowercase.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            for username, hash in user_hash_dict.items():
                if hashed_password == hash:
                    print(f"HASH FOUND\n{username} : {password}")

    except FileNotFoundError:
        print("ERROR: File not found")

def books_orig():
    print("Checking...")
    user_hash_dict = {}
    try:
        with open("greatest_books_of_all_time_original.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            for username, hash in user_hash_dict.items():
                if hashed_password == hash:
                    print(f"HASH FOUND\n{username} : {password}")

    except FileNotFoundError:
        print("ERROR: File not found")

def books_upper():
    print("Checking...")
    user_hash_dict = {}
    try:
        with open("greatest_books_of_all_time_uppercase.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            for username, hash in user_hash_dict.items():
                if hashed_password == hash:
                    print(f"HASH FOUND\n{username} : {password}")

    except FileNotFoundError:
        print("ERROR: File not found")

def books_var():
    print("Checking...")
    user_hash_dict = {}
    try:
        with open("greatest_books_of_all_time_with_leet_variations.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            for username, hash in user_hash_dict.items():
                if hashed_password == hash:
                    print(f"HASH FOUND\n{username} : {password}")
    except FileNotFoundError:
        print("ERROR: File not found")
def japanese_common():
    print("Checking...")
    user_hash_dict = {}
    try:
        with open("japanese_common.txt", "r", encoding="utf-8") as file:
            common_passwords = file.read().splitlines()
        with open("passwords.txt", "r", encoding="utf-8") as file:
            text = file.read().splitlines()
            for user_hash in text:
                username = user_hash.split(":")[0]
                hash = user_hash.split(":")[1]
                user_hash_dict[username] = hash

        for password in common_passwords:
            hashed_password = hashlib.sha256(password.encode("utf-8")).hexdigest()
            for username, hash in user_hash_dict.items():
                if hashed_password == hash:
                    print(f"HASH FOUND\n{username} : {password}")
    except FileNotFoundError:
        print("ERROR: File not found")

def main():
    common_passwords()
    common_passwords2()
    common_passwords3()
    books_lower()
    books_orig()
    books_upper()
    books_var()     
    japanese_common()    

main()
