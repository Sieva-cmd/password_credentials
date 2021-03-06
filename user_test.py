from cgi import test
import unittest

import pyperclip
from user import User
from user import Credentials

class TestClass(unittest.TestCase):
    """
    A Test class that defines test cases for the User class 
    """
    def setUp(self) :
        """
        method that runs before each individual test method run
        """
        self.new_user =User('SievaLucia','zxcvbnm')
        
    def test_init(self):
        """
        test case to check if object has been initialized correctly
        """  
        self.assertEqual(self.new_user.username, 'SievaLucia')  
        self.assertEqual(self.new_user.password,'zxcvbnm')
        
    def test_save_user(self):
        """
        test case to test if new user instance has been saved
        """ 
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)   


class TestCredentials(unittest.TestCase):
    """
    Test case for credentential model class
    """   
    
    def setUp(self):
        """
        Method that runs before each credential test case runs
        """  
        self.new_credentials =Credentials('Gmail','musyoka_sieva','zxcvbnm')  
        
    def test_init(self):
        """
        test case to check if new credentials have ben initialized correctly
        """ 
        self.assertEqual(self.new_credentials.account,'Gmail') 
        self.assertEqual(self.new_credentials.userName,'musyoka_sieva') 
        self.assertEqual(self.new_credentials.password,'zxcvbnm') 
    def save_credential_test(self):
        """
        test case to see if credentials have been saved
        """ 
        self.new_credentials.save_details()
        self.assertEqual(len(Credentials.credentials_list),1)
        
    def tearDown(self):
        """
        method that does clean up after test case has run
        """
        Credentials.credentials_list =[]
        
    def test_save_many_accounts(self):
        """
        Test to check if we can save multiple account credentials
        """   
        self.new_credentials.save_details()
        test_credential =Credentials("Twitter","sieva Lucia",'zxcvbnm') 
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list),2)
    
    def test_delete_credential(self):
        """
        test method to test whether we can delete credentials
        """ 
        self.new_credentials.save_details()
        test_credential =Credentials("Twitter",'sieva Lucia','zxcvbnm')
        test_credential.save_details()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
    def test_find_credentials(self):
        """
        test to check if we can find a credential by account name and display details
        """ 
        self.new_credentials.save_details()
        test_credential =Credentials("Twitter","sieva Lucia","zxcvbnm")
        test_credential.save_details()
        
        found_credential =Credentials.find_credentialls("Twitter")  
        self.assertEqual(found_credential.account,test_credential.account)  
        
    def test_credential_exist(self):
        """
        test method to test if credentials exists
        """ 
        self.new_credentials.save_details()
        test_credential =Credentials("Twitter","sieva Lucia",'zxcvbnm')
        test_credential.save_details()
        credentials_found =Credentials.if_credential_exist("Twitter")
        self.assertTrue(credentials_found) 
        
    def test_display_all_saved_credentials(self):
        """
        test to display all credentials
        """  
        self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)  
        
    def test_copy_password(self):
        self.new_credentials.save_details()
        Credentials.copy_password("zxcvbnm")
        self.assertEqual(self.new_credentials.password,pyperclip.paste())
                       









if __name__ == "__main__":
    unittest.main()
        
     
    
    
    