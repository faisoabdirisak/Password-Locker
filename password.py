class User:
     """
    Create User class that creates  new instances of a user.

    """
     user_list = []

     def __init__(self, username, password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password

        # save user
     def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)


        # Credential class

class Credentials():
    """
    Create credentials class to help create new objects of credentials
    """
    credentials_list = []


    def __init__(self, account, userName, password):
        """
        method that defines user credentials to be stored
        """
        self.account = account
        self.userName = userName
        self.password = password        