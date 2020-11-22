import random
import string

class User:
    
    user_list = []
    
    def __init__(self,username,password):
        self.username = username
        self.password = password

    def save_user(self):
        User.user_list.append(self)

    @classmethod
    def real_user(cls,username,password):
        current_user = ''
        for user in User.user_list:
            if user.username == username and user.password == password:
                current_user = user.username
        return current_user        

class Credentials:
    user_credentials = []

    def __init__ (self,account,username,password):
        self.account = account
        self.username = username
        self.password = password

    def save_credentials(self):
        Credentials.user_credentials.append(self)

    def delete_credentials(self):
        Credentials.user_credentials.remove(self)

    @classmethod
    def credentialsuser_exist(cls,account):
        for credential in cls.user_credentials:
            if credential.account == account:
                return True
        return False        

    @classmethod
    def find_account(cls,account):
        for credential in cls.user_credentials:
            if credential.account == account:
                return credential

    @classmethod
    def display_credentials(cls):
        return cls.user_credentials

    def gen_password (stringL = 10):
                    password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "(|/~!.@,)#{?&[%]^}&*"
                    return ''.join(random.choice(password) for i in range (stringL))



            