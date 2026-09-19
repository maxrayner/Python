# Password Cracker (without salts)

## About

Using the hashing.py python program, you can enter in a username + a password which is saved. Can test basic authentication via hashing.py as well as it has a sign in UI. Password.py uses the txt files with thousands of common passwords to compare against the users password and attempt to brute force it.

## Research

I conducted research to find txt files containing commonly used passwords, as the greater the volume the higher chance of successfully finding the real password. I also learnt about different types of hashing systems and why some are preferred over others, for instance SHA-256 outputs a 256 bit hash with no known collisions (when two strings share the same hash) which is relatively safer over MD5 which is faster yet the trade off is it outputs a 128 bit hash and vulnerable to hash collisions.


## How It Works

password.py:
* Reads in a line from one of the txt files
* Hashes the password
* Compares the hashed value with the hashed original password in the database (a txt file)
* If found, outputs the password in plain-text

hashingpy:
* Asks if the user wants to register/sign in
* If registering, asks for a username and password and stores username as plain-text and password as a hash using SHA-256
* If signing in, asks for username and a password and hashes the password, checks the database, and if it matches, allows the user to continue

## Technologies

* Python
* Hashing

## What I Learned

* Working with strings
* Using loops and conditional statements
* Reading data from a text file
* Using Git and GitHub
* Thinking about password security
* Decomposition 
* Dictionaries 
* Modules
* Hexadecimal hash representation
* String manipulation
* Dictionary attacks
* Hash comparison
* Hashing vs plain-text passwords
* SHA-256 and MD5


## Limitations

This project doesn't include salts which are a major factor in preventing both brute-force and rainbow table attacks, and therefore not realistic in the real world as most websites salt their stored passwords

## Future Improvements

* Add salting to hashing.py
* Improve efficiency by hashing all passwords in the txt files
