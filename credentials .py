import random
import string
import pyperclip

class User:
    """
    Create User class that generates new instances of user.
    """
    
    user_list = []
    
    def __init__(self,username,password):
        """
        method that defines the properties of a user.
        
        """
        
        self.username = username
        self.password =password
        
    def save_user(self):
        """
        A method that saves a new user instance into the user list
        """  
        User.user_list.append(self)   
    @classmethod
    def display_user(cls):
        return cls.user_list
    
    def delete_user(self):
        """
        delete_user method deletes a waved user account from the list
        
        """
        User.user_list.remove(self)
        
class Credentials():
    """
    Create credentials class to help create new objects of credentials
    
    """    
    credentials_list =[]
    
    @classmethod
    def verify_user(cls,username,password):
        """
        method to verify whether the user is in our user_list or not
        """
        a_user =""
        for user in User.user_list:
            if(user.username == username and user.password ==password):
                a_user ==user.username
        return a_user        
    
    def __init__(self,account,userName,password) :
        """
        method that defines user credentials to be stored
        
        """    
        self.account =account
        self.userName =userName
        self.password =password
        
    def save_details(self):
        """
        method to store a new credentials to the credentials list
        """   
        Credentials.credentials_list.append(self)
        
    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from credential_list
        """    
        Credentials.credentials_list.remove(self)
        
    @classmethod
    def find_credentialls(cls,account):
        """
        method that takes in account_name and returns a credentials that matvh account name
        """  
        for credential in cls.credentials_list:
            if credential.account ==account:
                return credential
            
    @classmethod
    def copy_password(cls,account):
        found_credentials =Credentials.find_credentialls(account)
        pyperclip.copy(found_credentials.password)
        pyperclip.paste()  
        
    @classmethod
    def if_credential_exist(cls,account):
        """
         method that checks if a credential exists from the crdential list and returns true or false depending if the credential exists.
        """ 
        for credential in cls.credentials_list:
            if credential.account ==account:
                return True
            return False
        
        
    @classmethod
    def display_crdentials(cls):
        """
        method that returns all items in credential list
        """ 
        return cls.credentials_list
    
    def generated_password(stringLength=8):
        """
        Generate a random password string of letters and digits and special characters
        """   
        password = string.ascii_uppercase +string.ascii_lowercase +string.digits + "~!@#$%^&*"
        return ''.join(random.choice(password) for i in range(stringLength))
                     
            
        