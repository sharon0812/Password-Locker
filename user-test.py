import  unittest
from user import User, Credentials

class TestClass(unittest.TestCase):

    def test_init(self):
        self.assertEqual(self.new_user.username,"sharon")
        self.assertEqual(self.new_user.password,"sharon123")
        

    def setUp(self):

        self.new_user = User("sharon","sharon123")

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials= Credentials("account","sharon","sharon123")

    def tearDown(self):
        Credentials.user_credentials = []

    def test_details(self):
        self.assertEqual(self.new_credentials.account,"account")
        self.assertEqual(self.new_credentials.username,"sharon")
        self.assertEqual(self.new_credentials.password,"sharon123")
        

   

    def test_save_credentials(self):

        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.user_credentials),1)

    def find_credentials(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("account","username","password")
        test_credential.save_credentials()

        the_credential= Credentials.find_account("account")
        self.assertEqual(the_credential.account,test_credential.account)

    def test_exist(self):

        self.new_credentials.save_credentials()
        test_credential = Credentials("account","username","password")
        test_credential.save_credentials()

        search_credential = Credentials.credentialsuser_exist("account")
        self.assertTrue(search_credential)

    def delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("account","username","password")
        test_credential.save_credentials()

        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.user_credentials),1)

    def test_savemany_account(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("account","username","password")
        test_credential.save_credentials()

        self.assertEqual(len(Credentials.user_credentials),2)


    
if __name__ == '__main__':
        unittest.main()