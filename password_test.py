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





if __name__ == "__main__":
    unittest.main()
