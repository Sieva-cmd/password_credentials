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
    return Credentials.display_credentials()   
    
def delete_credentials(credentials):
    """
    delete credentials from credential list
    """
    credentials.delete_credentials()
def find_credentials(account):
    """
    fumction that check if a credentials exists with that username and return true or false
    """
    return Credentials.find_credentialls(account) 

def credential_exist(account):
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
    while True:
        print("Use these short codes:\n CC --Create a new account.\n DC -Display Credentials. \n FC-- find credential. \n CP--copy password. \n DL-Delete credential. \n Ex -Exit the application. \n")      
        short_code =input().lower().strip()
        if short_code =='cc':
            print("Create New Credential")
            print("."*20)
            print("Account name: ")
            account = input()
            print("Your Account username")
            userName =input()  
            while True:
                print("TP --To type your own password : \n GP - to generate random password")
                password_Choice = input().lower().strip()
                if password_Choice =='tp':
                    password =input("Enter your own password \n")
                    break
                elif password_Choice =='gp':
                    password =generate_password()
                    break
                else:
                    print("Invalid password !. please try again")
            save_credential(create_new_credentials(account,userName,password))
            print('\n')
            print(f"Account Credentials for: {account} - username:{userName} - password:{password} created succesfully")
            print('\n')
        elif short_code =='dc':
            if display_account_details:
                print("Here is your List of accounts : ")
                print('*'*30) 
               
                for credentials in display_account_details():
                    print(f"Account: {credentials.account} \n Username: {credentials.userName}\n Password: {credentials.password}")
                    print('_' *30)
            else:
                print("You dont have any credentials saved yet !")
        elif short_code =='fc':
            print("Enter the account name you want to search for")
            search_name =input()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print(f"  Username: {search_credential.userName} password: {search_credential.password}")
                print('_'*50)
            else:
                print("that credential does not exist")
                print('\n')
        elif short_code =='dl':
            print("Enter the account name of the credential you want to delete")
            search_name =input()
            if credential_exist(search_name):
                search_credential =find_credentials(search_name)
                print('_'*50)
                delete_credentials(search_credential)
                print('\n')
                print(f"Your credentials for : {search_credential.account} have been deleted succesfully")    
                print("\n")
            else:
                print("That credential you want to delete doesnt exist") 
        elif short_code =='gp':  
            password =generate_password()
            print(f"{password} Has been generated succesfully. You can proceed to your account")  
            
            
        elif short_code =='cp':
            print("Enter the account of the password you want to copy")
            my_password =input()
            if credential_exist(my_password):
                myPassword = find_credentials(my_password)
                myPassword.copy_password(my_password)
                print("password copied")
                
            else:print("No password copied")    
                 
        elif short_code =='ex':
            print("Thank you for using Password Locker manager")
            break
        else:
            print("Wrong entry. Check your codes again")
    else:
        print("Please enter a valid input to continue")
if __name__ =='__main__':
    passlocker()                       
  