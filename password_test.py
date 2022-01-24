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
        Method that runs before each individual credentials test methods run.

        """
        self.new_credential = Credentials("twitter","faska-haji","faska12")

    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.account, "twitter")
        self.assertEqual(self.new_credential.userName, "faska-haji")
        self.assertEqual(self.new_credential.password, "faska12")








if __name__ == "__main__":
    unittest.main()
