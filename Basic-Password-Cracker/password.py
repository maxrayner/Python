import hashlib

def common_passwords():
    print("First")
    user_hash_dict = {}
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

def common_passwords2():
    print("Second")
    user_hash_dict = {}
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

def common_passwords3():
    print("Third")
    user_hash_dict = {}
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

def books_lower():
    print("Fourth")
    user_hash_dict = {}
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

def books_orig():
    print("Fifth")
    user_hash_dict = {}
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

def books_upper():
    print("Sixth")
    user_hash_dict = {}
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

def books_var():
    print("Seventh")
    user_hash_dict = {}
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

def japanese_common():
    print("Eighth")
    user_hash_dict = {}
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
common_passwords()
common_passwords2()
common_passwords3()
books_lower()
books_orig()
books_upper()
books_var()     
japanese_common()    
