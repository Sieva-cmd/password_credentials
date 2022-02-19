import unittest
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









if __name__ == "__main__":
    unittest.main()
        
     
    
    
    