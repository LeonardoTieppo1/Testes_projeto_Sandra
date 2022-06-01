from datetime import date
import re

class Cadastro:
    def cad_nome(self,nome):
        if nome==re.sub('[0-9]','',nome):
            print("Nome validado!")
            return True
        else:
            print("Nome invalido!")
            return False

    def cad_sobrenome(self,sobrenome):
        if sobrenome==re.sub('[0-9]','',sobrenome):
            print("Sobrenome validado!")
            return True
        else:
            print("Sobrenome invalido!")
            return False

    def cad_cpf(self,cpf):
        cpf=[int(char)for char in cpf if char.isdigit()]
        if len(cpf)!=11:
            return False
        if (cpf==cpf[::-1]):
            return False
        for i in range(9,11):
            valor=sum((cpf[num]*((i+1)-num) for num in range (0,i)))            
            validar=((valor*10)%11)%10
            if validar!=cpf[i]:
                print("CPF invalido!")
                return False
            else:
                print("CPF validado!")
                return True
    def cad_dataNasc(self,ano,mes,dia):
        dataNasc=date(ano,mes,dia)
        anoN=dataNasc.year
        mesN=dataNasc.month
        diaN=dataNasc.day
        print(f"Data de nascimento:{diaN}/{mesN}/{anoN}")
        if mes>=13 or 1940>ano>=2012 or dia>31:
            print("Data de nascimento invalida!")
            return False 
        else:
            print("Data de nascimento validada!")
            return True
        
    def cad_username(self,username):
            s=0
            if(len(username)>=8):
                for i in username:
                    if(i=='@'or i=='$' or i=='_'): 
                        s+=1
                        if(s>=1):
                            print("Usuário validado!")
                            return True
                        else:
                            print("Usuário invalido!")
                            return False
            else:
                print("Usuário fora do tamanho necessário!")
                return False
        
    def cad_password(self,password):
        if(len(password)<=8):
            l, u, s, d = 0, 0, 0, 0
            print("Senha dentro do tamanho")
            for i in password: 
                if (i.islower()): 
                    l+=1            
                if (i.isupper()): 
                    u+=1            
                if (i.isdigit()): 
                    d+=1            
                if(i=="@" or i=="$" or i=="%" or i=="&" or i=="(" or i==")" or i=="."): 
                        s+=1           
            if (l>=1 and u>=1 and s>=1 and d>=1 and l+s+u+d==len(password)): 
                print("Senha validada!")
                return True 
            else: 
                print("Senha invalida!")
                return False 
        else:
            print("Senha maior que o necessário!")
            return False

#Salvar como cadastro_projeto.py