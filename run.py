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

        save_user(create_new_user(username, password))
        print("*"*85)
        print(f"Hello {username}, Your account has been created succesfully and Your password is: {password}")
        print("*"*85)
        
        print(f"Hello {username}.Welcome To PassWord Locker Manager")
        print('\n')

        while True:
             print("Use these short codes:\n cc - Create a new credential \n dc - Display Credentials \n fc - Find a credential \n  del - Delete credential \n ex - Exit the application \n")
             short_code = input().lower()
             if short_code == "cc":
                print("Create New Credential")
                print("."*20)
                print("Account name ....")
                account = input().lower()
                print("Your Account username")
                userName = input()
                print("Account password")
                password = input("Enter Your Own Password\n")
                
                save_credentials(create_new_credential(
                account, userName, password))
                print('\n')
                print(f"Account Credential for: {account} - UserName: {userName} - Password:{password} created succesfully")
                print('\n')
             elif short_code == "dc":
                  if display_accounts_details():
                    print("Here are all lists of accounts: ")

                    print('*' * 30)
                    print('_' * 30)
                    for account in display_accounts_details():
                       print(f" Account:{account.account} \n User Name:{username}\n Password:{password}")
                       print('*' * 30)
                       print('*' * 30)
                  else:
                   print("You don't have any credentials saved yet in your account")
             elif short_code == "fc":
                  print("Enter the Account Name you want to search for")
                  search_name = input().lower()
                  if find_credential(search_name):
                    search_credential = find_credential(search_name)
                    print(f"Account Name : {search_credential.account}")
                    print('*' * 50)
                    print(f"User Name: {search_credential.userName} Password :{search_credential.password}")
                    print('*' * 50)
                  else:
                     print("That Credential does not exist in your store")
                     print('\n')
             elif short_code == "del":
                  print("Enter the account name of the Credentials you want to delete")
                  search_name = input().lower()
                  if find_credential(search_name):
                     search_credential = find_credential(search_name)
                     print("*"*50)
                     search_credential.delete_credentials()
                     print('\n')
                     print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                     print('\n')
                  else:
                    print("That Credential you want to delete does not exist in your store yet")

             elif short_code == 'ex':
                  print("Thanks for using passwords store manager.. See you next time!")
                  break
             else:
                 print("Wrong entry... Check your entry again and let it match those in the store")
        else:
           print("Please enter a valid input to continue using the store")



if __name__ == '__main__':
    main()