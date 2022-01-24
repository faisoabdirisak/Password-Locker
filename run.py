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


def display_accounts_details():
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list

    """
    credentials.delete_credentials()


def find_credential(account):
    """
    Function that finds a Credentials by an account name and returns the Credentials that belong to that account
    """
    return Credentials.find_credential(account)


def check_credendtials(account):
    """
    Function that check if a Credentials exists with that account name and return true or false

    """
    return Credentials.if_credential_exist(account)


def main():
    print("Hello Welcome to your Accounts Password Store...\n ca--- Create New Account  \n")
    short_code = input("").lower()
    if short_code == "ca":
        print("Create new Account")
        print('*' * 50)
        username = input("User_name: ")
        password = input("Enter Password:")



if __name__ == '__main__':
    main()