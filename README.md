# PASSWD MANAGER

#### Video Demo: url

### Description
This is a Password Manager Project created for [CS50 Introduction to Programming with Python](https://www.edx.org/school/harvardx). This is a simple program that securely stores the password for different websites.

### Local Installation
1. **Installation:** Ensure you have Python installed on your system.
    ```
    https://www.python.org/downloads/
2. **Clone or download the repository:** Clone or download this repository to your system.
    ```
    https://github.com/kam2ss/CS50P.git
3. **Run the Program:** This is a cli based program, so run it using the terminal, navigate to the project folder, and run 'python project.py'.
    ```
    python project.py
    ```

### Features
1. **Master Password:** Upon launching the program, you will be prompted to create a master password and confirm it.
2. **Validate Password:** After creating the master password, you will be asked to input the master password. Once confirmed, that is your master password to access the password vault. 
3. **Secure Password:** The master password is salted and hashed using the bcrypt module for security, ensuring it is not stored in plain text.
4. **Password File:** Once you have access, you can now add passwords for different websites.
5. **View Passwords:** The Password Manager allows you to view stored passwords in tabular format.

### Security
The Password Manager prioritises security, utilising the bcrypt module for password hashing and encryption. Your master password and the rest of the passwords in a password file are never stored in plain text.