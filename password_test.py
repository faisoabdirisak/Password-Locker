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