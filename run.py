from password import User, Credentials

def create_new_user(username, password):
    '''
    Function to create a new user with a username and password
    '''
    new_user = User(username, password)
    return new_user

    # save 

def save_user(user):
    '''
    Function to save a new user
    '''
    user.save_user()    

def create_new_credential(account, userName, password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credentials(account, userName, password)
    return new_credential


def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials. save_details()    