#!/usr/bin/env python3.8
from user import User
from user import Credentials

def create_new_user(username,password):
    """
    method to create new user with username and password
    """
    new_user = User(username,password)
    return new_user
def save_user(user):
    """method to save new user
    
    """
    user.save_user()
def display_user():
    """
    method to display new-user
    """
    return User.display_user()    
def login_user(username,password):
    """
    method that checks whether user exists and then logs in
    """
    check_user =Credentials.verify_user(username,password)
    return check_user
def create_new_credentials(account,userName,password):
    """
    cretae new credentials to credential list
    """
    new_credential =Credentials(account,userName,password)
    return new_credential
def save_credential(credential):
    """
    save new credential to credential list
    """
    credential.save_details()
def display_account_details():
    """
    diplay all saved credentials
    """ 
    return Credentials.display_crdentials   
    
def delete_credentials(credentials):
    """
    delete credentials from credential list
    """
    credentials.delete_credentials()
def find_credentials(account):
    """
    fumction that check if a credentials exists with that username and return true or false
    """
    return Credentials.if_credential_exist(account)  
def generate_password():
    """
    generates a random password for user
    """  
    auto_password =Credentials.generated_password()
    return auto_password
def copy_password(account):
    """
    function to copy password using pyperclip
    """   
    return Credentials.copy_password(account)
def passlocker():
    print("Welcome to password Locker . \n Choose one of the following to proceed .\n CA --Create New acount. \n LG ---To log in ") 
    short_code =input("").lower().strip()
    if short_code =="ca":
        print("Sign Up")
        print('*' *50)
        username =input("username: ")
        while True:
            print("TP -To type your own password:\n GP -To generate random password")
            password_Choice =input().lower().strip()
            if password_Choice =='tp':
                password = input("Enter password\n")
                break
            elif password_Choice =='gp':
                password =generate_password()
                break
            else:
                print("Invalid password please try again")
        save_user(create_new_user(username,password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created successfully!")
        print("*"*85)
    
    elif short_code =='lg':
        print("*"*50)
        print("Enter your username and your password to login: ")
        print("*"*50)  
        username =input("Username: ")
        password =input("Password: ")
        login =login_user(username,password)
        if login_user == login:
            print(f"Hello {username}. Welcome To password Locker manager")
            print('\n')  
        
                
    