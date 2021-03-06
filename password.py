import pyperclip


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

        # save 

    def save_details(self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credentials_list.append(self)
    
    # delete 
    def delete_credentials(self):
        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """
        Credentials.credentials_list.remove(self)     
        
        # finding contacts
    
    @classmethod
    def find_credential(cls, account):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return credential
     
    #  test existing credentials
    @classmethod
    def if_credential_exist(cls, account):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credentials_list:
            if credential.account == account:
                return True
        return False

    @classmethod
    def copy_password(cls, account):
        found_credentials = Credentials.find_credential(account)
        pyperclip.copy(found_credentials.password)

    
    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credentials_list      