#! /user/bin/env/ python3

# from user import Credentials , User

# def createUser (username,password):
#     New_user = User(username,password)
#     return New_user

# def logIn (username,password):
#     real_user = User.real_user(username,password)
#     return real_user

# def save_user(user):
#     user.save_user()

# def create_credentials(account,username, password):
#     New_credentials =Credentials(account, username,password)
#     return New_credentials

# def save_credentials(credentials) :
#     Credentials.save_credentials(credentials)

# def delete_credentials(credentials):
#     credentials.delete_credentials()

# def display_credentials():
#     return Credentials.display_credentials()

# def Credentialsuser_exist(account):
#     return Credentials.credentialsuser_exist(account)

# def find_account(account):
#     return Credentials.find_account(account)

# def gen_password():
#     gen_password =Credentials.gen_password()
#     return gen_password

# def main():
#     while True:
#         print('Welcome to password locker. Use this commamd to continue, use ca to crete account,  lg to log in, ex to exit')
#         userinput = input().lower()
        
#         if userinput  == "ca":
#             print("Enter new account details")
#             username = input("enter your username: ")
#             # while True:
#             print("use E to enter password, use G to generate password, and X to exit")
#             password = input().lower()
#             if password == "e":
#                 password = input("enter password: ")
#             elif password == "g":
#                 password = gen_password()
#             else :
#                 print("Try again")  

#             save_user(createUser(username,password))  
#             print(f"Welcome {username} your password is {password}")

#         elif userinput  == "lg":
#             print("enter  username and password to log in ")
#             print("enter your username:")
#             username = input()
#             print("enter your password:")
#             password = input()
#             real_user = logIn (username,password)
#             if real_user == username:
#                 print(f"hello {username}")
#                 while True:
#                     print("use CR to creat credentials, DE to delete credentials ,DI to display credentials, FI find credentials , X exit")
#                     credentials_choice = input().lower()

#                     if credentials_choice == "cr":
#                         print("create credentials")
#                         input("enter account name: ")
#                         account =input()
#                         print ("enter username: ")
#                         username = input()
#                         print("use E to enter password, use G to generate password, and X to exit")
#                         password = input().lower()
#                         if password == "e":
#                             password = input("enter password: ")
#                         elif password == "g":
#                             password = gen_password()
#                         else :
#                             print("Try again")  


#                         save_credentials(create_credentials( account,username,password))  
#                         print(f"your  credentials are {account}, {username}, {password} has been created")

#                     elif credentials_choice == "de":
#                         print("enter account to delete")
#                         account = input()
#                         if find_account(account):
#                             account_delete = find_account(account)
#                             account_delete.delete_credentials()
#                             print("account sussessfuly deleted")
#                         else:
#                             print("account does not exist")    

#                     elif credentials_choice == "di":
#                         print("your credentials are")
#                         if  display_credentials():
#                             for account in  display_credentials():
#                                 print(f"account: {account} \n username: {username} \n password: {password} \n")
#                         else:
#                             print("no credentials found")         
                        

#                     elif credentials_choice == "fi":
#                         print("enter account to find")
#                         account = input("enter account name:")
#                         if find_account(account):
#                             account_name = find_account(account)
#                             print(f"account: {account_name.account} \n username: {account_name.username} \n password: {account_name.password} \n")


#                     else:
#                         print( "Bye")

#         else:
#             print("next time")



    

# if __name__ == "__main__":
#     main()










    

