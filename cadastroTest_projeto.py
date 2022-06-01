import unittest
from cadastro_projeto import Cadastro

class cadastroTest(unittest.TestCase):
        def teste_cad_Anome(self):
                print("Digite o seu nome:")
                nomeC=Cadastro().cad_nome(input())
                self.assertTrue(nomeC)
                
        def teste_cad_Bsobrenome(self):
                print("\nDigite o seu sobrenome:")
                sobrenomeC=Cadastro().cad_sobrenome(input())
                self.assertTrue(sobrenomeC)
                
        def teste_cad_Ccpf(self):
                print("\nDigite o seu cpf:")
                cpfC=Cadastro().cad_cpf(input())
                self.assertTrue(cpfC)
        
        def teste_cad_DdataNasc(self):
                print("\nDigite a data de nascimento:\nYYYY \nMM \nDD):")
                dataNascC=Cadastro().cad_dataNasc(int(input()),int(input()),int(input()))
                self.assertTrue(dataNascC)
        
        def teste_cad_Eusername(self):
                print("\nDigite o seu username:")
                users=Cadastro().cad_username(input())
                self.assertTrue(users)
                
        def teste_cad_Fpass(self):
                print("\nDigite a senha:")
                passC=Cadastro().cad_password(input())
                self.assertTrue(passC)


if __name__ == '__main__':
    unittest.main()