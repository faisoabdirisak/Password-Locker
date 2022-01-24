import unittest
from password import User

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









if __name__ == "__main__":
    unittest.main()
