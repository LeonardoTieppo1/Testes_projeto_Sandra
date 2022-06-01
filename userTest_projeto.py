import unittest

from user_projeto import User

class UserTest(unittest.TestCase):
    def test_user_login(self):
        print("Digite o seu usuário:")
        login=User().login(input())
        self.assertTrue(login)
        
    def test_user_password(self):
        print("\nDigite sua senha:")
        password=User().senha(input())
        self.assertTrue(password)
        
if __name__ == '__main__':
    unittest.main()