import unittest
from password import User,Credentials

class TestClass(unittest.TestCase):
    """
    A test class that defines test cases for the user class.
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_user =  User("faska-haji", "faska12")

    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, "faska-haji")
        self.assertEqual(self.new_user.password, "faska12")    

        #  save user
    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

# Credential class

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """

    def setUp(self):
        """
         setup Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials("twitter","faska-haji","faska12")

    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account, "twitter")
        self.assertEqual(self.new_credential.userName, "faska-haji")
        self.assertEqual(self.new_credential.password, "faska12")

    # save

    def save_credential_test(self):
        """
        test case to test if the crential object is saved into the credentials list.

        """
        self.new_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 1)
    
        #  deleting many accounts

    def tearDown(self):
        '''
        method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_many_accounts(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credential.save_details()
        test_credential = Credentials("facebook", "faska", "faska12")
        test_credential.save_details()
        self.assertEqual(len(Credentials.credentials_list), 2)    
           
    # deleting method

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_details()
        test_credential = Credentials("twitter", "faska-haji", "faska12")
        test_credential.save_details()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)

    #  finds accounts
    def test_find_credentialr(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        self.new_credential.save_details()
        test_credential = Credentials("twitter", "faska-haji", "faska12")
        test_credential.save_details()

        the_credential = Credentials.find_credential("twitter")

        self.assertEqual(the_credential.account, test_credential.account)






if __name__ == "__main__":
    unittest.main()
